---
title: "The privacy nightmare of browser fingerprinting"
reader_id: "01kb0amp6qa6qa6pgawc72kj81"
notion_page_id: "3464ebe7-f118-8146-a4fc-cdd29695fb7f"
category: "article"
source_type: "Reader Share Sheet iOS"
reader_url: "https://read.readwise.io/read/01kb0amp6qa6qa6pgawc72kj81"
source_url: "https://news.ycombinator.com/item?id=46016249"
author: "ingve"
site: "ycombinator.com"
tags: []
published: "2025-11-22"
saved_at: "2025-11-26"
reading_time: "11 mins"
summary: "Browser settings like language choices can become persistent signals that uniquely identify you across sites. Fingerprinting is widespread and hard to avoid, used for ads, security, and state surveillance. Only broad adoption of privacy tools or systemic changes (e.g., Tor-like defaults or regulation) can reduce the risk."
content_hash: "5a1e87db1bb14963612b83902cc0ecd02e094bb192740b8c6a7d5c587d55f886"
---

# [ingve](<https://news.ycombinator.com/user?id=ingve>)

(2025-11-22 17:08:36)

## [aragonite](<https://news.ycombinator.com/user?id=aragonite>)

(2025-11-22 20:35:05)

Some time ago I noticed that in Chrome, every time you click "Never translate $language", $language quietly gets added to the Accept-Language header that Chrome sends to every website!

My header ended up looking like a permuted version of this:


      en-US,en;q=0.9,zh-CN;q=0.8,de;q=0.7,ja;q=0.6


I never manually configured any of those extra languages in the browser settings. All I had done was tell Chrome not to translate a few pages on some foreign news sites. Chrome then turned those one-off choices into persistent signals attached to every request.

I'd be surprised if anyone in my vicinity share my exact combination of languages in that exact order, so this seems like a pretty strong fingerprinting vector.

There was even a proposal to reduce this surface area, but it wasn't adopted:

[https://github.com/explainers-by-googlers/reduce-accept-lang...](<https://github.com/explainers-by-googlers/reduce-accept-language>)

### [zzo38computer](<https://news.ycombinator.com/user?id=zzo38computer>)

(2025-11-23 06:46:59)

This is a problem, that the software will try to guess what you mean by such things like this (it is not specific to this feature, but other features of computer programs in general; this is one specific case of that). Just because you do not want it to translate such a language (or any other langage) automatically does not necessarily mean that you can read it or that you want to request documents written in that language. Fingerprinting is not the only issue with this.

### [hoofedear](<https://news.ycombinator.com/user?id=hoofedear>)

(2025-11-22 20:38:18)

Is Chrome trying to assume that, since you don’t want it to translate those pages/languages, that you can read them/want them in your header? Interesting

#### [onion2k](<https://news.ycombinator.com/user?id=onion2k>)

(2025-11-23 16:07:09)

I'd read it more generously than that. I think Chrome trying to stop _the server_ choosing the language for you. By sending an accepts-language header (which your browser does regardless of what you use; it's not a Chrome thing) the server _should_ return the page in a language you've said you'll accept. By adding the language to what you've told Chrome not to translate, it's attempting to show you pages in languages you want.

I imagine Chrome is really adding the language to your browser preferences when you choose not to translate a page, and the HTTP client in the browser is generating request headers based on your preferred languages. A small (and largely unimportant) semantic point, but it's possible that the Google translate team weren't aware of how adding a preferred language might impact user privacy. That isn't to excuse the behaviour; they should have checked.

### [scrollop](<https://news.ycombinator.com/user?id=scrollop>)

(2025-11-22 20:58:39)

PSA Don't use chrome.

#### [faidit](<https://news.ycombinator.com/user?id=faidit>)

(2025-11-23 03:23:34)

Translating pages is literally the only thing I use Chrome for. The built-in translation works way better than other browsers, even though they also use Google Translate.

