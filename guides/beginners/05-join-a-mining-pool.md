# Join a Mining Pool

*Solo mining is a lottery. Pool mining is a paycheck. Here's how to get started.*

---

## What Is a Mining Pool?

A **mining pool** is a group of miners who combine their hashrate and share the rewards proportionally. Instead of each miner competing alone, they work together — and when the pool finds a block, everyone gets a cut based on their contribution.

### Why Solo Mining Is Hard for Beginners

On the Bitcoin network, a single miner with even a powerful machine has a tiny fraction of the total network hashrate. Finding a block solo could take years — or never happen at all.

**Example:** If the total Bitcoin network hashrate is 600 EH/s and your miner does 200 TH/s, your share of the network is about 0.000033%. You'd statistically find a block roughly once every 3,000 years. Not ideal.

Pool mining solves this by giving you small, frequent payments instead of rare, large ones. The total earnings over time are roughly the same — but the consistency is vastly better.

---

## How Pools Pay Out

Understanding payout methods helps you pick the right pool.

### PPS — Pay Per Share

**PPS (Pay Per Share)** pays you a fixed amount for every valid share you submit, regardless of whether the pool actually finds a block that round.

- **Pros:** Steady, predictable income — like a salary
- **Cons:** Pool charges a higher fee (usually 2–4%) to absorb the variance risk
- **Best for:** Beginners who want consistent payouts

### PPLNS — Pay Per Last N Shares

**PPLNS (Pay Per Last N Shares)** pays you based on your contribution during the shares window that led up to the last block found.

- **Pros:** Lower fees, can earn more during lucky periods
- **Cons:** Payouts are more variable; you earn nothing if the pool has a dry spell
- **Best for:** Miners who plan to stay with one pool long-term

### FPPS — Full Pay Per Share

**FPPS** is like PPS but also includes a share of transaction fees, not just the block subsidy. This is the most common method on major Bitcoin pools today.

---

## Top Mining Pools by Coin

### Bitcoin (SHA-256)

| Pool | Website | Payout Method | Fee |
|------|---------|--------------|-----|
| Braiins Pool (Slush Pool) | braiins.com | FPPS | 2% |
| Luxor Mining | luxor.tech | FPPS | 0.3% |
| F2Pool | f2pool.com | PPS+ | 2.5% |
| Foundry USA | foundrydigital.com | FPPS | 0% (US-focused) |
| AntPool | antpool.com | PPS/PPLNS | 0–2.5% |

### Litecoin / Dogecoin (Scrypt — merge-mined)

| Pool | Website |
|------|---------|
| F2Pool | f2pool.com |
| ViaBTC | viabtc.com |
| LitecoinPool | litecoinpool.org |

### Kaspa (kHeavyHash)

| Pool | Website |
|------|---------|
| Herominers | herominers.com |
| K1Pool | k1pool.com |
| Woolypooly | woolypooly.com |

### Monero (RandomX / CPU)

| Pool | Website |
|------|---------|
| SupportXMR | supportxmr.com |
| MoneroOcean | moneroocean.stream |
| MineXMR | minexmr.com |

### Alephium (Blake3)

| Pool | Website |
|------|---------|
| Herominers | herominers.com |
| Woolypooly | woolypooly.com |

---

## How to Create a Pool Account

### Step 1: Choose Your Pool

Pick a pool that supports your coin. For Bitcoin beginners, Braiins or Luxor are excellent starting points.

### Step 2: Register

Go to the pool's website and create a free account with your email address. Most pools don't require identity verification.

### Step 3: Create a Worker

In your pool dashboard, add a **worker**. A worker is just a label for each mining machine you connect. Name it something descriptive like `home_s21_01`.

### Step 4: Get Your Pool Stratum URL

The pool's documentation (usually under "Getting Started" or "Help") will list a stratum address. It looks like:

```
stratum+tcp://stratum.braiins.com:3333
```

Copy this — you'll enter it into your miner's configuration page (as covered in the [previous guide](04-setup-and-configuration.md)).

### Step 5: Set Your Payout Address

This is the most important step. The **payout address** is your personal cryptocurrency wallet address — where the pool sends your earnings.

- If you don't have a wallet yet, create one first (hardware wallets like Ledger or software wallets like Electrum for Bitcoin work well)
- In the pool dashboard, find "Payout Settings" and enter your wallet address
- Double-check the address — cryptocurrency transactions cannot be reversed

---

## What Is a Payout Address?

A **payout address** is like a bank account number for cryptocurrency. It's a string of letters and numbers that uniquely identifies your wallet.

A Bitcoin address looks like this:
```
bc1qxy2kgdygjrsqtzq2n0yrf2493p83kkfjhx0wlh
```

**Never share your private key** — that's the password to your wallet. Only share your public address when receiving payments.

---

## Reading Your Pool Dashboard

Once your miner connects, your pool dashboard will show live data. Here's what to look for:

| Metric | What It Means |
|--------|--------------|
| **Workers Online** | Number of miners currently connected |
| **Hashrate (Current)** | Your real-time hashrate as seen by the pool |
| **Hashrate (Average)** | Smoothed over the last hour/day — more reliable |
| **Accepted Shares** | Valid work submitted and counted |
| **Rejected Shares** | Work that didn't count — keep this below 1–2% |
| **Estimated Daily Earnings** | Approximate daily reward at your hashrate |
| **Unpaid Balance** | Earnings not yet sent to your wallet |
| **Minimum Payout** | Pool won't send until you reach this threshold |

Most pools have a **minimum payout threshold** — for example, 0.001 BTC. If you're running a small miner, it might take a few days or weeks to reach the threshold before you receive your first payment.

---

## Common Beginner Mistakes to Avoid

- **Wrong pool URL** — One typo and your miner connects to nothing. Copy the URL directly from the pool website.
- **Wrong coin's wallet address** — Sending Bitcoin earnings to an Ethereum address means losing them forever. Match the coin.
- **Forgetting to set a payout address** — Your pool dashboard may hold earnings until you add a wallet address.
- **Ignoring the pool fee** — A 3% fee on $200/month is $6. It matters over time. Read the fee structure.
- **Switching pools constantly** — PPLNS pools reward loyalty to the pool window. Switching frequently hurts your short-term earnings.

---

## You're Ready to Mine

You now have everything you need to start mining:

- You understand how mining works and why it exists
- You've chosen an algorithm and coin that fit your goals
- You've selected hardware within your budget and calculated ROI
- Your miner is physically set up, connected, and configured
- You've joined a pool and set your payout address

The rest is patience. Mining is a long game — daily earnings are small, but they compound over months. Check your dashboard regularly, keep an eye on temperature and fan health, and revisit your profitability numbers when coin prices shift significantly.

---

## Learn More

- [Back to the Main README](../../README.md)
- [Algorithm Details](../../algorithms/)
- [Miner Specifications](../../miners/)
- [Guide 1: How Mining Works](01-how-mining-works.md)
- [Guide 2: Choose Your Algorithm & Coin](02-choose-your-algorithm-and-coin.md)
- [Guide 3: Pick Your First Miner](03-pick-your-first-miner-under-3000.md)
- [Guide 4: Setup & Configuration](04-setup-and-configuration.md)
