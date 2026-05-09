# Scrypt

> **Used by:** Litecoin (LTC), Dogecoin (DOGE) | **ASIC Resistance:** Low | **Best Hardware:** ASIC miners

## What Is Scrypt?

Scrypt is a memory-hard password-based key derivation function created by Colin Percival in 2009, originally designed to make brute-force attacks expensive by requiring large amounts of RAM alongside computation. Litecoin adopted it in 2011 precisely because Bitcoin's SHA-256 was already being dominated by FPGAs, and Scrypt's memory requirements were expected to keep mining accessible to ordinary computers for longer.

The core idea: before hashing, scrypt fills a large block of memory with pseudorandom data, then reads from it in a pattern that depends on prior outputs. An attacker (or ASIC) cannot bypass this without providing the memory — raw compute speed alone is not enough.

In practice, Scrypt's ASIC resistance proved temporary. By 2014, dedicated Scrypt ASICs had arrived, and today the LTC and DOGE networks are entirely dominated by purpose-built hardware. Dogecoin merge-mines with Litecoin, meaning miners earn both coins simultaneously with the same hardware and no extra energy cost — a major advantage that has made DOGE one of the most profitably merge-mined coins.

## Coins That Use Scrypt

| Coin | Ticker | Details |
|------|--------|---------|
| Litecoin | LTC | [View coin page](../coins/litecoin.md) |
| Dogecoin | DOGE | [View coin page](../coins/dogecoin.md) |
| Viacoin | VIA | — |

## Best Mining Hardware

| Miner | Hashrate | Power | Daily Profit* | Details |
|-------|----------|-------|--------------|---------|
| Antminer L9 | 16 GH/s | 3,360W | ~$4.20 | [View](../miners/specs/antminer-l9.md) |
| Elphapex DG1 | 11 GH/s | 3,000W | ~$2.80 | [View](../miners/specs/elphapex-dg1.md) |
| Antminer L7 | 9.5 GH/s | 3,425W | ~$2.10 | — |

*At $0.06/kWh. LTC+DOGE merge-mine earnings combined. Updated periodically.

## ASIC Resistance

Scrypt was designed to resist ASICs through memory hardness, but this resistance collapsed within a few years of Litecoin's launch. Modern Scrypt ASICs implement on-chip SRAM at a scale that makes memory access nearly free. If you are considering GPU mining Scrypt, stop — GPUs cannot compete with current-generation ASICs on any profitability metric.

The merge-mining relationship between LTC and DOGE is the more interesting dynamic today: miners effectively get DOGE rewards for free, which substantially improves total profitability.

## Recommended Mining Pools

- [LitecoinPool](https://www.litecoinpool.org/) — 0% fee, PPS
- [F2Pool](https://www.f2pool.com/) — 1% fee, PPS+, supports merge mining
- [ViaBTC](https://www.viabtc.com/) — 2% fee, PPS/PPLNS, supports merge mining
- [AntPool](https://www.antpool.com/) — 1.5% fee, PPLNS
