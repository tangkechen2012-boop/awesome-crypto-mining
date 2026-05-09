#!/usr/bin/env python3
"""
Fetch new miner prices from bt-miners.com API and update price CSVs and daily-prices.json.

Usage:
    python3 scripts/fetch_miner_prices.py

Updates:
    miners/prices/<slug>.csv       — one row per day (idempotent)
    data/daily-prices.json         — today's snapshot
"""

import csv
import html
import json
import re
import requests
from datetime import date
from pathlib import Path

API_URL = "https://bt-miners.com/wp-json/wc/v2/list_income_product?Coin=All"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
}

ROOT = Path(__file__).parent.parent
PRICES_DIR = ROOT / "miners" / "prices"
DATA_DIR = ROOT / "data"


def slugify(name: str) -> str:
    name = name.lower()
    name = re.sub(r"[^a-z0-9\s-]", "", name)
    name = re.sub(r"[\s]+", "-", name.strip())
    name = re.sub(r"-+", "-", name)
    return name


def fetch_data():
    resp = requests.get(API_URL, headers=HEADERS, timeout=30)
    resp.raise_for_status()
    return resp.json()


def parse_miners(data):
    products = data.get("data", []) if isinstance(data, dict) else data
    miners = []
    for p in products:
        raw_price = p.get("price", None)
        if not raw_price:
            continue
        try:
            price = round(float(raw_price), 2)
        except (ValueError, TypeError):
            continue
        if price <= 0:
            continue

        name = html.unescape(
            p.get("custom_product_title", p.get("title", ""))
        ).replace(" | BT-MINERS", "").strip()

        if not name:
            continue

        miners.append({
            "slug": slugify(name),
            "name": name,
            "new_price_usd": price,
        })
    return miners


def update_csv(slug: str, today: str, new_price: float):
    PRICES_DIR.mkdir(parents=True, exist_ok=True)
    csv_path = PRICES_DIR / f"{slug}.csv"
    fieldnames = ["date", "new_price_usd", "used_price_usd", "used_source"]

    # Read existing rows
    rows = []
    if csv_path.exists():
        with open(csv_path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            rows = list(reader)

    # Check if today already exists (idempotent)
    for row in rows:
        if row.get("date") == today:
            return  # already recorded today

    rows.append({
        "date": today,
        "new_price_usd": f"{new_price:.2f}",
        "used_price_usd": "",
        "used_source": "",
    })

    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def write_daily_json(miners: list, today: str):
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    payload = {
        "date": today,
        "miners": [
            {
                "slug": m["slug"],
                "name": m["name"],
                "new_price_usd": m["new_price_usd"],
                "used_price_usd": None,
                "used_source": None,
            }
            for m in miners
        ],
    }
    out = DATA_DIR / "daily-prices.json"
    out.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
    return out


def main():
    today = date.today().isoformat()
    print(f"Fetching miner prices from bt-miners.com API ({today})...")

    data = fetch_data()
    miners = parse_miners(data)
    print(f"Found {len(miners)} miners with price data.")

    for m in miners:
        update_csv(m["slug"], today, m["new_price_usd"])

    out = write_daily_json(miners, today)
    print(f"Written: {out}")
    print(f"CSV files updated in: {PRICES_DIR}")

    if miners:
        sample = miners[0]
        print(f"Sample: {sample['name']} → ${sample['new_price_usd']}")


if __name__ == "__main__":
    main()
