---
title: "This basic stuff does sound complicated but it takes 5..."
reader_id: "01kkvhw9rwc8p1v6yt469771fk"
notion_page_id: ""
category: "tweet"
source_type: "Reader Share Sheet Android"
reader_url: "https://read.readwise.io/read/01kkvhw9rwc8p1v6yt469771fk"
source_url: "https://x.com/i/status/2033547042396557421/?rw_tt_thread=True"
author: "@levelsio"
site: "X (formerly Twitter)"
tags: []
published: "2026-03-16"
saved_at: "2026-03-16"
reading_time: "1 min"
summary: "Setting up a VPS is quick and easy, taking only five minutes. Use tools like Tailscale and Cloudflare to keep your server safe by limiting access. Never expose your VPS directly to the internet to avoid hacks and attacks."
content_hash: "31c798d41253d4eccd0cc7dcf71cc657a65faaef186774e9d04f6460706d4355"
---

This basic stuff does sound complicated but it takes 5 minutes to set up

After this part, running a VPS is cheap, safe and easy

Especially with Claude Code running it, which you can ask to check if the server is safe and stuff like enable auto upgrades and auto reboot after upgrade

![](https://pbs.twimg.com/profile_images/1996831016720486400/vycHz0uG.jpg)

[@levelsio](<https://twitter.com/levelsio>) [@levelsio](<https://twitter.com/levelsio>)

[ ](<https://twitter.com/levelsio/status/2033546675063554213>)

When I set up a new Hetzner VPS first thing I do install Tailscale and once I'm in via Tailscale lock down the firewall to only accept web traffic on HTTPS 443 for Cloudflare IPs and SSH 22 for Tailscale IP

That way nobody can get in

I know I keep repeating this but it should be basics of setting up a new VPS

So basic IMHO it should be part of any VPS service to default install Tailscale and enable it so it's the only way to get in

Why?

A VPS server is just like your laptop or destop computer but now imagine if it's connected to the entire internet with 8 billion people that can access it and try hack it

You want to only have it accessible to you

And if you want to host a website on your VPS (like I do), you should only let Cloudflare access your VPS so it can stand in front and block any hack attempts

Never expose a VPS to the world wide web which realistically is the world WILD web

![](https://pbs.twimg.com/profile_images/1822979568224878592/Cnwbrplz.jpg)

[Areeb ur Rub](<https://twitter.com/areeburrub>) [@areeburrub](<https://twitter.com/areeburrub>)

[ ](<https://twitter.com/areeburrub/status/2033544509477544201>)

[@levelsio](<https://twitter.com/levelsio>) [@nfcodes](<https://twitter.com/nfcodes>) I created a redis instance on hetzner with public port open for few minutes and someone was running a cryptominer the next moment taking 50% CPU 💀

After that I always use [@Tailscale](<https://twitter.com/Tailscale>) 👌

[Posted Mar 16, 2026 at 2:02PM](<https://twitter.com/areeburrub/status/2033544509477544201>)

[Posted Mar 16, 2026 at 2:11PM](<https://twitter.com/levelsio/status/2033546675063554213>)
