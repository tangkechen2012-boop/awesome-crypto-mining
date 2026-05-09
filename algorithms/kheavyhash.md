# kHeavyHash

> **Used by:** Kaspa (KAS) | **ASIC Resistance:** Low | **Best Hardware:** ASIC miners

## What Is kHeavyHash?

kHeavyHash is a proof-of-work algorithm created specifically for Kaspa, a cryptocurrency built on a blockDAG (Directed Acyclic Graph) structure rather than a traditional blockchain. Kaspa was designed to achieve extremely fast block times — initially 1 block per second, later upgraded to 10 blocks per second and targeting 100 — while still using proof-of-work for security.

The algorithm works in three stages. First, a standard SHA-3 (Keccak) hash is computed on the block header. Second, the result is fed into a matrix-vector multiplication step using 64×64 matrices of 16-bit integers. Third, another Keccak hash is applied to the result. The matrix multiplication step is what makes it "heavy" — it requires more computation than a simple hash but does so in a way that maps well to both GPU and ASIC silicon.

kHeavyHash was engineered with Kaspa's blockDAG in mind. Because Kaspa produces blocks at extremely high frequency, the mining algorithm needs to be fast enough that miners can receive, verify, and build on new blocks before the network moves on — a constraint that ruled out memory-hard designs that add latency.

## Coins That Use kHeavyHash

| Coin | Ticker | Details |
|------|--------|---------|
| Kaspa | KAS | [View coin page](../coins/kaspa.md) |

## Best Mining Hardware

| Miner | Hashrate | Power | Daily Profit* | Details |
|-------|----------|-------|--------------|---------|
| IceRiver KS5 Pro | 21.5 TH/s | 3,500W | ~$4.80 | [View](../miners/specs/iceriver-ks5-pro.md) |
| Antminer KS5 Pro | 21 TH/s | 3,150W | ~$4.90 | [View](../miners/specs/antminer-ks5-pro.md) |
| IceRiver KS3 | 8 TH/s | 3,200W | ~$1.50 | — |

*At $0.06/kWh. Updated periodically. KAS is volatile — verify current prices.

## ASIC Resistance

kHeavyHash was not designed to resist ASICs. The algorithm's matrix-multiplication step can be efficiently implemented in custom silicon, and the first KAS ASICs arrived in 2023, rapidly obsoleting GPU mining. GPU hashrates of a few hundred MH/s are completely outclassed by ASIC units delivering 8–21 TH/s.

If you purchased GPU rigs for KAS mining in 2022, they are no longer competitive. The transition from GPU to ASIC dominance happened faster for KAS than for most coins, partly because the simple, deterministic structure of kHeavyHash made ASIC design relatively straightforward.

## Recommended Mining Pools

- [K1Pool](https://k1pool.com/) — 1% fee, PPS+
- [Herominers](https://kaspa.herominers.com/) — 1% fee, PPLNS
- [2Miners](https://2miners.com/kas-mining-pool) — 1% fee, PPLNS
- [Woolypooly](https://woolypooly.com/) — 1% fee, PPS
