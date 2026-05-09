# Contributing to Awesome Crypto Mining

Thanks for helping keep this resource accurate and useful for the mining community. Here is everything you need to know.

---

## ♻️ How to Submit a Used Miner Listing

We handle listings manually to prevent scams and protect everyone's privacy.

**Send an email to [deals@bt-miners.com](mailto:deals@bt-miners.com) with the following:**

| Field | Example |
|-------|---------|
| Model | Antminer S19j Pro |
| Quantity | 4 units |
| Condition | Used – good (all hash boards working, minor cosmetic wear) |
| Asking price | $380 each or $1,400 for all four |

The team will post the listing in [`marketplace/listings.md`](marketplace/listings.md) within 24 hours. Your name, email address, and contact information are never published. Interested buyers contact us first, and we facilitate the introduction.

You can also reach us on Telegram ([@MiningDealBot](https://t.me/MiningDealBot)) or through the web form at [bt-miners.com/marketplace](https://bt-miners.com/marketplace).

---

## 🐛 How to Report a Data Error

If you spot a wrong hash rate, incorrect price, or stale profitability figure:

1. Open a [GitHub Issue](../../issues/new) in this repository.
2. Add the label `data-error`.
3. Include the following in the issue body:
   - **Date** you noticed the error (e.g., 2026-05-09)
   - **Miner or coin name** (e.g., IceRiver KS3, Kaspa)
   - **What is wrong** — what the data shows vs. what it should show, with a source link if you have one

We aim to fix confirmed data errors within one business day.

---

## ✍️ How to Contribute a Guide

We welcome well-written, practical guides aimed at real miners.

**Steps:**

1. Fork this repository.
2. Write your guide as a Markdown file in the appropriate folder:
   - `guides/beginners/` — introductory topics, no prior mining experience assumed
   - `guides/advanced/` — overclocking, firmware flashing, pool optimization, etc.
3. Name the file descriptively, e.g., `overclocking-antminer-s21.md`.
4. Open a pull request with a short description of what the guide covers and who it is for.

**Style guidelines:**

- Write in plain English. If you must use a technical term, define it in parentheses the first time: e.g., "hash rate (the speed at which a miner performs calculations)."
- Aim for **800–1,200 words**. Shorter is fine if the topic is narrow; longer is fine if the topic genuinely needs it.
- Use numbered steps for processes and bullet points for lists of options.
- Link to relevant miner spec pages or coin guides already in the repo rather than duplicating information.
- No affiliate links, no promotional language.

---

## 📋 CSV Data Format Specs

All data files live under `data/`. GitHub Actions refresh them daily. If you are contributing scripts or correcting raw data files, follow these column definitions exactly.

### Profitability CSV (`data/profitability/<miner-slug>.csv`)

```
date,daily_profit_usd,monthly_profit_usd,coin,hashrate,power_w,electricity_cost
2026-05-09,14.20,432.60,BTC,270TH,3610,0.07
```

| Column | Format | Notes |
|--------|--------|-------|
| `date` | YYYY-MM-DD | UTC date |
| `daily_profit_usd` | Decimal, 2 places | Revenue minus electricity |
| `monthly_profit_usd` | Decimal, 2 places | `daily_profit_usd × 30` |
| `coin` | Ticker symbol | E.g., BTC, KAS, LTC |
| `hashrate` | Number + unit | E.g., 270TH, 8TH, 16GH |
| `power_w` | Integer | Watts at wall |
| `electricity_cost` | Decimal, 2 places | USD per kWh assumed |

### Miner Price CSV (`data/miner-prices/<miner-slug>.csv`)

```
date,new_price_usd,used_price_usd,used_source
2026-05-09,2499,1350,marketplace/listings.md
```

| Column | Format | Notes |
|--------|--------|-------|
| `date` | YYYY-MM-DD | UTC date |
| `new_price_usd` | Integer | Leave blank if unavailable |
| `used_price_usd` | Integer | Median of active listings |
| `used_source` | URL or path | Where used price was sourced |

### Coin Price CSV (`data/coin-prices/<coin-ticker>.csv`)

```
date,price_usd,volume_usd,market_cap_usd
2026-05-09,62400,28500000000,1230000000000
```

| Column | Format | Notes |
|--------|--------|-------|
| `date` | YYYY-MM-DD | UTC date |
| `price_usd` | Decimal, 2 places | Closing price |
| `volume_usd` | Integer | 24h trading volume |
| `market_cap_usd` | Integer | Circulating supply × price |

---

## 🤝 Code of Conduct

This is a community project and we want it to stay welcoming and useful for everyone — beginners asking basic questions and veterans contributing advanced guides alike.

**We ask everyone to:**

- Be respectful and patient, especially with newcomers.
- Focus feedback on ideas and data, not on people.
- Acknowledge that mining setups vary widely — what works for one person may not work for another.
- Flag misinformation politely and with a source, rather than dismissing it.

Harassment, spam, or dishonest listings will result in removal from the project. If you see something that violates this spirit, open an issue or email [deals@bt-miners.com](mailto:deals@bt-miners.com).

We are all here to make crypto mining a little less confusing and a lot more accessible. Welcome aboard.
