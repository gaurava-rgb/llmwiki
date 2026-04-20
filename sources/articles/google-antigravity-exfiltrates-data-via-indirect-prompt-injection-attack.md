---
title: "Google Antigravity exfiltrates data via indirect prompt injection attack"
reader_id: "01kb0ac4et217pd14b4w5nagrm"
notion_page_id: "3484ebe7-f118-812c-b19f-eb6c30858b27"
reader_url: "https://read.readwise.io/read/01kb0ac4et217pd14b4w5nagrm"
source_url: "https://news.ycombinator.com/item?id=46048996"
author: "jjmaxwell4"
site: "ycombinator.com"
tags: []
published: "2025-11-25"
saved_at: "2025-11-26"
reading_time: "6 mins"
summary: "A report describes how Google Antigravity (Gemini) was tricked into leaking private data via an indirect prompt injection. Attackers used open redirects and the browser subagent to exfiltrate files and credentials. Commenters warn this highlights a broader risk in agentic AI that mixes untrusted input, private data access, and external actions."
content_hash: "864a6b9e24dc9f10042ca4479331f31ec6a11213d826f259415b22dc4f6beceb"
---

# [jjmaxwell4](<https://news.ycombinator.com/user?id=jjmaxwell4>)

(2025-11-25 18:31:16)

## [wingmanjd](<https://news.ycombinator.com/user?id=wingmanjd>)

(2025-11-25 19:23:06)

I really liked Simon's Willison's [1] and Meta's [2] approach using the "Rule of Two". You can have no more than 2 of the following:

\- A) Process untrustworthy input \- B) Have access to private data \- C) Be able to change external state or communicate externally.

It's not bullet-proof, but it has helped communicate to my management that these tools have inherent risk when they hit all three categories above (and any combo of them, imho).

[EDIT] added "or communicate externally" to option C.