#### [unethical_ban](<https://news.ycombinator.com/user?id=unethical_ban>)

(2025-11-23 04:44:31)

PSA only use Mullvad or Tails which are set up to be as bland and uniform as possible

#### [SV_BubbleTime](<https://news.ycombinator.com/user?id=SV_BubbleTime>)

(2025-11-22 21:01:32)

Definitely a good STEP1, but it’s not like Firefox and Safari are finger printing secure.

## [tzury](<https://news.ycombinator.com/user?id=tzury>)

(2025-11-23 10:02:25)

The OP argues that fingerprinting is a "privacy nightmare," but we need to look at why it exists.

From a pragmatic perspective, we are forcing two very different networks to run on the same protocols:

_The Business Internet:_ Banking, SaaS, and VC-funded content (Meta/Google).

_The Fun Internet:_ Hobby blogs, Lego fan sites, and the "GeoCities" spirit.

You cannot have a functioning "Business Internet" without identity verification. If you try to perform a transaction (or even just use a subsidized "free" tool like Gmail) while hiding behind a generic, non-unique fingerprint, you look indistinguishable from a bot or a fraudster.

Fingerprinting is often just the immune system of the commercial web trying to verify you are human.

The friction arises because we expect the "Fun Internet" to play by different rules. A Lego fan site shouldn't need to know who I am. But because we access both the Lego site and our Bank using the same browser, the same IP, and the same free tools (Chrome/Search), the "Fun Internet" becomes collateral damage of the "Business Internet's" need for security and monetization.

We can't have it both ways. We accepted the SLA for the "Business Internet" in exchange for free, billion-dollar tools. If you want 100% anonymity, you are effectively asking to use the commercial web's infrastructure without providing the identity signal it runs on.

As the OP notes, mitigation is hard. But that’s not just because advertisers are "evil"—it's because on the modern web, anonymity looks exactly like a security threat.

### [flossposse](<https://news.ycombinator.com/user?id=flossposse>)

(2025-11-23 22:58:17)

> You cannot have a functioning "Business Internet" without identity verification.

Yes, you can. Just like you can have a functioning grocery store without checking the identity of each shopper that walks through the door.

What you cannot have is a free and democratic society or an efficient free market without robust protections for individual privacy. Privacy is the best shield the less powerful have from being abused and exploited by the more powerful.

> We accepted the SLA for the "Business Internet" in exchange for free, billion-dollar tools.

No, we did not accept. There was no informed consent. The full consequences of our use of these services was and is still is kept hidden from us. Tracking happens invisibly, without our knowledge or consent. This deprives us of the opportunity to express our true preference and opt out and choose an alternative. It's employing deception in order to subvert the consumer's ability to make a rational choice that represents their best interests.

> on the modern web, anonymity looks exactly like a security threat

An anonymous user who just uses the service normally and does not attempt to access sensitive information without authorization does not look like a security threat.

#### [overflow897](<https://news.ycombinator.com/user?id=overflow897>)

(2025-11-24 12:31:23)

Most grocery stores in every place I have lived have security cameras so that if you did something illegal you'd be identified very quickly. At this point this is even true of small bodegas.

Also scammers can't waltz into my grocery store from the other side of the planet and wreak havoc.

Ultimately you can use privacy enhancing tools, just like servers can choose to block them. I wish there was a better system but that's what we've got.

### [everdrive](<https://news.ycombinator.com/user?id=everdrive>)

(2025-11-23 11:03:04)

Then let's get rid of the business internet. Every single thing I dislike about the internet is from the business internet: tracking, cookies, fingerprinting, SPAs, excessive javascript, optimizing for engagement, data brokers, I could go on.

"But won't you miss XYZ?" Nope, don't care, want it gone. If you can't be bothered to go to the store and get it then it probably didn't matter very much.

#### [lurking_swe](<https://news.ycombinator.com/user?id=lurking_swe>)

