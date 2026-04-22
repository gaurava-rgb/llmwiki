---
title: "attended a gem of an event organized by @GregKamradt at..."
reader_id: "01jy72yd8k32x6e6s6m59ddee7"
notion_page_id: ""
category: "tweet"
source_type: "Reader Share Sheet iOS"
reader_url: "https://read.readwise.io/read/01jy72yd8k32x6e6s6m59ddee7"
source_url: "https://x.com/nichochar/status/1935844386400878597/?s=12&rw_tt_thread=True"
author: "Nicholas Charriere"
site: "X (formerly Twitter)"
tags: ["ai", "twitter"]
published: "2025-06-19"
saved_at: "2025-06-20"
reading_time: "2 mins"
summary: "Nicholas Charriere attended an event where top builders shared how they make AI remember things better. Different teams use unique methods to handle memory, but the technology is still very new and evolving fast. In the future, AI will know users well and offer personalized experiences based on memory."
content_hash: "6a697baf6960f51a4cf52c46d479d882cde488fb8d80c14eae1328a38f61fdc9"
---

attended a gem of an event organized by [@GregKamradt](<https://twitter.com/GregKamradt>) at [@LangChainAI](<https://twitter.com/LangChainAI>) last night.

pretty rare to hear direct insights from top builders (cursor, langchain, newcomputer, headstart) how they actually get LLMs to "remember stuff".

my raw notes 👇

1/8

![](https://pbs.twimg.com/media/Gt12YnvWwAAUdSW.jpg)

* * *

[Cursor] [@yash_anysphere](<https://twitter.com/yash_anysphere>) is working on the "memories" feature in Cursor alone (what!?)

The feature allows the editor to remember some of your preferences and carry them across agent chat sessions.

Key insights:
\- false positives are very bad UX for this feature
\- manual evals (no framework, just a script)
\- tons of dogfooding internally (he builds the evals dataset manually)
\- Spent weeks iterating on prompts. Very model specific, and every word matters.
\- Pragmatic with a focus on simplicity and validation through dogfooding, rather than over-engineer and use complex frameworks.

Yash confirmed my impression of Cursor engineering: pragmatic, humble and curious.

2/8

![](https://pbs.twimg.com/media/Gt13rvzbwAEzNJO.jpg)

* * *

[New computer] [@sjwhitmore](<https://twitter.com/sjwhitmore>) is a legend in LLM memory. She gave what might have been the first talk on this topic at the AI eng summit a couple years back.

She's building [@newcomputer](<https://twitter.com/newcomputer>) \- a personal assistant that knows you really well. Memory is everything to them.

Key insights:

\- Perfect memory architecture doesn't exist. It's always approximating ground truth
\- The solution space is evolving fast as models get bigger contexts, faster throughput, more EQ, better attention
\- Different memory types (facts, procedures, worldview, relationships) each need different approaches for storage, deduplication, and retrieval

3/8

![](https://pbs.twimg.com/media/Gt145ngXcAAjG3m.jpg)![](https://pbs.twimg.com/media/Gt15GejXkAIVl8A.jpg)

* * *

[@NicoleHedley3](<https://twitter.com/NicoleHedley3>) is building Friday, a CLI agent that's similar (better?) to Claude Code.

She didn't have much time to dive deep, but mentioned they use an ensemble of models architecture.

Their challenge: ensuring different models can access and leverage memory from the task/codebase/user at the right time.

4/8

![](https://pbs.twimg.com/media/Gt16zr3WQAAgYq_.jpg)

* * *

[@LangChainAI](<https://twitter.com/LangChainAI>)'s [@WHinthorn](<https://twitter.com/WHinthorn>) presented LangMem, their new memory SDK extension.

Key lesson: building a generic memory solution that fits all use cases is incredibly hard. This was reinforced by other speakers describing their very unique architectures.

It's too early to have figured out the perfect abstraction, so they kept langmem simple and flexible - letting each use case implement it in flexible ways.

5/8

![](https://pbs.twimg.com/media/Gt17RMMaIAE_O_M.jpg)

* * *

My overall thoughts:

Memory feels very early.

Like [@sjwhitmore](<https://twitter.com/sjwhitmore>) said: it's evolved a ton in the last 12 months alone. Likely, this will continue.

Each application has very different requirements:
\- can they involve the user?
\- how bad is getting a memory wrong?
\- how should memories "expire"?
\- how should you retrieve memories? when?
\- what about context stuffing, over parsing memories and compressing them?

Tons of questions, still not a lot of answers.

However a lot of people are working on this (clearly), so I hope we get to hear more builders sharing their tips in the future @GregKamradt

6/8

* * *

Overall this was a special, and very "SF" event:

Full of talent, authentic and engaging talks from actual builders at the frontier.

My one thumbs down is that the langChain snacks bar is really disappointing [@hwchase17](<https://twitter.com/hwchase17>) pls fix

7/8

![](https://pbs.twimg.com/media/Gt19CFgWQAAai_9.jpg)

* * *

All this stuff is very top of mind for [@get_mocha](<https://twitter.com/get_mocha>) , we're introducing more and more features based on memory.

If you're building memory, i want to hear from you, how are you doing it? What framework are you using? What's your storage logic? retrieval logic?

In the future, AI products will know *you* and hyper-personalize to you. For that to work, we gotta build it.

Hearing how engineers are solving this today was a real treat.

8/8
