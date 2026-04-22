---
title: "yesterday someone leaked a full quant trading system on GitHub"
reader_id: "01kjt05k3msapf7va5204aksf4"
notion_page_id: "34a4ebe7-f118-819b-a088-f08df1ab2e6e"
category: "tweet"
source_type: "Reader Share Sheet Android"
reader_url: "https://read.readwise.io/read/01kjt05k3msapf7va5204aksf4"
source_url: "https://x.com/i/status/2028582457000247657/?rw_tt_thread=True"
author: "Archive"
site: "X (formerly Twitter)"
tags: []
published: "2026-03-02"
saved_at: "2026-03-03"
reading_time: "2 mins"
summary: "Someone leaked a full quant trading system on GitHub with 5,000 lines of code and 25 mathematical factors. The system uses Python and C++ to analyze data from Binance, news, social media, and blockchain to trade crypto. It costs about $200 a month to run and is open source for anyone to build."
content_hash: "50b61b0cf62840914d180305408c9392a021ac3a7080be79a4b2b9de4d614c13"
---

**yesterday someone leaked a full quant trading system on GitHub**

before they deleted it i forked everything

5,000 lines of code. 7 modules. 25 mathematical factors

funds use this system to **manage millions**

i studied it for a week. then pointed it at crypto markets on polymarket

here's the full breakdown

**you can feed this to your claude and build the same thing**

for just **$200**

**ARCHITECTURE:**

Python thinks, analyzes, calculates

C++ executes orders in 5-10ms

data → factors → AI → strategy → risk → execution

**DATA. 4 streams simultaneously:**

  * Binance WebSocket: prices every second, orderbook at 20 levels
  * AlphaVantage: news with sentiment score from -1 to +1

-X: mention volume, engagement, influencer activity

  * On-chain: BTC flows to/from exchanges



cache in Redis (<1ms). history in TimescaleDB

**FACTORS:**

the system calculates 25+ factors every 5 minutes:

\- price momentum over 1.5 hours

\- acceleration = momentum_30m - momentum_1h

\- RSI(14): above 70 = overbought, below 30 = oversold

\- MACD: fast EMA(12) minus slow EMA(26)

**microstructure:**

\- Order Flow Imbalance = (buy volume - sell volume) / total. above +0.3 = strong buyer pressure

\- VPIN = |buy_vol - sell_vol| / total. above 0.75 = smart money is moving

**volatility:**

\- VaR(95%) = mean - 1.645 × std. answers: "what's my max loss in 95% of cases?"

\- Sharpe = (return - risk free) / volatility. above 1.0 = good. above 2.0 = excellent

every factor converted to z-score and combined:

Composite Score = Σ (weight × z_score)

top 25 assets by score go to work

**AI:**

ClowdBot reads every news article and returns JSON

every historical article stored as a 384-dimensional vector

**PROBABILITY MODEL**

Geometric Brownian Motion:

P(BTC > target price) = N(d1) d1 = [ln(current/target) + (σ²/2)T] / (σ√T)

then 4 adjustments on top:

\- momentum: +/-5%

\- AI sentiment: +/-7%

\- order flow: +/-2%

\- historical patterns: +/-8%

compare final probability against polymarket price if edge > 10%: enter

**RISK**

  * Quarter Kelly for position sizing
  * max 5% bankroll per trade
  * drawdown 15% = bot stops
  * VaR < 3% per day
  * correlation between positions < 0.7
  * never take more than 1% of market liquidity



key insight is don't hold to expiry. trade the movement, not the outcome

**cost:**

→ Binance API: free

→ OpenAI: $50-100/month

→ AWS EC2: $120/month

→ monitoring: free

**\- total: $200-300/month -**

code is open source. formulas above. you already have claude

**the only thing between you and a working system is one free evening** ****

* * *

more breakdowns and details like this in my tg channel:

[t.me/+oCWYO2RdBzRjM…](<https://t.me/+oCWYO2RdBzRjMjM6>)
