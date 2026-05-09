# Blake3

> **Used by:** Alephium (ALPH) | **ASIC Resistance:** Low | **Best Hardware:** ASIC miners

## What Is Blake3?

Blake3 is a cryptographic hash function released in 2020 by Jack O'Connor, Jean-Philippe Aumasson, Samuel Neves, and Zooko Wilcox-O'Hearn. It is one of the fastest general-purpose cryptographic hash functions available, achieving throughput on modern CPUs that dramatically outpaces SHA-256, SHA-3, and even earlier Blake variants (Blake2b, Blake2s). Blake3 achieves this through a tree-based Merkle structure that allows unlimited parallelism — each chunk of input data can be hashed independently and then combined.

Alephium selected Blake3 as the foundation of its mining algorithm for a specific reason: BlockFlow. Alephium's BlockFlow is a sharded DAG architecture where transactions are processed across 16 parallel groups, each with its own chain. Mining in this system requires simultaneously hashing multiple block candidates across different chains — a workload that benefits enormously from Blake3's native parallelism and raw throughput.

Alephium's mining algorithm (sometimes called "Stratum" in pool documentation) wraps Blake3 with additional domain separation per chain, ensuring that hashrate dedicated to one chain's blocks cannot be trivially redirected to another. The result is a fast, verifiable proof-of-work that scales with Alephium's multi-chain structure.

Because Blake3 is computationally simple and extremely fast, it maps well to ASIC implementation. Purpose-built hardware quickly achieved dominance over GPU mining once it became available.

## Coins That Use Blake3

| Coin | Ticker | Details |
|------|--------|---------|
| Alephium | ALPH | [View coin page](../coins/alephium.md) |

## Best Mining Hardware

| Miner | Hashrate | Power | Daily Profit* | Details |
|-------|----------|-------|--------------|---------|
| Goldshell AL-BOX | 12 TH/s | 2,900W | ~$1.10 | [View](../miners/specs/goldshell-al-box.md) |
| Goldshell AL-BOX II | 15 TH/s | 3,100W | ~$1.40 | — |

*At $0.06/kWh. ALPH is a smaller-cap coin — verify current prices and liquidity before purchasing hardware. Updated periodically.

## ASIC Resistance

Blake3 was not designed to resist ASICs, and neither was Alephium's use of it. The algorithm's simplicity and speed, while ideal for Alephium's architecture, also make it straightforward to implement in custom silicon. Goldshell released dedicated Alephium miners in 2023, and GPU mining ALPH has been unprofitable since shortly after these machines became available.

For miners evaluating ALPH, the key risks are not hardware-related but market-related: ALPH is a smaller-cap asset with lower daily trading volume than BTC, LTC, or KAS. Hardware ROI depends heavily on ALPH price holding up through the payback period. Ensure you can liquidate mined coins before committing capital.

## Recommended Mining Pools

- [Alephium Herominers](https://alephium.herominers.com/) — 1% fee, PPLNS
- [Woolypooly](https://woolypooly.com/) — 1% fee, PPS
- [2Miners](https://2miners.com/) — 1% fee, PPLNS
- [Alph.land](https://alph.land/) — community pool, variable fee