(2025-11-23 19:39:42)

Based on your comment it sounds like you rarely travel (booking hotel / flights online), don’t have mobility issues (ordering groceries / household essentials online), don’t participate in online banking (do you write checks? carry cash with you all the time? go to an ATM weekly?), you don’t stream movies or tv shows, and you enjoy looking for apartments to rent in your local newspaper listing, and you enjoy using paper maps when traveling around the city and world. I could go on…

literally everything useful works on the business internet. Also how do you think local businesses near you operate? They don’t call each like the 1900s lol. They order stock from distributors, some local and some overseas. Often they are doing this on the business internet. Today’s global supply chain makes this a non-starter.

It’s OK if YOU personally prefer doing everything slowly and in person and don’t value the convenience of the business internet. No judgment. But don’t pretend this would be an easy transition at all. Or that most people would prefer to live that way.

IMO it would make _way_ more sense to introduce reasonable privacy regulations that are better thought out than GDPR and have proper enforcement.

Maybe a formal “community” version of the internet would be appropriate as well.

#### [nilslindemann](<https://news.ycombinator.com/user?id=nilslindemann>)

(2025-11-23 11:51:12)

To me, it would be enough if there existed a search engine which only lists sites which do nothing of the above. But that would require that sites are honestly answering the question "are you tracking?". They won't. Corps have the same thinking as the criminals they try to keep outside.

There would have to be laws which require site owners to answer that question honestly, so that users have a choice and such a search engine can be built. But states are interested in fingerprinting too, so I guess such will never happen.

#### [zymhan](<https://news.ycombinator.com/user?id=zymhan>)

(2025-11-23 19:38:18)

Those are some rose tinted glasses. Not having to drive a check to the city utility office to pay the power bill is quite the improvement.

### [johannes1234321](<https://news.ycombinator.com/user?id=johannes1234321>)

(2025-11-23 11:11:38)

No. Fingerprinting is a function of the ad network to identify ad-worth aspects of me.

That some aspects may be used to push bots away is a minor effect.

#### [tzury](<https://news.ycombinator.com/user?id=tzury>)

(2025-11-23 15:00:30)

I am assuming you are not in the bot mitigation business.

An encrypted cookie from a company such as cloudflare encapsulates a multi dimensional datum such that, generating one in a legitimate browser, and letting a botnet using it will get detected and blocked.

## [drnick1](<https://news.ycombinator.com/user?id=drnick1>)

(2025-11-22 18:14:15)

Firefox w/ the Arkenfox user.js is probably as good as it gets in terms of privacy. By default, this config burns cookies on exit, standardizes the time zone to UTC, spoofs the canvas fingerprint, and does other helpful things. Basically, it makes Firefox expose the same information as the Tor browser.

