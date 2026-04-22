---
title: "yesterday a friend messaged me: \"i have 48 hours before..."
reader_id: "01kjt0a29vjqz9c9rz91zq994v"
notion_page_id: ""
category: "tweet"
source_type: "Reader Share Sheet Android"
reader_url: "https://read.readwise.io/read/01kjt0a29vjqz9c9rz91zq994v"
source_url: "https://x.com/i/status/2028776579183116652/?rw_tt_thread=True"
author: "dunik"
site: "X (formerly Twitter)"
tags: []
published: "2026-03-03"
saved_at: "2026-03-03"
reading_time: "1 min"
summary: "A data engineer shared a trading strategy that predicts trader panic, not event outcomes, to trade against the crowd. The bot triggers trades when price, volume, and order conditions align, aiming for profit by exploiting market panic. After rewriting the strategy in Python, the user made a small profit in the first week."
content_hash: "1dca9ccee22a791d592276e79d6e9988027de73b1a16f87555d9bc045b98b0da"
---

**yesterday a friend messaged me: "i have 48 hours before the lawyers find out. you need to see this"**

he worked as a data engineer at a hedge fund in Zurich. he got fired on friday

on monday, his vpn was still working

he downloaded 3 jupyter notebooks before his access got cut

one of them was called **polymarket_edge_model_v4_FINAL.ipynb**

**THE CORE IDEA:**

the fund doesn’t predict the outcome of the event. they predict the PANIC of other traders

when the price moves sharply, 80% of players close at a loss. the fund takes the other side

"liquidity vacuum trade"

**TRIGGER — 3 conditions at the same time:**

/ price >2% in 90 seconds

/ volume >3x the average

/ 70%+ of orders on one side

the bot trades AGAINST the crowd

expected_price = EMA(200) × (1 + sentiment_offset)

deviation >12% = entry

stop at 25%

take profit at EMA ±3%

win rate: 73.2% across 1,847 trades. sharpe 2.7

i rewrote it in python over the weekend. 172 lines

first week: +$412 from $1,500

the formulas are above. claude will handle the rest.
