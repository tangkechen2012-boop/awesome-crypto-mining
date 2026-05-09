# Dogecoin (DOGE) Mining Guide

> **Algorithm:** Scrypt (merge-mined with LTC) | **Current Price:** ~$0.18 | **[Price History](price-history/doge.csv)**

## Overview

Dogecoin started as a meme cryptocurrency in 2013 but has grown into one of the top 10 coins by market cap, driven by a passionate community and high-profile endorsements. It uses the same Scrypt algorithm as Litecoin and has been merge-mined with LTC since 2014. This means **DOGE is earned automatically** when you mine Litecoin — you do not need separate hardware, separate pools, or any additional configuration. Every LTC miner is also a DOGE miner by default.

## Mining Specifications

| Parameter | Value |
|-----------|-------|
| Algorithm | Scrypt (merge-mined with Litecoin) |
| Block Time | ~1 minute |
| Block Reward | 10,000 DOGE per block |
| Network Hashrate | Shared with Litecoin (~1.5 PH/s) |
| Mining Difficulty | Adjusts with each block (DigiShield) |

## How Merge-Mining Works

Merge-mining (also called Auxiliary Proof of Work, or AuxPoW) allows miners to solve a single Scrypt proof-of-work puzzle that simultaneously satisfies the requirements for both Litecoin and Dogecoin. From a miner's perspective:

1. Point your Scrypt ASIC at a Litecoin pool that supports merge-mining (most major ones do)
2. Your pool automatically submits valid shares to both LTC and DOGE networks
3. Both LTC and DOGE rewards are credited to your account — no extra work required

> You do **not** mine DOGE directly. If you point a rig at a DOGE-only pool, you forgo your LTC rewards. Always use a Scrypt pool that enables merge-mining.

## Best Hardware for DOGE (via LTC merge-mining)

| Miner | Hashrate | Power | Est. Daily DOGE* | Details |
|-------|----------|-------|-----------------|---------|
| Bitmain Antminer L9 | 16 GH/s | 3,360W | ~800–1,200 DOGE | [View](../miners/specs/antminer-l9.md) |
| Elphapex DG1 | 11.5 GH/s | 3,220W | ~600–900 DOGE | [View](../miners/specs/elphapex-dg1.md) |
| Bitmain Antminer L7 | 9.5 GH/s | 3,425W | ~500–750 DOGE | [View](../miners/specs/antminer-l7.md) |

*Approximate values based on current network difficulty and DOGE price. Actual amounts vary.

## Recommended Mining Pools (Scrypt + merge-mining)

| Pool | Fee | Payout | URL |
|------|-----|--------|-----|
| Litecoinpool.org | 0% | PPS (LTC + DOGE) | [litecoinpool.org](https://www.litecoinpool.org) |
| F2Pool | 2% | PPS+ | [f2pool.com](https://www.f2pool.com) |
| Antpool | 0% | PPS+ | [antpool.com](https://www.antpool.com) |

## Price History

[View full daily price history →](price-history/doge.csv)

## Is DOGE Worth Mining Right Now?

You cannot mine DOGE in isolation efficiently — its value to miners comes entirely from the merge-mining bonus on top of LTC rewards. At $0.18/DOGE, the daily DOGE bonus from an Antminer L9 adds roughly $5–$8/day on top of LTC earnings, which can represent 20–40% of total daily revenue. DOGE is highly volatile and price-driven by sentiment and social media, so treat it as a bonus rather than a primary income source. The combination of LTC + DOGE makes Scrypt mining one of the more resilient strategies in the current market.
