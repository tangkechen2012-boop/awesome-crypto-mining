# Ethereum Classic (ETC) Mining Guide

> **Algorithm:** ETHash (Etchash) | **Current Price:** ~$22 | **[Price History](price-history/etc.csv)**

## Overview

Ethereum Classic is the original Ethereum chain that preserved the unaltered transaction history after the 2016 DAO hack fork. While Ethereum itself moved to proof-of-stake in 2022, ETC has remained committed to proof-of-work, inheriting a large population of GPU miners who were displaced from ETH. Ethereum Classic uses a modified version of Ethash called "Etchash," which keeps DAG file sizes manageable and makes ETC accessible to older GPUs with 4GB+ VRAM.

## Mining Specifications

| Parameter | Value |
|-----------|-------|
| Algorithm | ETHash / Etchash |
| Block Time | ~13 seconds |
| Block Reward | 2.048 ETC (ECIP-1017 5M20 reduction schedule) |
| Network Hashrate | ~200 TH/s |
| Mining Difficulty | Adjusts every block |

## Best Hardware for ETC

ETC is primarily mined with **GPUs** — there are no widely available purpose-built ASICs for Etchash. Legacy GPUs previously used for ETH mining are ideal.

| Hardware | Hashrate | Power | Est. Daily Profit* | Notes |
|----------|----------|-------|-------------------|-------|
| NVIDIA RTX 3090 | ~130 MH/s | 290W | ~$0.40–$0.70 | Excellent VRAM for DAG |
| AMD RX 6800 XT | ~65 MH/s | 160W | ~$0.20–$0.40 | Efficient option |
| NVIDIA RTX 3080 10GB | ~100 MH/s | 220W | ~$0.30–$0.55 | Popular for farms |
| AMD RX 580 8GB | ~32 MH/s | 185W | ~$0.05–$0.15 | Budget / older hardware |

*At $0.06/kWh electricity cost. Check [live rankings](../miners/index.md) for current data.

## Recommended Mining Pools

| Pool | Fee | Payout | URL |
|------|-----|--------|-----|
| Ethermine (ETC) | 1% | PPLNS | [etc.ethermine.org](https://etc.ethermine.org) |
| F2Pool | 3% | PPS+ | [f2pool.com](https://www.f2pool.com) |
| 2Miners | 1% | PPLNS | [etc.2miners.com](https://etc.2miners.com) |
| Viabtc | 2% | PPS+ | [viabtc.com](https://www.viabtc.com) |

## Price History

[View full daily price history →](price-history/etc.csv)

## Is ETC Worth Mining Right Now?

ETC is one of the few remaining profitable options for GPU miners following Ethereum's merge to PoS. At ~$22/ETC and $0.06/kWh, high-end GPUs like the RTX 3090 can still generate a modest positive return, but margins are thin. The coin's emission schedule continues to reduce block rewards over time. ETC mining is best for operators who already own compatible GPU hardware and want to continue utilizing it. For new builds, purpose-built ASICs for other coins will typically yield better ROI than a GPU farm targeting ETC.
