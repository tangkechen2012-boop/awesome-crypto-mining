# Ethash

> **Used by:** Ethereum Classic (ETC) | **ASIC Resistance:** Low | **Best Hardware:** Legacy GPUs, ASIC miners

## What Is Ethash?

Ethash was the proof-of-work algorithm used by Ethereum from its 2015 launch until The Merge in September 2022, when Ethereum switched to proof-of-stake. It was designed by Vitalik Buterin and other Ethereum contributors with GPU miners in mind — the goal was to reward decentralized participation while keeping the barrier low enough that ordinary people with gaming GPUs could participate.

The algorithm's central feature is a large dataset called the DAG (Directed Acyclic Graph). Mining a block requires reading pseudorandom locations from this DAG in sequence — an operation that is bottlenecked by memory bandwidth rather than raw computation. The DAG grows by roughly 8 GB every two to three years (every 30,000 blocks, called an "epoch"), which was originally intended to prevent memory-limited ASICs from being viable.

For each hash attempt, the miner:
1. Computes a seed hash from the block number
2. Derives a 16 MB pseudocache from the seed
3. Generates the full DAG (~4 GB initially, growing over time) from the cache
4. Performs 64 random lookups into the DAG to produce the final hash

The DAG must fit in VRAM for efficient GPU mining. As it grew past 4 GB, older GPUs with 4 GB or less VRAM became unable to mine Ethash — a significant event that retired much of the early GPU mining fleet.

After The Merge, Ethash mining effectively moved entirely to Ethereum Classic, which chose to continue proof-of-work. ETC remains the largest Ethash chain by far.

## Coins That Use Ethash

| Coin | Ticker | Details |
|------|--------|---------|
| Ethereum Classic | ETC | [View coin page](../coins/ethereum-classic.md) |
| Ethash Testnets | — | Various test networks |

## Best Mining Hardware

| Miner | Hashrate | Power | Daily Profit* | Details |
|-------|----------|-------|--------------|---------|
| Antminer E9 Pro | 3,680 MH/s | 2,200W | ~$1.80 | — |
| iPollo V1 Mini | 300 MH/s | 240W | ~$0.15 | — |
| NVIDIA RTX 4090 | ~130 MH/s | ~340W | ~$0.04 | — |

*At $0.06/kWh. ETC profitability is modest — verify current prices. Updated periodically.

## ASIC Resistance

Ethash was moderately ASIC-resistant for its first few years. Bitmain launched the first Ethash ASIC (Antminer E3) in 2018, but it was quickly obsoleted by the growing DAG exceeding its onboard memory. Since then, ASICs with larger memory have arrived and dominate the ETC network.

GPU mining ETC remains possible and is a common use case for GPU rigs originally purchased for Ethereum mining. However, ASICs are significantly more efficient per hash, so GPU miners are at a disadvantage on electricity cost unless they have very cheap power.

The current DAG size for ETC is approximately 22 GB (as of 2025–2026). Any GPU with less VRAM cannot mine ETC at all.

## Recommended Mining Pools

- [2Miners](https://2miners.com/etc-mining-pool) — 1% fee, PPLNS
- [F2Pool](https://www.f2pool.com/) — 2.5% fee, PPS+
- [Herominers](https://etc.herominers.com/) — 1% fee, PPLNS
- [Ethermine (ETC)](https://etc.ethermine.org/) — 1% fee, PPLNS
