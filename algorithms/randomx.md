# RandomX

> **Used by:** Monero (XMR) | **ASIC Resistance:** High | **Best Hardware:** CPUs (AMD Ryzen, EPYC)

## What Is RandomX?

RandomX is a proof-of-work algorithm designed specifically to be efficient on general-purpose CPUs while being difficult and expensive to implement on ASICs or GPUs. It was developed by a team of Monero contributors (tevador, hyc, vielmetti, antanst, and SChernykh) and activated on the Monero network in November 2019.

The key innovation is randomized execution. RandomX generates a random program — a sequence of arithmetic, logical, floating-point, and memory access instructions — and executes it on a virtual machine. Because the program changes with every block header hash attempt, an ASIC would need to implement a full general-purpose CPU just to execute it efficiently. There is no shortcut.

Specifically, RandomX uses:
- A 2 GB dataset (the "full" mode dataset) that must be loaded into RAM to mine at full speed
- A virtual machine with 8 integer registers, 8 floating-point registers, and 256-byte scratchpad
- Randomly generated programs of 256 instructions per hash
- AES-based fast mixing to fill the dataset

The 2 GB dataset requirement means that mining nodes need at least 2–3 GB of RAM per mining thread in full mode. This is within reach of consumer CPUs but extremely expensive to replicate on ASIC silicon at competitive scale.

## Coins That Use RandomX

| Coin | Ticker | Details |
|------|--------|---------|
| Monero | XMR | [View coin page](../coins/monero.md) |
| Wownero | WOW | — |

## Best Mining Hardware

| Miner | Hashrate | Power | Daily Profit* | Details |
|-------|----------|-------|--------------|---------|
| AMD EPYC 9654 (96-core) | ~60,000 H/s | ~360W | ~$1.20 | — |
| AMD Ryzen 9 7950X | ~23,000 H/s | ~170W | ~$0.45 | — |
| Intel Xeon w9-3595X | ~18,000 H/s | ~350W | ~$0.20 | — |

*At $0.06/kWh. CPU mining profitability is modest — most miners use idle or already-running hardware. Updated periodically.

## ASIC Resistance

RandomX achieves the highest level of practical ASIC resistance of any major mining algorithm. No commercially viable RandomX ASIC has been produced. The reason: the algorithm's random instruction set makes the program-execution path unpredictable, and the 2 GB dataset creates a memory bottleneck that standard DRAM is already well-suited to handle. An ASIC would essentially need to be a full CPU — at which point you have just built a more expensive CPU.

Monero has also historically been willing to change its proof-of-work algorithm to break ASIC mining when it appears. Before RandomX, Monero used CryptoNight and cycled through variants (v7, v8, Turtle, etc.) to break successive waves of ASICs. RandomX was intended to be a long-term solution that makes this arms race unnecessary.

GPUs do mine RandomX but perform poorly compared to CPUs on a per-watt basis, making CPU mining unusually competitive for a major coin.

## Recommended Mining Pools

- [SupportXMR](https://supportxmr.com/) — 0.6% fee, PPLNS
- [MoneroOcean](https://moneroocean.stream/) — 0% fee (takes algorithm switching revenue), PPLNS
- [2Miners](https://2miners.com/xmr-mining-pool) — 1% fee, PPLNS
- [MineXMR](https://minexmr.com/) — 1% fee, PPLNS (note: has had high share of hashrate — consider smaller pools for decentralization)