In addition, I block most known advertizing/tracking domains at the DNS level (I run my own server, and use Hagezi's blacklists).

Finally, another suggestion would be to block all third party content by default using uBlock Origin and/or uMatrix. This will break a lot of websites, but automatically rules out most forms of tracking through things such as fonts hosted by Google, Adobe and others. I manually whitelist required third party domains (CDNs) for websites I frequently visit.

### [samtheprogram](<https://news.ycombinator.com/user?id=samtheprogram>)

(2025-11-22 22:12:20)

There's no point unless a critical mass of people use these tools. You will be the only one on your IP address using this configuration of masked fingerprinting, which is itself a fingerprint.

That's also why it's indeed useful when using Tor, because you're not identified by your base IP.

Unless we make this part of the culture, you have basically 0 recourse to browser fingerprinting except using Tor. Which can itself still be a useful fingerprint depending on the context.

EDIT: I'll add that using these tools outside of normal browsing use can be useful for obfuscating who's doing specific browsing, but it should be emphasized that using fingerprinting masking in isolation all the time is nearly as useful as not using them at all.

#### [thrw888](<https://news.ycombinator.com/user?id=thrw888>)

(2025-11-23 16:20:10)

I have packed ff with arkenfox js into container and maybe a handful other people use it <https://github.com/grzegorzk/ff_in_podman>. Still, most likely the IP address alone is probably the strongest part of fingerprint vector Maybe instead it would be better to have very different vector each time?

#### [cortesoft](<https://news.ycombinator.com/user?id=cortesoft>)

(2025-11-22 23:21:23)

Basically the XKCD license plate comic: <https://xkcd.com/1105/>

#### [DavideNL](<https://news.ycombinator.com/user?id=DavideNL>)

(2025-11-23 17:18:13)

> "_There's no point unless a critical mass of people use these tools_ "

That's what Mullvad Browser attempts to solve i guess:

<https://mullvad.net/en/browser>

### [codedokode](<https://news.ycombinator.com/user?id=codedokode>)

(2025-11-22 18:23:17)

Does it hide GPU name that is exposed via WebGL/WebGPU? Does it hide internal IP address, available via WebRTC?

> block all third party content

It's not going to work, because the fingerprinting script can be (and is often served) from first-party domain.

Also imagine if browser didn't provide drawing API for canvas (if you would have to ship your own wasm rendering library). Canvas would become useless for fingerprinting and its usage would drop manyfold. And the browser would have less code and smaller attack surface.

#### [drnick1](<https://news.ycombinator.com/user?id=drnick1>)

(2025-11-22 18:31:15)

> Does it hide GPU name that is exposed via WebGL/WebGPU? Does it hide internal IP address, available via WebRTC?

My GPU is reported as simply "Mozilla" by <https://abrahamjuliot.github.io/creepjs/>.

The number of cores is also set to 4 for everyone using this config and/or Tor.

> It's not going to work, because the fingerprinting script can be (and is often served) from first-party domain.

This may be true, but allowed third party content makes it trivially easy for Google and others to follow people around the Internet through fonts delivery systems among others.

#### [dminuoso](<https://news.ycombinator.com/user?id=dminuoso>)

(2025-11-22 18:39:12)

If I infiltrate someone else’s computer, secretly run code in order to to exfiltrate data I risk prison time because objectively it seems to satisfy criminal laws over where I live.

How do prosecutors in any modern country/state not charge this behavior when done by a website owner?

### [0xy](<https://news.ycombinator.com/user?id=0xy>)

(2025-11-22 19:52:51)

As someone who utilizes these tools for anti-fraud purposes, Firefox is just as trackable if not more trackable than Chrome (especially because you stand out by using a niche browser in the first place).

Firefox exposes a massive amount of identifiable information via canvas, audio device and feature detection methods. There's also active methods to detect private windows, use of the developer console and more.

#### [vpShane](<https://news.ycombinator.com/user?id=vpShane>)

(2025-11-22 20:08:56)

Of course. There's data where there isn't data.

-make client load something

-client doesn't load it

-add.fingerprint.point(client,'doesnltloadthings',1)

-detect if client does something only a certain browser does

-client does it

-add.fingerprint.point(client,'doesthisbrowsderthing',1)

-window was resized/moved, send a websocket snitch to the backend

\- keep a consistent web socket open, or fetch a backend-api call for updates on X events \- more calls are made, means user is probably scrolling, inject more things/different things.

I see some js obfuscators out there where I look at the js file and it's all mumbo jumbo.

It is indeed a privacy nightmare, where whatever we do feeds the algorithms to aide in making other people do things.

But it's also used in network security, organizations etc. Staff/employees will use the system a certain way, if something enters it without the behaviors, it's detectable. I assume that's what you mean in anti-fraud.

Sad part is we don't know what the data is ever used for, and it's often bought and sold and the cycle repeats.

#### [pteraspidomorph](<https://news.ycombinator.com/user?id=pteraspidomorph>)

(2025-11-23 07:31:07)

If you enable privacy.resistFingerprinting in about:config I believe instead of trying to prevent fingerprinting entirely, it's supposed to make things annoying for the fingerprinters by regularly changing the various spoofed factors.

There are more comments to this post:

  * <https://news.ycombinator.com/item?id=46019206>
  * <https://news.ycombinator.com/item?id=46016474>
  * <https://news.ycombinator.com/item?id=46016786>
  * <https://news.ycombinator.com/item?id=46017814>
  * <https://news.ycombinator.com/item?id=46017603>
  * <https://news.ycombinator.com/item?id=46016755>
  * <https://news.ycombinator.com/item?id=46019675>
  * <https://news.ycombinator.com/item?id=46017125>
  * <https://news.ycombinator.com/item?id=46022964>
  * <https://news.ycombinator.com/item?id=46018112>
  * <https://news.ycombinator.com/item?id=46016434>
  * <https://news.ycombinator.com/item?id=46016955>
  * <https://news.ycombinator.com/item?id=46017259>
  * <https://news.ycombinator.com/item?id=46018219>
  * <https://news.ycombinator.com/item?id=46017136>
  * <https://news.ycombinator.com/item?id=46023605>
  * <https://news.ycombinator.com/item?id=46023272>
  * <https://news.ycombinator.com/item?id=46020655>
  * <https://news.ycombinator.com/item?id=46022466>
  * <https://news.ycombinator.com/item?id=46019152>
  * <https://news.ycombinator.com/item?id=46016404>
  * <https://news.ycombinator.com/item?id=46018174>
  * <https://news.ycombinator.com/item?id=46018021>
  * <https://news.ycombinator.com/item?id=46017526>
  * <https://news.ycombinator.com/item?id=46023281>
  * <https://news.ycombinator.com/item?id=46021752>
  * <https://news.ycombinator.com/item?id=46016562>
  * <https://news.ycombinator.com/item?id=46021410>
  * <https://news.ycombinator.com/item?id=46023177>
  * <https://news.ycombinator.com/item?id=46019558>
  * <https://news.ycombinator.com/item?id=46019473>
  * <https://news.ycombinator.com/item?id=46016592>
  * <https://news.ycombinator.com/item?id=46017519>
  * <https://news.ycombinator.com/item?id=46017079>
  * <https://news.ycombinator.com/item?id=46018089>
  * <https://news.ycombinator.com/item?id=46022191>
  * <https://news.ycombinator.com/item?id=46026302>
  * <https://news.ycombinator.com/item?id=46018419>
  * <https://news.ycombinator.com/item?id=46017521>
  * <https://news.ycombinator.com/item?id=46016459>
  * <https://news.ycombinator.com/item?id=46016746>
  * <https://news.ycombinator.com/item?id=46016517>
  * <https://news.ycombinator.com/item?id=46016696>
  * <https://news.ycombinator.com/item?id=46017282>
  * <https://news.ycombinator.com/item?id=46016764>
  * <https://news.ycombinator.com/item?id=46019933>
  * <https://news.ycombinator.com/item?id=46016585>
  * <https://news.ycombinator.com/item?id=46016859>
  * <https://news.ycombinator.com/item?id=46021901>
  * <https://news.ycombinator.com/item?id=46022215>
  * <https://news.ycombinator.com/item?id=46024121>
  * <https://news.ycombinator.com/item?id=46017356>
  * <https://news.ycombinator.com/item?id=46020457>
  * <https://news.ycombinator.com/item?id=46017218>
  * <https://news.ycombinator.com/item?id=46021448>
  * <https://news.ycombinator.com/item?id=46016655>
  * <https://news.ycombinator.com/item?id=46019405>
  * <https://news.ycombinator.com/item?id=46017189>
  * <https://news.ycombinator.com/item?id=46017387>
  * <https://news.ycombinator.com/item?id=46018673>