[1] [https://simonwillison.net/2025/Nov/2/new-prompt-injection-pa...](<https://simonwillison.net/2025/Nov/2/new-prompt-injection-papers/>) [2] <https://ai.meta.com/blog/practical-ai-agent-security/>

### [btown](<https://news.ycombinator.com/user?id=btown>)

(2025-11-25 20:40:00)

It's really vital to also point out that (C) doesn't just mean _agentically_ communicate externally - it extends to any situation where any of your users can even access the output of a chat or other generated text.

You might say "well, I'm running the output through a watchdog LLM before displaying to the user, and that watchdog doesn't have private data access and checks for anything nefarious."

But the problem is that the moment someone figures out how to prompt-inject a quine-like thing into a private-data-accessing system, such that it outputs another prompt injection, now you've got both (A) and (B) in your system as a whole.

Depending on your problem domain, you can mitigate this: if you're doing a classification problem and validate your outputs that way, there's not much opportunity for exfiltration (though perhaps some might see that as a challenge). But plaintext outputs are difficult to guard against.

#### [quuxplusone](<https://news.ycombinator.com/user?id=quuxplusone>)

(2025-11-25 21:55:59)

Can you elaborate? How does an attacker turn "any of your users can even access the output of a chat or other generated text" into a means of exfiltrating data _to the attacker_?

Are you just worried about social engineering — that is, if the attacker can make the LLM say "to complete registration, please paste the following hex code into evil.example.com:", then a large number of human users will just do that? I mean, you'd probably be right, but if that's "all" you mean, it'd be helpful to say so explicitly.

### [blcknight](<https://news.ycombinator.com/user?id=blcknight>)

(2025-11-26 03:08:02)

It baffles me that we've spent decades building great abstractions to isolate processes with containers and VM's, and we've mostly thrown it out the window with all these AI tools like Cursor, Antigravity, and Claude Code -- at least in their default configurations.

#### [otabdeveloper4](<https://news.ycombinator.com/user?id=otabdeveloper4>)

(2025-11-26 07:10:37)

Exfiltrating other people's code is the entire reason why "agentic AI" even exists as a business.

It's this decade's version of "they trust me, dumb fucks".

### [ArcHound](<https://news.ycombinator.com/user?id=ArcHound>)

(2025-11-25 19:26:58)

I recall that. In this case, you have only A and B and yet, all of your secrets are in the hands of an attacker.

It's great start, but not nearly enough.

EDIT: right, when we bundle state with external Comms, we have all three indeed. I missed that too.

#### [malisper](<https://news.ycombinator.com/user?id=malisper>)

(2025-11-25 19:40:14)

Not exactly. Step E in the blog post:

> Gemini exfiltrates the data via the browser subagent: Gemini invokes a browser subagent per the prompt injection, instructing the subagent to open the dangerous URL that contains the user's credentials.

fulfills the requirements for being able to change external state

#### [bartek_gdn](<https://news.ycombinator.com/user?id=bartek_gdn>)

(2025-11-25 19:44:28)

What do you mean? The last part in this case is also present, you can change external state by sending a request with the captured content.

## [simonw](<https://news.ycombinator.com/user?id=simonw>)

(2025-11-25 21:19:13)

More reports of similar vulnerabilities in Antigravity from Johann Rehberger: [https://embracethered.com/blog/posts/2025/security-keeps-goo...](<https://embracethered.com/blog/posts/2025/security-keeps-google-antigravity-grounded/>)

He links to this page on the Google vulnerability reporting program:

[https://bughunters.google.com/learn/invalid-reports/google-p...](<https://bughunters.google.com/learn/invalid-reports/google-products/4655949258227712/antigravity-known-issues>)

That page says that exfiltration attacks against the browser agent are "known issues" that are not eligible for reward (they are already working on fixes):

> Antigravity agent has access to files. While it is cautious in accessing sensitive files, there’s no enforcement. In addition, the agent is able to create and render markdown content. Thus, the agent can be influenced to leak data from files on the user's computer in maliciously constructed URLs rendered in Markdown or by other means.

And for code execution:

> Working with untrusted data can affect how the agent behaves. When source code, or any other processed content, contains untrusted input, Antigravity's agent can be influenced to execute commands. [...]

> Antigravity agent has permission to execute commands. While it is cautious when executing commands, it can be influenced to run malicious commands.

### [kccqzy](<https://news.ycombinator.com/user?id=kccqzy>)

(2025-11-25 22:27:21)

As much as I hate to say it, the fact that the attacks are “known issues” seems well known in the industry among people who care about security and LLMs. Even as an occasional reader of your blog (thank you for maintaining such an informative blog!), I know about the lethal trifecta and the exfiltration risks since early ChatGPT and Bard.

I have previously expressed my views on HN about removing one of the three lethal trifecta; it didn’t go anywhere. It just seems that at this phase, people are so excited about the new capabilities LLMs can unlock that they don’t care about security.

#### [TeMPOraL](<https://news.ycombinator.com/user?id=TeMPOraL>)

(2025-11-26 09:04:41)

I have a different perspective. The Trifecta is a _bad_ model because it makes people think this is just another cybersecurity challenge, solvable with careful engineering. But it's not.

It cannot be solved this way because it's a people problem - LLMs are like people, not like classical programs, and that's fundamental. That's what they're made to be, that's why they're useful. The problems we're discussing are variations of principal/agent problem, with LLM being the savant but extremely naive agent. There is no probable, verifiable solution here, not any more than when talking about human employees, contractors, friends.

#### [Helmut10001](<https://news.ycombinator.com/user?id=Helmut10001>)

(2025-11-26 06:44:40)

Then, the goal must be to guide users to run Antigravity in a sandbox, with only the data or information that it must access.

## [jsmith99](<https://news.ycombinator.com/user?id=jsmith99>)

(2025-11-25 19:15:43)

There's nothing specific to Gemini and Antigravity here. This is an issue for all agent coding tools with cli access. Personally I'm hesitant to allow mine (I use Cline personally) access to a web search MCP and I tend to give it only relatively trustworthy URLs.

### [ArcHound](<https://news.ycombinator.com/user?id=ArcHound>)

(2025-11-25 19:21:23)

For me the story is that Antigravity tried to prevent this with a domain whitelist and file restrictions.

They forgot about a service which enables arbitrary redirects, so the attackers used it.

And LLM itself used the system shell to pro-actively bypass the file protection.

### [dabockster](<https://news.ycombinator.com/user?id=dabockster>)

(2025-11-25 21:20:51)

> Personally I'm hesitant to allow mine (I use Cline personally) access to a web search MCP and I tend to give it only relatively trustworthy URLs.

Web search MCPs are generally fine. Whatever is facilitating tool use (whatever program is controlling both the AI model and MCP tool) is the real attack vector.

### [connor4312](<https://news.ycombinator.com/user?id=connor4312>)

(2025-11-25 22:03:35)

Copilot will prompt you before accessing untrusted URLs. It seems a crux of the vulnerability that the user didn't need to consent before hitting a url that was effectively an open redirect.

#### [simonw](<https://news.ycombinator.com/user?id=simonw>)

(2025-11-25 22:06:50)

Which Copilot?

Does it do that using its own web fetch tool or is it smart enough to spot if it's about to run `curl` or `wget` or `python -c "import urllib.request; print(urllib.request.urlopen('<https://www.example.com/').read>())"`?

There are more comments to this post:

  * <https://news.ycombinator.com/item?id=46049840>
  * <https://news.ycombinator.com/item?id=46049385>
  * <https://news.ycombinator.com/item?id=46050628>
  * <https://news.ycombinator.com/item?id=46049070>
  * <https://news.ycombinator.com/item?id=46050586>
  * <https://news.ycombinator.com/item?id=46049938>
  * <https://news.ycombinator.com/item?id=46049222>
  * <https://news.ycombinator.com/item?id=46050196>
  * <https://news.ycombinator.com/item?id=46049554>
  * <https://news.ycombinator.com/item?id=46049986>
  * <https://news.ycombinator.com/item?id=46050790>
  * <https://news.ycombinator.com/item?id=46054225>
  * <https://news.ycombinator.com/item?id=46049652>
  * <https://news.ycombinator.com/item?id=46051540>
  * <https://news.ycombinator.com/item?id=46056995>
  * <https://news.ycombinator.com/item?id=46050003>
  * <https://news.ycombinator.com/item?id=46051138>
  * <https://news.ycombinator.com/item?id=46056390>
  * <https://news.ycombinator.com/item?id=46049668>
  * <https://news.ycombinator.com/item?id=46049260>
  * <https://news.ycombinator.com/item?id=46053827>
  * <https://news.ycombinator.com/item?id=46049575>
  * <https://news.ycombinator.com/item?id=46049449>
  * <https://news.ycombinator.com/item?id=46049115>
  * <https://news.ycombinator.com/item?id=46049434>
  * <https://news.ycombinator.com/item?id=46050405>
  * <https://news.ycombinator.com/item?id=46050723>
  * <https://news.ycombinator.com/item?id=46049508>
  * <https://news.ycombinator.com/item?id=46049667>
  * <https://news.ycombinator.com/item?id=46050346>
  * <https://news.ycombinator.com/item?id=46050937>
  * <https://news.ycombinator.com/item?id=46051231>
  * <https://news.ycombinator.com/item?id=46054318>
  * <https://news.ycombinator.com/item?id=46050686>
  * <https://news.ycombinator.com/item?id=46053785>
  * <https://news.ycombinator.com/item?id=46049620>
  * <https://news.ycombinator.com/item?id=46052030>
  * <https://news.ycombinator.com/item?id=46050600>
  * <https://news.ycombinator.com/item?id=46049593>
  * <https://news.ycombinator.com/item?id=46056793>
  * <https://news.ycombinator.com/item?id=46049378>
  * <https://news.ycombinator.com/item?id=46053637>
  * <https://news.ycombinator.com/item?id=46049198>
  * <https://news.ycombinator.com/item?id=46051250>
