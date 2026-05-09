# ⛏️ Awesome Crypto Mining

> Daily-updated data, beginner guides, and a community marketplace for cryptocurrency miners worldwide.

![Updated Daily](https://img.shields.io/badge/updated-daily-brightgreen)
![Miners Tracked](https://img.shields.io/badge/miners%20tracked-287-blue)
![Profitable Miners](https://img.shields.io/badge/profitable%20miners-102-orange)
![License](https://img.shields.io/badge/license-MIT-green)

A neutral, community-focused resource for anyone mining cryptocurrency — from first-time hobbyists to multi-rig operators. Get fresh profitability data, fair miner prices, coin market info, and plain-English guides, all in one place.

---

## 🗺️ New to Mining? Start Here

Follow these five steps in order and you'll go from zero to hashing:

1. [How Mining Works](guides/beginners/01-how-mining-works.md) — proof-of-work explained without the jargon
2. [Choose Your Algorithm & Coin](guides/beginners/02-choose-your-algorithm-and-coin.md) — SHA-256, Scrypt, Equihash, and more
3. [Pick Your First Miner (Under $3,000)](guides/beginners/03-pick-your-first-miner-under-3000.md) — budget-friendly picks with real ROI math
4. [Setup & Configuration](guides/beginners/04-setup-and-configuration.md) — hardware, network, and firmware basics
5. [Join a Mining Pool](guides/beginners/05-join-a-mining-pool.md) — why solo mining rarely pays and how to pick a pool

---

## 📊 Today's Most Profitable Miners

<!-- AUTO-UPDATED BY GITHUB ACTIONS — last updated 2026-05-09 -->

| Rank | Miner | Coin | Hashrate | Power | Daily Profit* | Detail Page |
|------|-------|------|----------|-------|---------------|-------------|
| 1 | Pinecone INIBOX PRO | INITVERSE | 2.4 Gh/s | 1,280 W | **$46.80** | [View](miners/specs/pinecone-matches-inibox-pro-24-ghs-initverse-miner.md) |
| 2 | Antminer Z15 Pro | ZEC | 840 KSol/s | 2,780 W | **$32.01** | [View](miners/specs/bitmain-antminer-z15-pro-zcash-miner-840ksol.md) |
| 3 | Antminer X9 | XMR | 1 MH/s | 2,472 W | **$26.85** | [View](miners/specs/bitmain-antminer-x9-monero-miner-1m.md) |
| 4 | Antminer S23 Hyd 3U | BTC | 1.16 PH/s | 11,020 W | **$23.15** | [View](miners/specs/bitmain-antminer-s23-hyd-3u-bitcoin-miner-116phs.md) |
| 5 | Pinecone INIBOX 850 | INITVERSE | 850 Mh/s | 500 W | **$16.48** | [View](miners/specs/pinecone-matches-inibox-850-mhs-initverse-miner.md) |

> \* Profitability estimates at $0.07/kWh electricity. **102 of 287 tracked miners are currently profitable.** [→ Full rankings](miners/index.md)

---

## 💰 Coin Prices

<!-- AUTO-UPDATED BY GITHUB ACTIONS -->

| Coin | Symbol | Algorithm | Guide |
|------|--------|-----------|-------|
| Bitcoin | BTC | SHA-256 | [bitcoin.md](coins/bitcoin.md) |
| Zcash | ZEC | Equihash | [zcash.md](coins/zcash.md) |
| Monero | XMR | RandomX | [monero.md](coins/monero.md) |
| Kaspa | KAS | kHeavyHash | [kaspa.md](coins/kaspa.md) |
| Ethereum Classic | ETC | ETHash | [ethereum-classic.md](coins/ethereum-classic.md) |
| Litecoin | LTC | Scrypt | [litecoin.md](coins/litecoin.md) |
| Dogecoin | DOGE | Scrypt | [dogecoin.md](coins/dogecoin.md) |
| Alephium | ALPH | Blake3 | [alephium.md](coins/alephium.md) |

---

## 🛒 Used Miner Marketplace

Buy and sell used mining hardware through our privacy-preserving AI middleman — seller contact info is never made public.

**Current listings:** [marketplace/listings.md](marketplace/listings.md)

**How to inquire about a listing:**

| Channel | How |
|---------|-----|
| 💬 Telegram | [@MiningDealBot](https://t.me/MiningDealBot) — send the listing ID |
| 🌐 Web form | [bt-miners.com/marketplace](https://bt-miners.com/marketplace) |
| 📧 Email | [deals@bt-miners.com](mailto:deals@bt-miners.com) |

**Want to list your miner for sale?** Email [deals@bt-miners.com](mailto:deals@bt-miners.com) with model, quantity, condition, and asking price. We post the listing within 24 hours — your contact info stays private.

---

## 📁 Repository Structure

```
awesome-crypto-mining/
├── miners/
│   ├── index.md                    # Full profitability rankings (auto-updated daily)
│   ├── specs/                      # Detailed pages for top 20 miners
│   ├── profitability/              # Daily profit history per miner (CSV)
│   └── prices/                     # Daily new + used price history (CSV)
├── coins/                          # Coin guides (BTC, ZEC, XMR, KAS, ETC, LTC, DOGE, ALPH)
├── algorithms/                     # Mining algorithm references
│   └── sha256.md · scrypt.md · equihash.md · kheavyhash.md · randomx.md · ethash.md · blake3.md
├── guides/
│   ├── beginners/                  # 5-step onboarding series
│   └── advanced/                   # ROI, farm scaling, solar mining, multi-algo strategy
├── marketplace/                    # Used miner listings + AI middleman docs
└── data/                           # Machine-readable JSON snapshots (updated daily)
    ├── daily-profitability.json
    ├── daily-prices.json
    └── coins-summary.json
```

---

## 🤖 AI Knowledge Layer

The structured data in this repo (`data/*.json`, `miners/profitability/*.csv`, `miners/prices/*.csv`) is designed to be consumed by AI assistants for natural language queries:

- *"What's the most profitable miner right now under $3,000?"*
- *"Has the Antminer Z15 Pro ever been profitable at $0.10/kWh?"*
- *"Show me all Scrypt miners and their current daily revenue"*

Because the repo auto-updates daily, any AI using it as a data source stays current without retraining.

---

## 🔄 Data Update Schedule

| Pipeline | Cron | What updates |
|----------|------|-------------|
| Profitability | Daily 00:00 UTC | `miners/index.md`, `miners/profitability/*.csv`, `data/daily-profitability.json` |
| Miner Prices | Daily 01:00 UTC | `miners/prices/*.csv`, `data/daily-prices.json` |
| Coin Prices | Daily 02:00 UTC | `coins/`, `data/coins-summary.json` |

---

## 🤝 Contributing

- **Submit a used miner listing** → email [deals@bt-miners.com](mailto:deals@bt-miners.com)
- **Fix a data error** → open an issue with the miner name and correct value
- **Improve a guide** → see [CONTRIBUTING.md](CONTRIBUTING.md) for content standards

---

## 📄 License

MIT License — data is free to use. If you build something with it, a link back is appreciated but not required.
