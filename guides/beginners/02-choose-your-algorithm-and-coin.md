# Choose Your Algorithm & Coin

*Once you understand how mining works, the next question is: what should you mine?*

---

## Why the Algorithm Matters

Every mineable cryptocurrency uses a specific **mining algorithm** — a set of mathematical rules that determines what kind of hardware can mine it efficiently.

Choosing an algorithm is not just picking a coin. It's choosing an entire hardware ecosystem, a competitive landscape, and a risk profile. The algorithm you pick determines what machine you buy, how much you spend, and how you compete with other miners.

---

## The 7 Main Mining Algorithms

### 1. SHA-256
**SHA-256** (Secure Hash Algorithm 256-bit) is the oldest and most battle-tested mining algorithm. It powers Bitcoin, the most valuable cryptocurrency by market cap.

- **Main coins:** Bitcoin (BTC), Bitcoin Cash (BCH), Bitcoin SV (BSV)
- **Hardware:** ASIC-only — the most competitive mining market in the world
- **Difficulty:** Very high. You need serious hardware to earn meaningfully.

### 2. Scrypt
**Scrypt** was designed to be memory-intensive and initially more ASIC-resistant than SHA-256. ASICs now exist for it, but they're less dominant than in Bitcoin.

- **Main coins:** Litecoin (LTC), Dogecoin (DOGE)
- **Hardware:** ASIC miners
- **Note:** LTC and DOGE are often **merge-mined** together — you mine both at once for free.

### 3. Equihash
**Equihash** is a memory-hard algorithm used by privacy-focused and older GPU-friendly coins. ASICs exist but the ecosystem is smaller.

- **Main coins:** Zcash (ZEC), Flux (FLUX), Komodo (KMD)
- **Hardware:** ASIC miners (Bitmain Antminer Z series)

### 4. kHeavyHash
**kHeavyHash** is the algorithm behind Kaspa (KAS), one of the fastest-growing newer mining coins. It was specifically designed to be ASIC-friendly but open to new entrants.

- **Main coins:** Kaspa (KAS)
- **Hardware:** ASIC miners (IceRiver KS series, Bitmain KA series)
- **Note:** Kaspa has high growth potential but also higher volatility.

### 5. RandomX
**RandomX** is CPU-optimized on purpose. It uses random code execution and memory-hardness to give standard processors a fair shot against specialized hardware.

- **Main coins:** Monero (XMR)
- **Hardware:** CPUs (regular computer processors) — no ASIC needed
- **Note:** Great for privacy enthusiasts; lower upfront cost, lower returns.

### 6. ETHash / ETHashPOW
**ETHash** was Ethereum's original algorithm. Since Ethereum moved to proof of stake in 2022, some forked coins still use it.

- **Main coins:** Ethereum Classic (ETC), ETHW
- **Hardware:** GPUs (Nvidia and AMD cards)
- **Note:** The GPU mining market shrank significantly after Ethereum's merge.

### 7. Blake3
**Blake3** (and its variants like Blake3d) is used by newer proof-of-work coins that emphasize speed and efficiency.

- **Main coins:** Alephium (ALPH), some smaller coins
- **Hardware:** ASIC miners (Goldshell AL series) and some GPU support

---

## Algorithm Comparison Table

| Algorithm | Main Coin | Hardware | Difficulty | Stability | Growth Potential |
|-----------|-----------|----------|------------|-----------|-----------------|
| SHA-256 | Bitcoin (BTC) | ASIC | Very High | Very High | Moderate |
| Scrypt | Litecoin / Dogecoin | ASIC | High | High | Moderate |
| Equihash | Zcash (ZEC) | ASIC | Medium | Medium | Low–Medium |
| kHeavyHash | Kaspa (KAS) | ASIC | Medium | Medium | High |
| RandomX | Monero (XMR) | CPU | Low | High | Low–Medium |
| ETHash | Ethereum Classic | GPU | Medium | Medium | Low |
| Blake3 | Alephium (ALPH) | ASIC/GPU | Low | Low | Medium–High |

*Difficulty, stability, and growth potential are approximate and change with market conditions.*

---

## How to Think About Choosing

### Stability vs. Growth Potential

**Stable coins** (Bitcoin, Litecoin) have large markets, established infrastructure, and predictable (if competitive) returns. The hardware is more expensive upfront, but there's less risk of the coin becoming worthless.

**Growth-potential coins** (Kaspa, Alephium) are newer, less competitive, and may offer better short-term returns — but they're also more volatile. A coin that pays well today could be worth far less in six months.

A common beginner strategy: start with a well-established coin to learn the ropes, then diversify once you're comfortable.

### Electricity Cost

This cannot be overstated. A coin that looks profitable at $0.05/kWh may be a money-loser at $0.12/kWh. Always calculate profitability using **your actual electricity rate** before buying any hardware.

Free tools like [WhatToMine](https://whattomine.com) let you plug in your electricity cost and hardware specs to see estimated daily profit.

### Hardware Availability

Some algorithms have a wide range of miner options at different price points. Others (like SHA-256) have hardware that costs thousands of dollars per unit. Check what's available and at what price before committing to an algorithm.

---

## Where to Learn More

Detailed algorithm pages are available in the [`../../algorithms/`](../../algorithms/) directory of this repository. Each page covers the technical details, top hardware options, and current profitability benchmarks.

---

## Quick Decision Framework

1. **Low budget (under $500)?** → CPU mining (Monero/RandomX) or small GPU rig
2. **Mid budget ($500–$2,000)?** → Kaspa, Alephium, or Scrypt ASIC
3. **Larger budget ($2,000+)?** → Bitcoin SHA-256 ASIC or Litecoin/DOGE Scrypt ASIC
4. **Privacy matters most?** → Monero (RandomX, CPU)
5. **Want the most established option?** → Bitcoin (SHA-256, ASIC)

---

**Next Step → [Pick Your First Miner](03-pick-your-first-miner-under-3000.md)**
