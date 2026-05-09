# How Cryptocurrency Mining Works

*A plain-English guide for complete beginners.*

---

## What Is Cryptocurrency Mining?

**Cryptocurrency mining** is the process of using computers to validate transactions on a blockchain network — and earning newly created coins as a reward for doing so.

Think of it like this: every time someone sends Bitcoin, that transaction needs to be verified and recorded permanently. Mining is the engine that makes that happen. Without miners, the network would grind to a halt.

---

## Why Does Mining Exist?

Blockchains like Bitcoin have no central authority — no bank, no company, no government. So how does everyone agree on what transactions are valid?

The answer is **proof of work**. Miners compete to solve a mathematical puzzle. The winner gets to add the next block of transactions to the blockchain and collects a reward. This competition keeps the network honest: cheating would require more computing power than all honest miners combined — which is practically impossible.

---

## Proof of Work, Explained Simply

Imagine the network gives everyone a dice-rolling challenge: "Roll a number below 10,000." Anyone can roll. Anyone can check your result instantly. But there's no shortcut to getting a low number — you just have to keep rolling.

That's essentially what miners do, except with cryptographic math instead of dice. The "roll" is called a **hash**. Miners produce billions of hashes per second until one of them meets the network's target. The first miner to find it broadcasts the result, everyone verifies it, and the block is added.

---

## What Miners Actually Do (Hashing)

A **hash** is a fixed-length string of letters and numbers generated from an input. Change even one character of the input and the hash changes completely.

Miners take a block of pending transactions, add a random number called a **nonce**, and run it through a hash function. If the result starts with enough zeros, they've found a valid block. If not, they change the nonce and try again — billions of times per second.

**Hashrate** is how we measure this speed. It's usually expressed in:
- **TH/s** (terahashes per second) — common for Bitcoin miners
- **MH/s** or **GH/s** — used for altcoin miners

A higher hashrate means more "guesses" per second, which means a higher chance of winning the block reward.

---

## Why Electricity Matters So Much

All that hashing requires real computing power, and computing power requires electricity. Electricity is the single biggest ongoing cost for any miner.

- A modern Bitcoin ASIC miner might consume **3,000–5,000 watts** — like running 30–50 light bulbs continuously.
- At $0.10/kWh (a common residential rate), that's roughly **$7–12 per day** just in electricity.
- At $0.05/kWh (cheap industrial power), the same miner costs half as much to run, making it far more profitable.

**Your electricity rate determines whether you profit or lose money.** This is the most important variable in mining economics.

---

## Three Types of Mining Hardware

### ASIC Miners (Application-Specific Integrated Circuits)

**ASICs** are purpose-built chips designed to do one thing: compute a specific hash algorithm as fast and efficiently as possible. They dominate Bitcoin mining.

- Pros: Extremely fast and energy-efficient for their target algorithm
- Cons: Expensive, can only mine one algorithm, useless if the coin changes

### GPU Miners (Graphics Processing Units)

**GPUs** — the same cards used in gaming PCs — are flexible enough to mine many different algorithms. They were once the standard for Ethereum mining.

- Pros: Can switch between coins, resellable, multi-purpose
- Cons: Lower efficiency than ASICs for algorithms that have ASICs

### CPU Miners (Central Processing Units)

**CPUs** are the main processors in regular computers. A handful of coins (notably Monero) are intentionally designed to resist ASICs and favor CPU mining.

- Pros: Everyone already has one, very low barrier to entry
- Cons: Much lower hashrate and earnings compared to ASICs or GPUs

For most beginners today, **ASIC miners** are the practical starting point for serious income.

---

## The Big Picture

Here's the mining cycle in brief:

1. Transactions are broadcast to the network
2. Miners bundle them into a candidate block
3. Miners race to find a valid hash
4. The winner broadcasts the solution; everyone verifies it
5. The block is added to the blockchain
6. The winning miner receives the **block reward** (new coins + transaction fees)
7. The cycle repeats every ~10 minutes (Bitcoin) or faster for other coins

Every block that gets added makes the entire chain more secure — and mining is what makes that happen.

---

## Key Terms Recap

| Term | Plain English |
|------|--------------|
| Blockchain | A permanent, public record of all transactions |
| Proof of Work | A competition to solve math puzzles that secures the network |
| Hash | A fingerprint generated from data |
| Nonce | A random number miners change to get a different hash |
| Hashrate | Speed at which a miner produces hashes |
| Block reward | Coins paid to the miner who finds a valid block |
| ASIC | A chip built specifically for mining one algorithm |

---

**Next Step → [Choose Your Algorithm & Coin](02-choose-your-algorithm-and-coin.md)**
