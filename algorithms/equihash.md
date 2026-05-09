# Equihash

> **Used by:** Zcash (ZEC) | **ASIC Resistance:** Low (was High) | **Best Hardware:** ASIC miners

## What Is Equihash?

Equihash is a memory-hard proof-of-work algorithm based on the Generalized Birthday Problem — a mathematical puzzle that asks: given a large set of random strings, find a subset that XORs to zero. The algorithm was designed by Alex Biryukov and Dmitry Khovratovich and chosen by the Zcash team for its launch in 2016.

The Birthday Problem approach is elegant: finding a valid solution requires storing and searching through hundreds of megabytes of intermediate values. Early Equihash parameters (200,9) meant that efficient mining required roughly 700 MB of RAM per thread — far more than SHA-256 or Scrypt, and at the time genuinely difficult to implement in silicon at a competitive cost.

Equihash's parameters (n, k) control the memory-time tradeoff. Zcash uses n=200, k=9. The puzzle generates 2^(n/(k+1)) initial strings and requires finding k+1 = 10 of them that XOR to zero at each level of a binary tree — a process that cannot easily be shortcut.

Despite the original promise, Equihash ASICs arrived in 2018 (notably from Bitmain with the Antminer Z9). Zcash chose not to fork away from ASICs, reasoning that ASIC miners provide more stable, long-term security than GPU miners who might easily redirect hashrate elsewhere.

## Coins That Use Equihash

| Coin | Ticker | Details |
|------|--------|---------|
| Zcash | ZEC | [View coin page](../coins/zcash.md) |
| Horizen | ZEN | — |
| Komodo | KMD | — |

## Best Mining Hardware

| Miner | Hashrate | Power | Daily Profit* | Details |
|-------|----------|-------|--------------|---------|
| Antminer Z15 Pro | 840 KSol/s | 2,650W | ~$2.10 | [View](../miners/specs/antminer-z15-pro.md) |
| Antminer Z15 | 420 KSol/s | 1,510W | ~$1.00 | — |

*At $0.06/kWh. Updated periodically.

## ASIC Resistance

Equihash was considered highly ASIC-resistant at launch, but that reputation ended in 2018. Purpose-built Equihash ASICs are now the only cost-effective way to mine ZEC. GPU mining Equihash is unprofitable at virtually any electricity price.

Some Equihash variants (144,5 used by BitcoinGold; 192,7 used by ZelHash) were developed specifically to restore GPU mining after ASICs arrived — each new parameter set temporarily breaks existing ASICs until new ones are engineered. Zcash itself stayed on the original 200,9 parameters.

## Recommended Mining Pools

- [2Miners](https://2miners.com/zec-mining-pool) — 1% fee, PPLNS
- [F2Pool](https://www.f2pool.com/) — 3% fee, PPS+
- [ViaBTC](https://www.viabtc.com/) — 2% fee, PPS/PPLNS
- [Flypool](https://zcash.flypool.org/) — 1% fee, PPLNS
