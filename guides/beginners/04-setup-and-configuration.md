# Setup & Configuration

*Your miner arrived. Here's how to get it running in under an hour.*

---

## What's in the Box

Most ASIC miners ship with just the essentials:

- **The miner unit itself** — the main hashing hardware
- **Power cables** — typically C13/C19 or proprietary connectors
- **Ethernet cable** (sometimes included, sometimes not)
- **Quick-start guide** (often minimal and in multiple languages)

**What's NOT usually included:**
- Power supply unit (PSU) — some miners have integrated PSUs, but many require a separate one
- Network switch or router access
- Any mounting hardware

Check the product listing carefully before ordering so you have everything ready on arrival day.

---

## What You Need Before You Start

### Power Supply

Many ASIC miners — especially Bitcoin miners — require a high-wattage PSU rated for their draw **plus 20% headroom**. If your miner draws 3,500W, you need a PSU rated for at least 4,200W.

- Some miners (like many Goldshell units) have the PSU built in
- Larger miners (Bitmain S21, WhatsMiner M50, etc.) require a separate, high-voltage PSU
- Use a dedicated **20A or 30A circuit** — never plug a heavy miner into a shared household outlet

If you're not sure about your electrical setup, consult a licensed electrician. Overloaded circuits are a fire hazard.

### Internet Connection

Miners only need a basic internet connection to communicate with the mining pool. A standard home router works fine.

- Connect via **Ethernet cable** (not Wi-Fi — most miners don't have Wi-Fi)
- The miner just needs to reach the internet; bandwidth requirements are minimal
- Run the cable to wherever you're placing the miner before powering it on

### Placement and Ventilation

ASIC miners are loud and generate significant heat. Plan your placement accordingly.

- **Keep at least 12–18 inches of clearance** in front of and behind the miner for airflow
- **Intake goes in, exhaust goes out** — don't let hot exhaust air recirculate back to the intake
- Ideal ambient temperature: **15–25°C (59–77°F)**
- Above 35°C, most miners will throttle or shut down automatically
- Common locations: garage, basement, utility room, shed, or dedicated mining space

---

## Physical Setup

1. Place the miner on a stable, flat surface
2. Connect the Ethernet cable to the miner's LAN port
3. Connect the power cable(s) to the miner and plug into your outlet or PDU (power distribution unit)
4. Power on the miner — fans will spin up immediately and loudly

The miner will take 1–3 minutes to boot. During this time, it gets an IP address from your router via DHCP.

---

## Finding Your Miner's IP Address

To configure the miner, you need to access its web interface. First, find its IP address.

**Option 1: Check your router's admin panel**
Log into your router (usually at `192.168.1.1` or `192.168.0.1`) and look at the list of connected devices. The miner should appear with a name like "antminer" or "iceriver."

**Option 2: Use a network scanner**
Tools like [Advanced IP Scanner](https://www.advanced-ip-scanner.com) (Windows) or [Angry IP Scanner](https://angryip.org) (Mac/Linux) scan your local network and list all devices with their IP addresses.

**Option 3: Manufacturer default**
Some miners default to a fixed IP. Check your manual — for example, some Goldshell miners default to `192.168.1.1`.

---

## Logging Into the Web Interface

Open a browser on any computer connected to the same network. Type the miner's IP address into the address bar — for example:

```
http://192.168.1.105
```

You'll see a login page. Default credentials are usually:

| Brand | Default Username | Default Password |
|-------|-----------------|-----------------|
| Bitmain (Antminer) | root | root |
| MicroBT (WhatsMiner) | admin | admin |
| IceRiver | admin | (check manual) |
| Goldshell | admin | 123456a |

**Change your password immediately after first login.** The default credentials are public knowledge.

---

## Basic Settings: Connecting to Your Pool

Once logged in, find the **Pool Settings** or **Miner Configuration** section. You'll need to fill in three fields:

### Pool URL
This is the address of the mining pool you want to connect to. Your pool's website will give you this. It typically looks like:

```
stratum+tcp://stratum.braiins.com:3333
```

### Worker Name
This is how the pool identifies your miner. It's usually in the format:

```
YourPoolUsername.WorkerName
```

For example: `alice.garage_miner_01`

You can name it anything — just make it descriptive if you have multiple miners.

### Worker Password
Most pools accept any value here. Common defaults are `x`, `123`, or `anything`. Check your pool's documentation.

Save the settings. The miner will restart and begin connecting to the pool within a few minutes.

---

## Reading the Dashboard

Once connected, the miner's web interface shows a real-time dashboard. Here's what the key metrics mean:

| Metric | What It Means |
|--------|--------------|
| **Hashrate** | How fast the miner is working (TH/s, GH/s, etc.) |
| **Temperature** | Chip and/or board temperature — watch for anything above 80°C |
| **Fan Speed** | RPM of cooling fans — sudden drops may indicate a failed fan |
| **Accepted Shares** | Work submitted to the pool that was valid |
| **Rejected Shares** | Work the pool didn't accept — a small % is normal |
| **Pool Status** | Whether the miner is successfully connected to the pool |

**Accepted shares** are what count toward your earnings. A rejection rate above 2–3% may indicate a network issue or misconfigured pool URL.

---

## What a Healthy Miner Looks Like

- Hashrate is close to the rated spec (within 5–10%)
- Temperature is stable, not climbing over time
- Accepted shares increasing steadily
- Pool status shows "Connected" or "Active"

If something looks off, don't panic — the troubleshooting section of your miner's documentation is your first stop.

---

**Next Step → [Join a Mining Pool](05-join-a-mining-pool.md)**
