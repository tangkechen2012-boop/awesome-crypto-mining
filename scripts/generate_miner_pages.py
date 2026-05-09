#!/usr/bin/env python3
"""Generate miner detail pages for the top 20 most profitable miners."""

import json
import os
import re
from pathlib import Path

# Coin mapping: algo keyword in name/coin -> (algo label, coins list, coin page links)
COIN_MAP = {
    "BTC": ("SHA-256", ["BTC", "FB", "NMC"], [
        "[BTC](../../coins/bitcoin.md)",
        "FB",
        "NMC",
    ]),
    "ZEC": ("Equihash", ["ZEC"], ["[ZEC](../../coins/zcash.md)"]),
    "XMR": ("RandomX", ["XMR"], ["[XMR](../../coins/monero.md)"]),
    "LTC": ("Scrypt", ["LTC", "DOGE"], [
        "[LTC](../../coins/litecoin.md)",
        "[DOGE](../../coins/dogecoin.md)",
    ]),
    "ETC": ("ETHash", ["ETC"], ["[ETC](../../coins/ethereum-classic.md)"]),
    "KAS": ("kHeavyHash", ["KAS"], ["[KAS](../../coins/kaspa.md)"]),
    "ALPH": ("Blake3", ["ALPH"], ["[ALPH](../../coins/alephium.md)"]),
    "INITVERSE": ("VersaHash/InitVerse", ["INI"], ["INI"]),
}


def get_algo_and_coins(coin_field: str):
    """Map the coin field from profitability data to algo + coin links."""
    coin_upper = coin_field.upper()
    for key, (algo, coins, links) in COIN_MAP.items():
        if key in coin_upper:
            return algo, ", ".join(coins), ", ".join(links)
    # Fallback
    return "Unknown", coin_field, coin_field


def compute_efficiency(hashrate_str: str, power_w: int) -> str:
    """Compute efficiency in J/TH or J/GH based on hashrate string."""
    hr = hashrate_str.upper()
    val_match = re.match(r"([0-9.]+)(.*)", hr)
    if not val_match:
        return "N/A"
    val = float(val_match.group(1))
    unit = val_match.group(2).strip()

    # Normalise to TH
    if unit == "TH" or unit == "PH":
        if unit == "PH":
            val_th = val * 1000
        else:
            val_th = val
        eff = power_w / val_th
        return f"{eff:.2f} J/TH"
    elif unit in ("GH", "GS", "G/S"):
        eff = power_w / val
        return f"{eff:.2f} J/GH"
    elif unit in ("MH", "MS"):
        eff = power_w / (val / 1000)
        return f"{eff:.2f} J/GH"
    elif unit in ("KH", "KS", "KSOL"):
        eff = power_w / (val / 1_000_000)
        return f"{eff:.2f} J/TH"
    else:
        return "N/A"


def generate_page(miner: dict, new_price: float | None) -> str:
    slug = miner["slug"]
    name = miner["name"]
    coin_field = miner["coin"]
    daily = miner["daily_profit_usd"]
    monthly = miner["monthly_profit_usd"]
    hashrate = miner["hashrate"]
    power_w = miner["power_w"]

    algo, coins_plain, coins_links = get_algo_and_coins(coin_field)
    efficiency = compute_efficiency(hashrate, power_w)

    # Break-even in days (handle div-by-zero)
    if new_price and daily > 0:
        breakeven = f"{new_price / daily:.0f} days"
    else:
        breakeven = "N/A"

    price_str = f"${new_price:,.0f}" if new_price else "*Contact for pricing*"

    page = f"""# {name}

> **Algorithm:** {algo} | **Coins:** {coins_plain} | **[Buy New →](https://bt-miners.com)**

## Specifications

| Parameter | Value |
|-----------|-------|
| Hashrate | {hashrate} |
| Power Consumption | {power_w}W |
| Efficiency | {efficiency} |
| Algorithm | {algo} |
| Mineable Coins | {coins_links} |
| Noise Level | ~75dB |

## Current Profitability

> ⚡ Auto-updated daily. Assumes **$0.06/kWh** electricity cost.

| Coin | Daily Profit | Monthly Profit | Break-even |
|------|-------------|----------------|------------|
| {coins_plain} | ${daily:.2f} | ${monthly:.2f} | {breakeven} |

## Prices

| Type | Price | Source |
|------|-------|--------|
| New | {price_str} | [bt-miners.com](https://bt-miners.com) |
| Used (market avg) | *Check listings* | [marketplace](../../marketplace/listings.md) |

## Historical Data

- 📈 [Profitability history](../profitability/{slug}.csv)
- 💰 [Price history](../prices/{slug}.csv)

## Where to Buy

- 🆕 **New:** [bt-miners.com](https://bt-miners.com/shop) — ships worldwide
- ♻️ **Used:** [View current listings](../../marketplace/listings.md) or inquire via [@MiningDealBot](https://t.me/MiningDealBot)
"""
    return page


def main():
    base_dir = Path(__file__).parent.parent
    prof_path = base_dir / "data" / "daily-profitability.json"
    prices_path = base_dir / "data" / "daily-prices.json"
    out_dir = base_dir / "miners" / "specs"
    out_dir.mkdir(parents=True, exist_ok=True)

    with open(prof_path) as f:
        prof_data = json.load(f)

    with open(prices_path) as f:
        prices_data = json.load(f)

    prices_lookup = {m["slug"]: m.get("new_price_usd") for m in prices_data["miners"]}

    top20 = prof_data["miners"][:20]

    generated = []
    for miner in top20:
        slug = miner["slug"]
        new_price = prices_lookup.get(slug)
        page = generate_page(miner, new_price)
        out_path = out_dir / f"{slug}.md"
        out_path.write_text(page)
        generated.append((slug, miner["name"], miner["daily_profit_usd"]))
        print(f"  Generated: {slug}.md  (${miner['daily_profit_usd']}/day)")

    print(f"\nDone — {len(generated)} pages written to {out_dir}")


if __name__ == "__main__":
    main()
