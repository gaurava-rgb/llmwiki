---
title: "so..."
reader_id: "01kn5drbxzx0t1qkc1e04wt8qt"
notion_page_id: "34a4ebe7-f118-815e-a13d-e84ace5472dd"
category: "tweet"
source_type: "Readwise web highlighter"
reader_url: "https://read.readwise.io/read/01kn5drbxzx0t1qkc1e04wt8qt"
source_url: "https://x.com/Gregorein/status/2038953944475472316/?rw_tt_thread=True"
author: "gregorein"
site: "X (formerly Twitter)"
tags: []
published: "2026-03-31"
saved_at: "2026-04-01"
reading_time: "3 mins"
summary: "Garry Tan's website is very large and inefficient, loading 6.42 MB with 169 requests just for the homepage. It sends unnecessary files like test code, duplicate images, and uncompressed pictures, wasting bandwidth. The audit shows that using AI without proper review leads to poor quality and bloated code."
content_hash: "1401ba30fdd793e892b16afe5af9311961f3e3219f1f6f3067390c14a44fcfb2"
---

so... I audited Garry's website after he bragged about 37K LOC/day and a 72-day shipping streak.

here's what 78,400 lines of AI slop code actually looks like in production.

a single homepage load of [garryslist.org](<http://garryslist.org/>) downloads 6.42 MB across 169 requests.

for a newsletter-blog-thingy.

1/9🧵

![Image](https://pbs.twimg.com/media/HEvJOO4asAATISw.jpg?name=orig)

![](https://pbs.twimg.com/profile_images/1922894268403941377/-dGWAt3N.jpg)

[Garry Tan](<https://twitter.com/garrytan>) [@garrytan](<https://twitter.com/garrytan>)

[ ](<https://twitter.com/garrytan/status/2038555792052506941>)

Absolutely insane week for agentic engineering

37K LOC per day across 5 projects

Still speeding up

![Image](https://pbs.twimg.com/media/HEpnM4FawAAhEe3.jpg?name=orig)

[Posted Mar 30, 2026 at 9:55AM](<https://twitter.com/garrytan/status/2038555792052506941>)

* * *

the homepage ships 28 TEST FILES to every visitor.

not test results - actual test harnesses.

membership_form_controller.test (89 KB), media_grid_controller.test (31 KB), story_composer_controller.test (19 KB)

...

300 KB of test code. All returning HTTP 200. All actively downloaded. HAR file doesn't lie.

2/9🧵

![Image](https://pbs.twimg.com/media/HEvJ7WKXkAA3hNi.jpg?name=orig)

* * *

it also downloads 78 Stimulus controller, including...

AI image generation

voice extraction

video generation

radar charts

draft review

lab evaluation

and the literal Rails "Hello World" scaffold (`hello_controller.js`, 157 bytes).

154 KB transferred. None of these are used on the homepage. The browser fetches all of them anyway.

3/9🧵

![Image](https://pbs.twimg.com/media/HEvKdLya0AIT2H0.jpg?name=orig)

* * *

the logo situation is my favorite 🖤

the same bear gets downloaded... 8 times per page load: 3 png copies, 2 WebP variants, 2 AVIF variants, and a 512x512 favicon.

one of the AVIF files is 0 bytes. an empty file. a failed image conversion that got deployed and served to production.

total logo bandwidth: 654kb for two logos.

4/9🧵

![Image](https://pbs.twimg.com/media/HEvLNJna0AAinZr.jpg?name=orig)

* * *

but the real bandwidth killer are article images served from CloudFront as raw, uncompressed PNGs:

  * Image 1: 2.07mb png
  * Image 2: 1.99mb png

...




the browser sends

>
>
>
> Accept: image/avif, image/webp
>
> explicitly asking for modern formats




the server ignores it and sends 4mb of raw PNG.

with WebP these would be 200-400kb combined. That's 4mb of waste from two images alone.

5/9🧵

![Image](https://pbs.twimg.com/media/HEvLodHaQAAjI8Q.jpg?name=orig)

* * *

more highlights from the audit

  * 520 KB Trix rich text editor (120kb transferred) loaded on a read-only homepage (a spillover from a backend?)
  * 47 images with empty `alt=""`... on a "civic engagement" site
  * the entire page content rendered TWICE in the DOM (mobile + desktop)
  * duplicate  tags in the <head></li><br/><li>an empty CSS file (just a manifest comment, content-hashed and served)</li><br/><li>PostHog analytics proxied through <code>/s/</code> to... bypass ad blockers, as his own source code comment says so</li><br/></ul><br/><p>6/9🧵 </p><br/><p><img alt="Image" src="<a href="https://pbs.twimg.com/media/HEvMEqFaAAAPmhd.png?name=orig" rel="nofollow">https://pbs.twimg.com/media/HEvMEqFaAAAPmhd.png?name=orig</a>" /></p>



* * *

The source code literally contains this comment:


    // Load SDK from our proxy (bypasses ad blockers)


A 501(c)(4) nonprofit "civic engagement organization" actively circumventing its readers' privacy tools to track them harder.

while shipping test files, a 0-byte broken image, and 4 MB of raw PNGs to production.

7/9🧵

![Image](https://pbs.twimg.com/media/HEvM5B8WgAAHE-j.png?name=orig)

* * *

for context: the Hacker News homepage, run by Y Combinator, Garry's own org, makes 7 requests and transfers 12kb

Garry's page makes 169 requests and transfers 6.42mb

562x heavier

even discounting images, 73% of the bandwidth is waste.

one could say it's a HAR truth.

8/9🧵

![Image](https://pbs.twimg.com/media/HEvQJj1WUAA8k06.png?name=orig)

* * *

AI & llms are an incredible tool, i use them every day... even burned over 3 billion tokens last year (2.5 in cursor alone)

but AI amplifies whatever process you feed it - including no process at all. Garry's site is what happens when you replace code review with a shipping streak counter.

A Duolingo streak for `git push` 🔥

the automatons did exactly what they were told. nobody told them to stop.

* * *




this is a client-side audit only, of what the browser downloads. i didn't read a single line of the source slop. idc, qed 🧵

![Image](https://pbs.twimg.com/media/HEvOqSyacAAUoKE.png?name=orig)

* * *

for added context: when a 17yo developer ([@xiaonweb](<https://twitter.com/xiaonweb>)) politely pointed out that bragging about LOC is silly, Garry's response was to publicly call them a "clout farmer."

the "clout farming" teen... wrote a browser engine in Rust at 17. HTML tokenizer, CSS cascade, box model layout, GPU renderer via wgpu, and published a technical breakdown showing deeper understanding of how the web works than most senior engineers I've worked with (including me, cos I've never dug that low-level).

vs

the "shipping" guy, the president of Y Combinator, a multi-billion dollar startup kingmaker, who mass-generates code with 113 Claude sessions a week, counts lines like a Duolingo streak, and ships test files, 0-byte AVIFs, and 4 MB uncompressed PNGs to production.

right, punch down at a teenager. on main @.

<https://t.co/1pd36T14MG>

![Image](https://pbs.twimg.com/media/HEvSH37WcAEKWwI.png?name=orig)
