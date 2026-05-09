#!/usr/bin/env python3
"""
Fetch daily miner profitability from bt-miners.com API.

Updates:
    miners/profitability/<slug>.csv  — appends one row per day (idempotent)
    miners/index.md                  — ranked miner table
    data/daily-profitability.json    — full snapshot for today
"""

import csv
import html
import json
import re
import requests
from datetime import datetime
from pathlib import Path

API_URL = "https://bt-miners.com/wp-json/wc/v2/list_income_product?Coin=All"
ELECTRICITY_COST = 0.06  # $/kWh

ROOT = Path(__file__).parent.parent
PROFITABILITY_DIR = ROOT / "miners" / "profitability"
INDEX_MD = ROOT / "miners" / "index.md"
DAILY_JSON = ROOT / "data" / "daily-profitability.json"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
}


def make_slug(name: str) -> str:
    name = name.lower()
    name = re.sub(r"[^a-z0-9\s-]", "", name)
    name = re.sub(r"\s+", "-", name.strip())
    name = re.sub(r"-+", "-", name)
    return name


def fetch_miners():
    resp = requests.get(API_URL, headers=HEADERS, timeout=30)
    resp.raise_for_status()
    return resp.json()


def parse_miners(data):
    miners = []
    products = data.get("data", []) if isinstance(data, dict) else data
    for p in products:
        daily_profit = float(p.get("value", 0) or 0)
        hashrate_val = p.get("hashrate_disp", "")
        hashrate_unit = p.get("hashrate_disp_", "")
        name = html.unescape(
            p.get("custom_product_title", p.get("title", ""))
        ).replace(" | BT-MINERS", "").strip()
        hashrate = f"{hashrate_val}{hashrate_unit}".strip()
        power = round(float(p.get("power", 0) or 0))
        monthly_profit = round(daily_profit * 30, 2)
        miners.append({
            "slug": make_slug(name),
            "name": name,
            "coin": p.get("coin", ""),
            "daily_profit_usd": daily_profit,
            "monthly_profit_usd": monthly_profit,
            "hashrate": hashrate,
            "power_w": power,
        })
    return sorted(miners, key=lambda x: x["daily_profit_usd"], reverse=True)


def update_csv(miner, today):
    PROFITABILITY_DIR.mkdir(parents=True, exist_ok=True)
    path = PROFITABILITY_DIR / f"{miner['slug']}.csv"
    # Check idempotency
    if path.exists():
        with open(path, newline="") as f:
            for row in csv.DictReader(f):
                if row.get("date") == today:
                    return  # already recorded today
    write_header = not path.exists()
    with open(path, "a", newline="") as f:
        writer = csv.writer(f)
        if write_header:
            writer.writerow([
                "date", "daily_profit_usd", "monthly_profit_usd",
                "coin", "hashrate", "power_w", "electricity_cost"
            ])
        writer.writerow([
            today,
            miner["daily_profit_usd"],
            miner["monthly_profit_usd"],
            miner["coin"],
            miner["hashrate"],
            miner["power_w"],
            ELECTRICITY_COST,
        ])


def write_index(miners, today):
    profitable = [m for m in miners if m["daily_profit_usd"] > 0]
    lines = [
        "# ⛏️ Miner Profitability Rankings",
        "",
        f"> **Last updated:** {today} | **Electricity cost:** ${ELECTRICITY_COST}/kWh | **Source:** bt-miners.com API",
        "",
        "<!-- AUTO-UPDATED BY GITHUB ACTIONS -->",
        "",
        "| Rank | Miner | Coin | Daily Profit | Monthly | Hashrate | Power | Details |",
        "|------|-------|------|-------------|---------|----------|-------|---------|",
    ]
    for i, m in enumerate(profitable, 1):
        daily = f"${m['daily_profit_usd']:.2f}" if m["daily_profit_usd"] else "—"
        monthly = f"${m['monthly_profit_usd']:.2f}" if m["monthly_profit_usd"] else "—"
        power_fmt = f"{m['power_w']:,}W" if m["power_w"] else "—"
        lines.append(
            f"| {i} | {m['name']} | {m['coin']} | {daily} | {monthly} | "
            f"{m['hashrate']} | {power_fmt} | [View](miners/specs/{m['slug']}.md) |"
        )
    INDEX_MD.parent.mkdir(parents=True, exist_ok=True)
    INDEX_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_daily_json(miners, today):
    profitable = [m for m in miners if m["daily_profit_usd"] > 0]
    payload = {
        "date": today,
        "electricity_cost_kwh": ELECTRICITY_COST,
        "total_miners": len(miners),
        "profitable_miners": len(profitable),
        "miners": profitable,
    }
    DAILY_JSON.parent.mkdir(parents=True, exist_ok=True)
    DAILY_JSON.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")


def main():
    today = datetime.now().strftime("%Y-%m-%d")
    print(f"Fetching miner data from bt-miners.com API (date: {today})...")
    data = fetch_miners()
    miners = parse_miners(data)
    profitable = [m for m in miners if m["daily_profit_usd"] > 0]
    print(f"Fetched {len(miners)} miners, {len(profitable)} profitable.")

    csv_count = 0
    for m in miners:
        if m["daily_profit_usd"] > 0:
            update_csv(m, today)
            csv_count += 1

    write_index(miners, today)
    write_daily_json(miners, today)

    print(f"CSV files updated: {csv_count}")
    print(f"Index written: {INDEX_MD}")
    print(f"Daily JSON written: {DAILY_JSON}")


if __name__ == "__main__":
    main()
