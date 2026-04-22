---
title: "james has achieved distributed opencode"
reader_id: "01kmnwjdvmx29xfvr4qq1wpc3s"
notion_page_id: ""
category: "tweet"
source_type: "Reader Share Sheet Android"
reader_url: "https://read.readwise.io/read/01kmnwjdvmx29xfvr4qq1wpc3s"
source_url: "https://x.com/i/status/2036925457417822299/?rw_tt_thread=True"
author: "dax"
site: "X (formerly Twitter)"
tags: []
published: "2026-03-25"
saved_at: "2026-03-26"
reading_time: "1 min"
summary: "James created OpenCode, which lets code run on your laptop or in remote cloud sandboxes. If you close your laptop or delete the remote sandbox, your work stays safe and syncs back when you return. This system can restore sessions easily, even if the remote environment is destroyed."
content_hash: "ef212e862aa1d6eb4346215ab851b84b1799e8497b09a5f945a0bdf63fa8aeed"
---

james has achieved distributed opencode

agents can run on your laptop, on a remote server, in a cloud sandbox provider

shut your laptop and things keep running

open it back up and all the data syncs

delete the sandbox nothing is lost

![](https://pbs.twimg.com/profile_images/1966306118621179904/OnblkvjY.jpg)

[James Long](<https://twitter.com/jlongster>) [@jlongster](<https://twitter.com/jlongster>)

[ ](<https://twitter.com/jlongster/status/2036924361379037224>)

OpenCode is about to get more powerful with remote sandboxes

I showed a brief demo before, but here's a much more in-depth demo. it's not hard to add basic support for a remote env, but handling all the edge cases like when a remote env gets deleted is difficult. especially if care about good UX

You never want to lose session data. so the choices are: run the session in your env, but run all tool calls remotely. that's too complex and painful.

The other way is to just let the full session run remotely, but sync back all the session data in your env. We chose this path: we built a syncing system which logs all events in a way that we can always recreate your entire session.

That means the remote env could get destroyed, but we can easily restore it. it also opens up other interesting ideas which we'll be exploring

[Posted Mar 25, 2026 at 9:53PM](<https://twitter.com/jlongster/status/2036924361379037224>)

* * *

the ux in this video is temporary, just demonstrates the primitives

now we get to figure out how to wrap this in a great experience

* * *

this also allows for so many interesting configurations

maybe your laptop is the "home" device. it can kick off agents and you can connect your phone as a remote controller

or run it on your phone standalone - it can use remote sandboxes to get work done

or put the home server
