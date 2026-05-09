#!/usr/bin/env python3
"""
fetch_ebay_prices.py — Scrape eBay sold listings for used miner prices.

For each miner in MINERS:
  1. Fetch eBay completed/sold listings page
  2. Parse sold prices, remove outliers, take median
  3. Update miners/prices/<slug>.csv with used_price_usd + used_source="ebay"
  4. Update data/daily-prices.json with the same used price

Usage:
    python3 scripts/fetch_ebay_prices.py
"""

import csv
import json
import os
import re
import statistics
import time
import urllib.parse
from datetime import date
from pathlib import Path
from typing import Optional

import requests
from bs4 import BeautifulSoup

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

REPO_ROOT = Path(__file__).resolve().parent.parent
PRICES_DIR = REPO_ROOT / "miners" / "prices"
DAILY_JSON = REPO_ROOT / "data" / "daily-prices.json"

TODAY = date.today().isoformat()

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
}

SLEEP_BETWEEN_REQUESTS = 3  # seconds

MINERS = [
    {"slug": "antminer-s21-xp",        "query": "Antminer S21 XP"},
    {"slug": "antminer-s21-pro",        "query": "Antminer S21 Pro"},
    {"slug": "antminer-s21",            "query": "Antminer S21 270T"},
    {"slug": "whatsminer-m60s",         "query": "WhatsMiner M60S"},
    {"slug": "whatsminer-m66s",         "query": "WhatsMiner M66S"},
    {"slug": "iceriver-ks5-pro",        "query": "IceRiver KS5 Pro"},
    {"slug": "iceriver-ks3",            "query": "IceRiver KS3"},
    {"slug": "antminer-ks5-pro",        "query": "Antminer KS5 Pro"},
    {"slug": "antminer-l9",             "query": "Antminer L9"},
    {"slug": "elphapex-dg1",            "query": "Elphapex DG1"},
    {"slug": "antminer-z15-pro",        "query": "Antminer Z15 Pro"},
    {"slug": "goldshell-al-box",        "query": "Goldshell AL-BOX"},
    {"slug": "antminer-s19k-pro",       "query": "Antminer S19k Pro"},
    {"slug": "canaan-avalon-a15",       "query": "Canaan Avalon A15"},
    {"slug": "bitdeer-sealminer-a2",    "query": "Bitdeer SealMiner A2"},
    {"slug": "antminer-d9",             "query": "Antminer D9"},
    {"slug": "antminer-e9-pro",         "query": "Antminer E9 Pro"},
    {"slug": "iceriver-ks0-pro",        "query": "IceRiver KS0 Pro"},
    {"slug": "antminer-l7",             "query": "Antminer L7"},
    {"slug": "goldshell-ck6",           "query": "Goldshell CK6"},
]

MIN_LISTINGS = 3  # need at least this many sold prices to compute a median


# ---------------------------------------------------------------------------
# eBay scraping helpers
# ---------------------------------------------------------------------------

def build_ebay_url(query: str) -> str:
    """Return an eBay sold-listings search URL for *query*."""
    params = {
        "_nkw": query,
        "LH_Sold": "1",
        "LH_Complete": "1",
        "_sop": "13",  # sort: newly listed
    }
    return "https://www.ebay.com/sch/i.html?" + urllib.parse.urlencode(params)


def parse_price(text: str) -> Optional[float]:
    """Extract the first USD dollar amount from a string like '$1,234.56'."""
    text = text.strip()
    # Handle price ranges like "$1,000.00 to $2,000.00" — use the lower bound
    match = re.search(r"\$([0-9,]+(?:\.[0-9]{1,2})?)", text)
    if match:
        return float(match.group(1).replace(",", ""))
    return None


