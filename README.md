# ⛏️ Awesome Crypto Mining

> Daily-updated data, beginner guides, and a community marketplace for cryptocurrency miners worldwide.

![Updated Daily](https://img.shields.io/badge/updated-daily-brightgreen)
![Miners Tracked](https://img.shields.io/badge/miners%20tracked-284-blue)
![License](https://img.shields.io/badge/license-MIT-green)

A neutral, community-focused resource for anyone mining cryptocurrency — from first-time hobbyists to multi-rig operators. Get fresh profitability data, fair miner prices, coin market info, and plain-English guides, all in one place.

---

## 🗺️ New to Mining? Start Here

Follow these five steps in order and you'll go from zero to hashing:

1. [How Mining Works](guides/beginners/01-how-mining-works.md) — proof-of-work explained without the jargon
2. [Choosing Your First Miner](guides/beginners/02-choosing-your-first-miner.md) — ASIC vs GPU, budget vs performance
3. [Setting Up Your Miner](guides/beginners/03-setting-up-your-miner.md) — hardware, network, and firmware basics
4. [Calculating Profitability](guides/beginners/04-calculating-profitability.md) — electricity cost, difficulty, and break-even math
5. [Join a Mining Pool](guides/beginners/05-join-a-mining-pool.md) — why solo mining rarely pays and how to pick a pool

---

## 📊 Today's Most Profitable Miners

<!-- AUTO-UPDATED BY GITHUB ACTIONS -->

| Miner | Algorithm | Hashrate | Power | Daily Profit (est.) | Buy New |
|-------|-----------|----------|-------|---------------------|---------|
| Antminer S21 XP | SHA-256 | 270 TH/s | 3,610 W | $14.20 | [bt-miners.com](https://bt-miners.com) |
| IceRiver KS3 | KHeavyHash | 8 TH/s | 3,200 W | $11.80 | [bt-miners.com](https://bt-miners.com) |
| Antminer L9 | Scrypt | 16 GH/s | 3,260 W | $6.40 | [bt-miners.com](https://bt-miners.com) |

> Profitability estimates assume $0.07/kWh electricity. See [`data/profitability/`](data/profitability/) for full CSVs updated daily.

---

## 💰 Coin Prices Today

<!-- AUTO-UPDATED BY GITHUB ACTIONS -->

| Coin | Symbol | Price (USD) | 24h Change | Algorithm |
|------|--------|-------------|------------|-----------|
| Bitcoin | BTC | $62,400 | +1.2% | SHA-256 |
| Kaspa | KAS | $0.1840 | -0.8% | KHeavyHash |
| Litecoin | LTC | $84.20 | +0.5% | Scrypt |
| Zcash | ZEC | $28.60 | +2.1% | Equihash |

> See [`data/coin-prices/`](data/coin-prices/) for full price history CSVs.

---

## ♻️ Used Miner Marketplace

Looking to buy or sell second-hand mining hardware? Our community marketplace connects buyers and sellers with an AI-assisted middleman to keep deals fair and scam-free.

**How to list or inquire:**

| Channel | Contact |
|---------|---------|
| Telegram | [@MiningDealBot](https://t.me/MiningDealBot) |
| Web | [bt-miners.com/marketplace](https://bt-miners.com/marketplace) |
| Email | [deals@bt-miners.com](mailto:deals@bt-miners.com) |

Browse current listings: [`marketplace/listings.md`](marketplace/listings.md)

> Your contact information is never published. The team responds within 24 hours.

---

## 📚 Repository Contents

```
awesome-crypto-mining/
├── guides/
│   ├── beginners/          # Five-step intro series for new miners
│   └── advanced/           # Overclocking, firmware, multi-pool strategies
├── miners/                 # Per-model spec sheets and profitability history
├── coins/                  # Per-coin mining guides and algorithm explainers
├── algorithms/             # Deep dives: SHA-256, KHeavyHash, Scrypt, Equihash, etc.
├── data/
│   ├── profitability/      # Daily profit CSVs per miner (auto-updated)
│   ├── miner-prices/       # New and used price history CSVs
│   └── coin-prices/        # Daily coin price CSVs
├── marketplace/
│   └── listings.md         # Current used miner listings
└── scripts/                # GitHub Actions scripts that refresh data daily
```

---

## 🤖 AI Mining Assistant

This repository is structured so that AI assistants can answer natural-language mining questions directly from the data and guides here. If you are using an AI tool (Claude Code, ChatGPT, etc.), you can ask questions like:

- "Which miner is most profitable for Kaspa right now?"
- "What is the break-even time for an Antminer S21 XP at $0.08/kWh?"
- "Show me Litecoin mining profitability over the last 30 days."

Reach the team through the same three channels listed in the marketplace section above — Telegram, web, or email.

---

## 🤝 Contributing

We welcome contributions from the mining community. See [CONTRIBUTING.md](CONTRIBUTING.md) for full details on:

- Submitting used miner listings
- Reporting data errors
- Writing guides
- CSV data format specs

Pull requests are welcome. Please open an issue first for large changes so we can discuss the approach.

---

## 📄 License

MIT — see [LICENSE](LICENSE) for details. Data and guides may be freely used and redistributed with attribution.
