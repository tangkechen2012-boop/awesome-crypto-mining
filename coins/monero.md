# Monero (XMR) Mining Guide

> **Algorithm:** RandomX | **Current Price:** ~$230 | **[Price History](price-history/xmr.csv)**

## Overview

Monero is the leading privacy cryptocurrency, offering untraceable transactions through ring signatures, stealth addresses, and RingCT. Its RandomX algorithm is specifically designed to be ASIC-resistant by favoring general-purpose CPUs, making it one of the few coins where consumer hardware remains competitive. Monero has a "tail emission" of 0.6 XMR per block indefinitely after the main emission curve ends, ensuring miners are always incentivized.

## Mining Specifications

| Parameter | Value |
|-----------|-------|
| Algorithm | RandomX |
| Block Time | ~2 minutes |
| Block Reward | ~0.6 XMR (tail emission) |
| Network Hashrate | ~3.2 GH/s |
| Mining Difficulty | Adjusts every block |

## Best Hardware for XMR

| Hardware | Hashrate | Power | Est. Daily Profit* | Notes |
|----------|----------|-------|-------------------|-------|
| AMD Ryzen 9 7950X | ~25,000 H/s | 170W | ~$0.80–$1.20 | Best consumer CPU |
| AMD EPYC 7742 | ~44,000 H/s | 225W | ~$1.40–$2.00 | Server-grade, high upfront cost |
| AMD Ryzen 9 5950X | ~19,500 H/s | 142W | ~$0.60–$1.00 | Good efficiency |
| Intel Core i9-13900K | ~8,000 H/s | 125W | ~$0.25–$0.50 | Less efficient than AMD |

*At $0.06/kWh electricity cost. Check [live rankings](../miners/index.md) for current data.

> **Note:** No ASICs are listed because RandomX is designed to invalidate ASIC advantages. AMD Zen-architecture CPUs dominate due to their large L3 cache.

## Recommended Mining Pools

| Pool | Fee | Payout | URL |
|------|-----|--------|-----|
| SupportXMR | 0.6% | PPLNS | [supportxmr.com](https://supportxmr.com) |
| MoneroOcean | 0% (algorithm switching) | PPLNS | [moneroocean.stream](https://moneroocean.stream) |
| MineXMR | 1% | PPLNS | [minexmr.com](https://minexmr.com) |
| 2Miners | 1% | PPLNS | [xmr.2miners.com](https://xmr.2miners.com) |

## Price History

[View full daily price history →](price-history/xmr.csv)

## Is XMR Worth Mining Right Now?

Monero is unique because anyone with a modern CPU can participate without specialized hardware investment. At $230/XMR and modest electricity costs, a high-end AMD Ryzen or EPYC system can generate a small but consistent return. MoneroOcean is especially popular because it auto-switches to the most profitable RandomX-family coin at any moment. XMR mining is best suited for those who already own capable CPUs (e.g., home servers, workstations) and want to put idle compute to work with minimal upfront cost.