def remove_outliers(prices: list[float]) -> list[float]:
    """
    Remove outliers using the 1.5×IQR rule.
    Returns the filtered list (may be empty if all values are outliers).
    """
    if len(prices) < 4:
        return prices  # not enough data for meaningful IQR filtering

    sorted_p = sorted(prices)
    n = len(sorted_p)
    q1 = statistics.median(sorted_p[: n // 2])
    q3 = statistics.median(sorted_p[(n + 1) // 2 :])
    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr
    return [p for p in prices if lower <= p <= upper]


def fetch_ebay_used_price(query: str) -> Optional[float]:
    """
    Scrape eBay for sold listings matching *query*.
    Returns the median sold price (USD) or None if fewer than MIN_LISTINGS found.
    """
    url = build_ebay_url(query)
    try:
        resp = requests.get(url, headers=HEADERS, timeout=20)
        resp.raise_for_status()
    except requests.RequestException as exc:
        print(f"  [WARNING] HTTP error fetching eBay for '{query}': {exc}")
        return None

    soup = BeautifulSoup(resp.text, "html.parser")

    # Primary selector: eBay's standard price span
    price_elements = soup.select("span.s-item__price")

    # Fallback: look for any element whose class contains "s-item__price"
    if not price_elements:
        price_elements = soup.find_all(
            lambda tag: tag.get("class")
            and any("s-item__price" in c for c in tag.get("class", []))
        )

    raw_prices: list[float] = []
    for el in price_elements:
        text = el.get_text(strip=True)
        price = parse_price(text)
        if price is not None and price > 0:
            raw_prices.append(price)

    if len(raw_prices) < MIN_LISTINGS:
        print(
            f"  [WARNING] Only {len(raw_prices)} sold listing(s) found for '{query}' "
            f"(need {MIN_LISTINGS}). Skipping."
        )
        return None

    filtered = remove_outliers(raw_prices)
    if len(filtered) < MIN_LISTINGS:
        print(
            f"  [WARNING] After outlier removal only {len(filtered)} listing(s) remain "
            f"for '{query}'. Skipping."
        )
        return None

    median_price = statistics.median(filtered)
    print(
        f"  Found {len(raw_prices)} listings → {len(filtered)} after filtering → "
        f"median ${median_price:,.2f}"
    )
    return round(median_price, 2)


# ---------------------------------------------------------------------------
# CSV helpers
# ---------------------------------------------------------------------------

CSV_FIELDNAMES = ["date", "new_price_usd", "used_price_usd", "used_source"]


def find_csv_for_slug(slug: str) -> Optional[Path]:
    """
    Return the CSV path whose filename *starts with* the given slug.
    The Task-6 CSVs may have a longer name (e.g., appended model suffix), so
    we do a prefix match.  Returns None if not found.
    """
    # Exact match first
    exact = PRICES_DIR / f"{slug}.csv"
    if exact.exists():
        return exact

    # Prefix match (slug is a prefix of the filename stem)
    for p in PRICES_DIR.glob("*.csv"):
        if p.stem.startswith(slug):
            return p

    return None


def update_csv(csv_path: Path, used_price: float) -> None:
    """
    Read the CSV at *csv_path*, update or create today's row with the given
    used_price_usd and used_source="ebay", then write the file back.
    """
    rows: list[dict] = []
    if csv_path.exists():
        with csv_path.open(newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            rows = list(reader)

    # Find today's row
    today_row = next((r for r in rows if r.get("date") == TODAY), None)

    if today_row is not None:
        today_row["used_price_usd"] = f"{used_price:.2f}"
        today_row["used_source"] = "ebay"
    else:
        # Create a new row for today with null new_price_usd
        rows.append(
            {
                "date": TODAY,
                "new_price_usd": "",
                "used_price_usd": f"{used_price:.2f}",
                "used_source": "ebay",
            }
        )
        # Keep rows sorted by date
        rows.sort(key=lambda r: r.get("date", ""))

    with csv_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=CSV_FIELDNAMES)
        writer.writeheader()
        writer.writerows(rows)


# ---------------------------------------------------------------------------
# daily-prices.json helper
# ---------------------------------------------------------------------------

def update_daily_json(slug: str, used_price: float) -> None:
    """
    Load data/daily-prices.json, update the entry for *slug* with
    used_price_usd and used_source="ebay", then write back.

    If the file doesn't exist or the slug isn't present, a minimal entry is
    created so that the file always reflects the latest used prices.
    """
    if DAILY_JSON.exists():
        with DAILY_JSON.open(encoding="utf-8") as f:
            data = json.load(f)
    else:
        data = {"date": TODAY, "miners": []}

    miners: list[dict] = data.get("miners", [])

    # Find existing entry by slug (exact or prefix match)
    entry = next(
        (
            m
            for m in miners
            if m.get("slug") == slug or m.get("slug", "").startswith(slug)
        ),
        None,
    )

    if entry is not None:
        entry["used_price_usd"] = used_price
        entry["used_source"] = "ebay"
    else:
        # Add a minimal entry
        miners.append(
            {
                "slug": slug,
                "name": slug,  # best we can do without extra metadata
                "new_price_usd": None,
                "used_price_usd": used_price,
                "used_source": "ebay",
            }
        )
        data["miners"] = miners

    DAILY_JSON.parent.mkdir(parents=True, exist_ok=True)
    with DAILY_JSON.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
        f.write("\n")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    print(f"fetch_ebay_prices.py — {TODAY}")
    print(f"Prices dir : {PRICES_DIR}")
    print(f"Daily JSON : {DAILY_JSON}")
    print()

    results: dict[str, float] = {}  # slug → used_price

    for miner in MINERS:
        slug = miner["slug"]
        query = miner["query"]
        print(f"[{slug}] Querying eBay: '{query}'")

        try:
            used_price = fetch_ebay_used_price(query)
        except Exception as exc:  # pylint: disable=broad-except
            print(f"  [ERROR] Unexpected error for '{slug}': {exc}")
            used_price = None

        if used_price is not None:
            results[slug] = used_price

            csv_path = find_csv_for_slug(slug)
            if csv_path is None:
                # No CSV yet — create one
                csv_path = PRICES_DIR / f"{slug}.csv"
                csv_path.parent.mkdir(parents=True, exist_ok=True)
                print(f"  Creating new CSV: {csv_path.name}")

            try:
                update_csv(csv_path, used_price)
                print(f"  Updated CSV : {csv_path.name}")
            except Exception as exc:  # pylint: disable=broad-except
                print(f"  [ERROR] Could not update CSV for '{slug}': {exc}")

            try:
                update_daily_json(slug, used_price)
                print(f"  Updated JSON: {DAILY_JSON.name}")
            except Exception as exc:  # pylint: disable=broad-except
                print(f"  [ERROR] Could not update daily JSON for '{slug}': {exc}")

        print()
        time.sleep(SLEEP_BETWEEN_REQUESTS)

    # Summary
    print("=" * 60)
    print(f"Done. Updated {len(results)}/{len(MINERS)} miners with eBay used prices.")
    for slug, price in results.items():
        print(f"  {slug}: ${price:,.2f}")


if __name__ == "__main__":
    main()
