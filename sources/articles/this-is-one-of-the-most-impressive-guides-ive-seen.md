---
title: "This is one of the most impressive guides I've seen..."
reader_id: "01kkj8v4scg0vn9gqvy26wvw2f"
notion_page_id: ""
category: "tweet"
source_type: "Reader Share Sheet Android"
reader_url: "https://read.readwise.io/read/01kkj8v4scg0vn9gqvy26wvw2f"
source_url: "https://x.com/i/status/2031802820924436506/?rw_tt_thread=True"
author: "am.will"
site: "X (formerly Twitter)"
tags: []
published: "2026-03-11"
saved_at: "2026-03-13"
reading_time: "4 mins"
summary: "This guide shows a new way to create consistent pixel art game animations using AI. It starts with one key sprite frame and generates a full animation strip in one step. Then, it normalizes the frames to fit the game, making the process easier and more reliable."
content_hash: "e625a8b4c849ffcf95cf3e646c256e9b5d0aee4e847cc8e16a5d8b41b8227e78"
---

This is one of the most impressive guides I've seen for building games with Codex.

Even if you're not building any games, just look how impressive this is.

You're not pushing your agents enough.

We are just barely tapping into their potential.

![](https://pbs.twimg.com/profile_images/1896733293908807680/_r8j7E1A.jpg)

[Chong-U](<https://twitter.com/chongdashu>) [@chongdashu](<https://twitter.com/chongdashu>)

[ ](<https://twitter.com/chongdashu/status/2031743032266043687>)

![Generating Animated Game Sprites using GPT 5.4 + Image 1.5](https://pbs.twimg.com/media/HDIzdmZWkAAusE_.jpg)

I recently posted [this tweet](<https://x.com/chongdashu/status/2031474716704436484>) that showed how I created an animated pixel art pirate game character.

Since that tweet, I've gone ahead and improved the image generation.

A lot of you showed interest (thanks!) - and even more had questions about the workflow I used. Rather than using threads, I thought I'd give X articles a try to showcase what I'm doing to get

**Disclaimer:** This workflow is still **_experimental_** i.e. I am still figuring out the best way to get good results. So treat it as an educational resource, but it's not meant to be a definitive guide in any way.

Let's go!

## Workflow Overview

The core idea is simple:

  1. start from one approved in-game frame
  2. ask GPT Image to create a whole animation strip around that frame
  3. normalize the strip into fixed-size game frames
  4. rebuild the asset index and preview it in-engine



## 1\. Start From A Shipped Seed Frame

We learned that consistency gets much better when the model is anchored to the actual production sprite, not a loose concept.

For the hurt animation, the seed image was the following generated frame

 _(I'll write a separate tutorial on how I got this first image) but_ [this tweet](<https://x.com/chongdashu/status/2031474716704436484>) _does cover the high level approach)_

![Image](https://pbs.twimg.com/media/HDImmWlXIAAXON5.png)

That matters because it locks in:

  * the face
  * the body proportions
  * the palette
  * the silhouette



## 2\. Build A Reference Canvas For The Edit API

We do not send the raw 64x64 sprite directly. We upscale it with nearest-neighbor and place it into a larger transparent edit canvas with reserved frame slots.

For the hurt run, taking the above idle/frame-01.png and putting it into a 1024x1024 canvas, we get the following:

![Image](https://pbs.twimg.com/media/HDIn9w3bQAAqn2Q.png)

That canvas is created with a python script.

## 3\. Ask For The Full Strip, Not Tiny Frame Edits

One thing to note is that trying to generate animations frame-by-frame did not work well for character consistency. Instead the better method is to ask for one whole strip at once.

So for the hurt animation, I used the prompt:

Intended use: candidate production spritesheet for a 2D side-view pirate platformer hurt animation review. Edit the provided transparent reference-canvas image into a single horizontal four-frame hurt spritesheet. The existing sprite in the leftmost slot is the exact shipped idle-v2 starting frame and must remain the starting frame for this sequence: same compact pirate hero, same right-facing side view, same red bandana, same blue tunic, same brown boots, same tan skin, same readable face, same proportions, same pixel-art silhouette family. Composition: keep the image transparent, keep exactly one row of four equal 256x256 frame slots laid out left to right across the 1024x1024 canvas, centered vertically, no overlap between frame slots, no extra characters, no labels, no UI. Action: frame 1 stays as the calm idle starting pose, frames 2 through 4 show a short hurt reaction from a hit, with the same pirate recoiling backward, torso pulled back, head jolted, one brief pain expression, then slight recovery. Keep body size, head size, and outfit proportions consistent across all four frames. Style: authentic 16-bit pixel art, crisp pixel clusters, stepped shading, restrained palette, production game asset, not concept art. Constraints: no sword, no weapon, no scenery, no floor, no glow, no atmospheric haze, no impact effects, no shadows outside the sprite contours, no collage, no poster layout, no blurry details. Keep wide transparent empty space outside the four frame slots.

This gave a consistent sequence as you can see below:

![Image](https://pbs.twimg.com/media/HDIolqxWUAANcqA.jpg)

## 4\. Normalize The Strip Into Real Game Frames

The raw GPT strip is not yet game-ready. We import it into standardised format with 64x64 frames with another python script. Basically, what it does is

  * detecting the sprite components in the raw strip
  * using the player 'anchor' image (idle/frame-01.png)
  * computing one shared scale for the whole animation
  * padding each frame into a 64x64 transparent canvas
  * optionally locking frame 01 to the exact shipped idle frame



That last part is important for hurt. We explicitly replace exported 01.png with the real idle frame so the animation starts from the exact sprite already used in-game.

This results is 'normalised' spritesheets having a standard frame size for each panel.

![Image](https://pbs.twimg.com/media/HDIpZS1aEAEyJh5.png)

This works surprisingly well even for more complex animations. For example, see the Attack animation below

![Image](https://pbs.twimg.com/media/HDIp2MYXMAAHpKP.jpg)

![Image](https://pbs.twimg.com/media/HDIsqxIXcAAx-au.png)

## 5\. Lessons

**5.1 Handling complex poses**

Problems can come when one pose was taller than another. For example:

  * a sword-up attack frame is naturally taller than a neutral frame
  * if you scale that pose down on its own, the whole character looks smaller

![Image](https://pbs.twimg.com/media/HDIqBWUaoAAbJI2.png)




The fix was:

  * use one global scale for the whole strip
  * let pose differences show up as extra height inside the frame
  * use padding and a shared anchor instead of per-frame rescaling



## In Summary

If we want consistent AI-generated sprite animations, the workflow should be:

  1. pick the exact shipped sprite frame to anchor from
  2. generate a full strip in one request
  3. normalize with one shared scale
  4. lock frame 01 back to the shipped sprite when the animation should start from idle
  5. verify in the preview scene before treating it as production-ready



That is the part that has made the results noticeably more stable.

[Posted Mar 11, 2026 at 2:44PM](<https://twitter.com/chongdashu/status/2031743032266043687>)

* * *

if you're here to pixel peep looking for perfect sprites, go yell into your pillow. this is about building assets using ai agents, which is a _somewhat_ new niche.

we know you can do better by hand. who cares?

doesn't make this any less impressive as the models improve.
