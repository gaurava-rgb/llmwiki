---
title: "We got 7M views on YouTube with completely automated content"
reader_id: "01kk99kqmvssd073tjp7btcv7x"
notion_page_id: "34a4ebe7-f118-81a6-8607-dd263a61707a"
category: "tweet"
source_type: "Reader Share Sheet Android"
reader_url: "https://read.readwise.io/read/01kk99kqmvssd073tjp7btcv7x"
source_url: "https://x.com/i/status/2030716132093460742/?rw_tt_thread=True"
author: "Mau Baron"
site: "X (formerly Twitter)"
tags: []
published: "2026-03-08"
saved_at: "2026-03-09"
reading_time: "4 mins"
summary: "The author and a partner automated their YouTube channel to create hundreds of videos quickly using viral clips and custom CTAs. They used Python scripts to scrape and stitch videos, then scheduled posts for growth. This method helped them gain 7 million views without manual uploading."
content_hash: "d999b06b460552f6cb02df4fe0afb59789020c104d4ac6c20bb0a2d88d74bfc2"
---

![We got 7M views on YouTube with completely automated content](https://pbs.twimg.com/media/HC6KsJWaUAAzRI3.jpg)

Our YouTube channel currently has 61k subscribers and we've never uploaded or made a single post ourselves. Everything has been completely automated.

![Image](https://pbs.twimg.com/media/HCp8pHkXEAALr6G.jpg)

it takes @ErnestoSOFTWARE and I 10 minutes to create 700 posts, and I'm about to show exactly how you can do this too.

This should not be your main distribution strategy, but, the videos are so easy to make that it's still worth it to have as PART of your strategy in the search for total market domination.

The format is very simple: use familiar viral videos as hooks and then stitch a direct CTA to the video, here's an example:

Your browser does not support the video tag.

## It's literally that simple, the hooks can be from any viral creator, in this example we're using hooks from ZackD Films.

## Step #1: Find your viral hooks

This is the most important part of the whole process. Spend some time finding creators with great numbers, ideally your users are watching these videos regularly.

This is why I love ZackD videos, he consistently gets millions of views per post and chances are that your target audience is watching them as well.

Whoever the creator may be you have to make sure the video feels like brainrot to the user. This is part of the shock that makes these videos effective.

In this article i'm just gonna go with ZackD videos.

## Step #2: Create the CTA clip of your app

Using the editor of your choice you are going to create a little CTA clip which you will then stitch to the hook.

In our case we just grabbed some images from Pinterest and used CapCut to add some transitions and effects.

Make sure you are using a recognizable viral song that goes with your CTA clip.

Here's a little video tutorial on how to create this clip:

Your browser does not support the video tag.


## Step #3: Scrape and Stitch everything together with Python:

After you've identified the creator you want to grab the hooks from and you've edited your little clip you are now ready to create a script that will scrape the videos from YouTube and then stitch them together.

You can make this as simple or complex as you want, in reality this could be an OpenClaw agent that get's everything done for you.

But I wanted to go over the basics first and then you can go further into making an agent out of this yourself if you want to.

Creating the scraper is as simple as creating a new python virtual environment and telling Claude Code to create the scraper for you.

You essentially want to tell Claude to use a headless browser to scrape videos when provided with a creator's URL

Here's a little tutorial on how to create this script with Claude:

Your browser does not support the video tag.

And here's the EXACT same cave man prompt I used in the video:

Hey Claude, I need you to create for me a scraper that uses a headless browser to download the YouTube Shorts videos from a given creator and then scroll down and download the next one and then scroll down and down on the next video and so on and so forth for ten times for ten different videos. The way this is going to work is I'm going to provide to you the link of a certain YouTube profile and then you're going to start downloading the videos from that creator. The link is going to be to their YouTube Shorts and again I just want to scrape each video one by one for ten different times, okay.

After you scrape all of the videos you want it's now time to stitch them together into one single video that you are then going to schedule to TikTok

Again this is just a matter of telling Claude Code to do it for you, no need to overcomplicate this at all.

Here's how:

Your browser does not support the video tag.

Here's the EXACT cave man prompt I used:

Hey Claude! Now I need you to create a script and to run it that grabs the first three seconds of the YouTube videos that you just downloaded. In the downloads folder you're going to grab only the first three seconds and then immediately after you want to stitch the video titled CTAvideo.mp4 found in the same folder you're on. You're going to show the YouTube video for the first three seconds and then switch to CTA Video. You're going to do the same thing for each one of the videos, grabbing always the same CTA video. Go!

* * *

Once you have your videos created all you need to do is schedule them using the tool of your choice.

We use post bridge by @jackfriks but any will work. YouTube is a little tricky so I'd recommend posting manually for the first week before fully automating.

Having said that, we did upload through a scheduler since day 1 but we got shadow banned multiple times during this process and it took us weeks to get out of it.

That's it, now you know how to create a full system that let's you create hundreds of videos in literally minutes.
