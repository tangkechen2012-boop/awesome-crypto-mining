#!/usr/bin/env python3
"""
Fetch today's price for mineable coins via CoinGecko API.

Usage:
    python3 scripts/fetch_coin_prices.py [--days 1]

Outputs:
    coins/price-history/<symbol_lower>.csv  — one row per day (idempotent)
    data/coins-summary.json                 — latest prices for all coins
    coins/summary.md                        — human-readable price table
"""

import json
import time
import argparse
import requests
from pathlib import Path
from datetime import datetime

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

BASE_DIR = Path(__file__).parent.parent
PRICE_HISTORY_DIR = BASE_DIR / "coins" / "price-history"
DATA_DIR = BASE_DIR / "data"
SUMMARY_MD = BASE_DIR / "coins" / "summary.md"

HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; research/1.0)"}

COINS = [
    {"id": "bitcoin",           "symbol": "BTC",  "name": "Bitcoin",          "algo": "SHA-256"},
    {"id": "zcash",             "symbol": "ZEC",  "name": "Zcash",            "algo": "Equihash"},
    {"id": "monero",            "symbol": "XMR",  "name": "Monero",           "algo": "RandomX"},
    {"id": "kaspa",             "symbol": "KAS",  "name": "Kaspa",            "algo": "kHeavyHash"},
    {"id": "ethereum-classic",  "symbol": "ETC",  "name": "Ethereum Classic", "algo": "ETHash"},
    {"id": "litecoin",          "symbol": "LTC",  "name": "Litecoin",         "algo": "Scrypt"},
    {"id": "dogecoin",          "symbol": "DOGE", "name": "Dogecoin",         "algo": "Scrypt"},
    {"id": "alephium",          "symbol": "ALPH", "name": "Alephium",         "algo": "Blake3"},
]

CSV_HEADER = "date,price_usd,volume_usd,market_cap_usd\n"


# ---------------------------------------------------------------------------
# API helpers
# ---------------------------------------------------------------------------

def fetch_today_price(coin_id):
    """
    Fetch current price, 24h volume, and market cap from CoinGecko simple/price.
    Returns dict or None on failure.
    """
    url = (
        f"https://api.coingecko.com/api/v3/simple/price"
        f"?ids={coin_id}&vs_currencies=usd"
        f"&include_24hr_vol=true&include_market_cap=true"
    )
    try:
        resp = requests.get(url, headers=HEADERS, timeout=20)
        if resp.status_code == 429:
            print(f"  WARNING: rate limited (429) for {coin_id}, skipping.")
            return None
        resp.raise_for_status()
        data = resp.json().get(coin_id, {})
        return {
            "price_usd":      data.get("usd", 0),
            "volume_usd":     data.get("usd_24h_vol", 0),
            "market_cap_usd": data.get("usd_market_cap", 0),
        }
    except Exception as e:
        print(f"  ERROR fetching {coin_id}: {e}")
        return None


# ---------------------------------------------------------------------------
# CSV helpers
# ---------------------------------------------------------------------------

def csv_path(symbol):
    return PRICE_HISTORY_DIR / f"{symbol.lower()}.csv"


def date_already_in_csv(path, today):
    """Return True if today's row already exists in the CSV."""
    if not path.exists():
        return False
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            if line.startswith(today):
                return True
    return False


def append_csv_row(path, today, price_data):
    """Write CSV header on creation, then append one row."""
    new_file = not path.exists()
    with open(path, "a", encoding="utf-8") as f:
        if new_file:
            f.write(CSV_HEADER)
        f.write(
            f"{today},{price_data['price_usd']},{price_data['volume_usd']},"
            f"{price_data['market_cap_usd']}\n"
        )


# ---------------------------------------------------------------------------
# Output generators
# ---------------------------------------------------------------------------

def format_billions(value):
    """Format a large USD number into a readable string like $28.5B."""
    if value >= 1e12:
        return f"${value / 1e12:.1f}T"
    if value >= 1e9:
        return f"${value / 1e9:.1f}B"
    if value >= 1e6:
        return f"${value / 1e6:.1f}M"
    return f"${value:,.0f}"


def format_price(p):
    if p >= 1000:
        return f"${p:,.2f}"
    if p >= 1:
        return f"${p:.4f}"
    if p >= 0.001:
        return f"${p:.6f}"
    return f"${p:.8f}"


def write_coins_summary_json(results, today):
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    out = {
        "date": today,
        "coins": [
            {
                "symbol":         r["symbol"],
                "name":           r["name"],
                "algo":           r["algo"],
                "price_usd":      r["price_usd"],
                "volume_usd":     r["volume_usd"],
                "market_cap_usd": r["market_cap_usd"],
            }
            for r in results
        ],
    }
    dest = DATA_DIR / "coins-summary.json"
    dest.write_text(json.dumps(out, indent=2), encoding="utf-8")
    print(f"  Wrote {dest}")


def write_summary_md(results, today):
    lines = [
        "# \U0001f4b0 Coin Prices",
        "",
        f"> **Last updated:** {today} | **Source:** CoinGecko",
        "",
        "<!-- AUTO-UPDATED BY GITHUB ACTIONS -->",
        "",
        "| Coin | Algorithm | Price (USD) | 24h Volume | Market Cap | Details |",
        "|------|-----------|-------------|------------|------------|---------|",
    ]
    for r in results:
        symbol = r["symbol"]
        coin_id = r["id"]
        lines.append(
            f"| {symbol} | {r['algo']} | {format_price(r['price_usd'])} "
            f"| {format_billions(r['volume_usd'])} "
            f"| {format_billions(r['market_cap_usd'])} "
            f"| [View](coins/{coin_id}.md) |"
        )
    SUMMARY_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"  Wrote {SUMMARY_MD}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Fetch today's coin prices from CoinGecko.")
    parser.add_argument("--days", type=int, default=1,
                        help="Number of days to fetch (default 1 = today only)")
    args = parser.parse_args()

    today = datetime.utcnow().strftime("%Y-%m-%d")
    PRICE_HISTORY_DIR.mkdir(parents=True, exist_ok=True)

    results = []

    for coin in COINS:
        symbol = coin["symbol"]
        print(f"\n{symbol} ({coin['name']})...")

        path = csv_path(symbol)

        # Idempotency check
        if date_already_in_csv(path, today):
            print(f"  Already have {today} in {path.name}, skipping fetch.")
            # Still include in results if we can read from CSV
            with open(path, "r", encoding="utf-8") as f:
                for line in f:
                    if line.startswith(today):
                        parts = line.strip().split(",")
                        if len(parts) == 4:
                            results.append({
                                **coin,
                                "price_usd":      float(parts[1]),
                                "volume_usd":     float(parts[2]),
                                "market_cap_usd": float(parts[3]),
                            })
                        break
            continue

        data = fetch_today_price(coin["id"])
        if data is None:
            continue

        append_csv_row(path, today, data)
        print(f"  Appended {today} → {path.name}  price={format_price(data['price_usd'])}")

        results.append({**coin, **data})

        time.sleep(2)  # CoinGecko free tier rate limit

    if results:
        write_coins_summary_json(results, today)
        write_summary_md(results, today)
    else:
        print("\nNo data collected — nothing written.")

    print(f"\nDone! {len(results)} coins processed.")


if __name__ == "__main__":
    main()
