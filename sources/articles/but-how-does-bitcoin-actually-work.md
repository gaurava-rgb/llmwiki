---
title: "But how does bitcoin actually work?"
reader_id: "01jyx4q29xb33yvaafsvf8fk41"
notion_page_id: ""
category: "video"
source_type: "Wisereads discovery"
reader_url: "https://read.readwise.io/read/01jyx4q29xb33yvaafsvf8fk41"
source_url: "https://www.youtube.com/watch?v=bBC-nXj3Ng4"
author: "3Blue1Brown"
site: "YouTube"
tags: []
published: "2017-07-07"
saved_at: "2025-06-29"
reading_time: ""
summary: "Bitcoin is a digital currency that uses a communal ledger and cryptography to verify transactions without needing a central authority. Transactions are secured with digital signatures, and miners validate and add them to the blockchain, which is a public record of all transactions. New bitcoins are created as rewards for miners who help maintain the integrity of the system."
content_hash: "376e7a9beffaff1c3908c19d21c1d837992f98ddb62630d98fc13ec62351c4a2"
---

What does it mean to have a Bitcoin?Many people have heard of Bitcoin, that it's a fully digital currencywith no government to issue it, that no banks need to manage accountsand verify transactions, and that no one really knows who invented it.And yet many people don't know the answer to this question, at least not in full.To get there, and to make sure that the technical details underlyingthe answer actually feel motivated, we're going to walk through,step by step, how you might have invented your own version of Bitcoin.

We'll start with you keeping track of payments with your friends using a communal ledger,and then as you start to trust your friends and the world around you less and less,and if you're clever enough to bring in a few ideas from cryptography to help circumventthe need for trust, what you end up with is what's called a cryptocurrency.Bitcoin is just the first implemented example of a cryptocurrency,and now there are thousands more on exchanges with traditional currencies.Walking the path of inventing your own can help to set the foundationsfor understanding some of the more recent players in the game,and recognizing when and why there's room for different design choices.

In fact, one of the reasons I chose this topic is that in the last year there'sbeen a huge amount of attention, investment, and hype directed at these currencies.I'm not going to comment or speculate on the current or future exchange rates,but I think we'd all agree that anyone looking to buy a cryptocurrency should reallyknow what it is.And I don't just mean in terms of analogies with vague connections to gold mining,I mean an actual direct description of what the computers are doing when we send,receive, and create cryptocurrencies.One thing worth stressing is that even though you and I are going to dig into thedetails here, and that takes meaningful time,you don't actually need to know those details if you just want to use thecryptocurrency, just like you don't need to know the details of what happensunder the hood when you swipe a credit card.

Like any digital payment, there are lots of user-friendly applications that letyou just send and receive the currencies without thinking about what's going on.The difference is that the backbone underlying this is not a bank thatverifies transactions; instead, it's a clever system of decentralizedtrustless verification based on some of the math born in cryptography.

But to start, I want you to actually set aside the thoughtof cryptocurrencies and all that just for a few minutes.We’re going to begin the story with something more down to earth,ledgers and digital signatures.If you and your friends exchange money pretty frequently,paying your share of the dinner bill and such,it can be inconvenient to exchange cash all the time.

So you might keep a communal ledger that records all thepayments you intend to make at some point in the future.Alice pays Bob $20, Bob pays Charlie $40, things like that.This ledger is going to be something public and accessible to everyone,like a website where anyone can go and add new lines.

And let’s say at the end of every month you all get together,look at the list of transactions, and settle up.If you spent more than you received, you put that money in the pot,and if you received more than you spent, you take that money out.

So the protocol for being part of this very simple system might look like this:Anyone can add lines to the ledger, and at the endof every month you all get together and settle up.Now, one problem with a public ledger like this is that anyone can add a line.So what's to prevent Bob from going and writingAlice pays Bob $100 without Alice approving?How are we supposed to trust that all of thesetransactions are what the sender meant them to be?Well, this is where the first bit of cryptography comes in: digital signatures.

Like handwritten signatures, the idea here is that Alice should be able to addsomething next to that transaction that proves that she has seen it and that she'sapproved of it, and it should be infeasible for anyone else to forge that signature.At first, it might seem like a digital signature shouldn't even be possible.I mean, whatever data makes up that signature can just be read and copied by a computer.So how do you prevent forgeries?Well, the way this works is that everyone generates what's called a publickey-private key pair, each of which looks like some string of bits.The private key is sometimes also called a secret key,so we can abbreviate it as SK while abbreviating the public key as PK.As the name suggests, this secret key is something you want to keep to yourself.

In the real world, your handwritten signature looksthe same no matter what document you're signing.But a digital signature is actually much stronger,because it changes for different messages.It looks like some string of 1s and 0s, commonly something like 256 bits,and altering the message even slightly completely changes whatthe signature on that message should look like.Speaking a little more formally, producing a signature involves afunction that depends both on the message itself and on your private key.

The private key ensures that only you can produce that signature,and the fact that it depends on the message means that no one canjust copy one of your signatures and forge it on another message.Hand in hand with this is a second function used to verify that a signature is valid,and this is where the public key comes into play.All it does is output true or false to indicate if this was a signature producedby the private key associated with the public key you're using for verification.

I won't go into the details of how exactly both these functions work,but the idea is that it should be completely infeasible tofind a valid signature if you don't know the secret key.

Specifically, there's no strategy better than just guessing and checking randomsignatures, which you can check using the public key that everyone knows.Now, think about how many signatures there are with a length of 256 bits.That's 2 to the power of 256!This is a stupidly large number.To call it astronomically large would be giving way too much credit to astronomy.In fact, I made a supplemental video devoted justto illustrating what a huge number this is.

Right here, let's just say that when you verify that a signature against a given messageis valid, you can feel extremely confident that the only way someone could have producedit is if they knew the secret key associated with the public key you used forverification.Making sure people sign transactions on the ledger is pretty good,but there's one slight loophole.

If Alice signs a transaction like Alice pays Bob $100,even though Bob can't forge Alice's signature on a new message,he could just copy that same line as many times as he wants.I mean, that message-signature combination remains valid.To get around this, we make it so that when you sign a transaction,the message has to include some sort of unique ID associated with that transaction.

That way, if Alice pays Bob $100 multiple times,each one of those lines on the ledger requires a completely new signature.Alright, great. Digital signatures remove a huge aspect of trust in this initial protocol.But even still, if you were to really do this,you would be relying on an honor system of sorts.Namely, you're trusting that everyone will actually followthrough and settle up in cash at the end of each month.

What if, for example, Charlie racks up thousandsof dollars in debt and just refuses to show up?The only real reason to revert back to cash to settle up is if some people,I'm looking at you, Charlie. You owe a lot of money.

So maybe you have the clever idea that you never actually have to settle up in cash aslong as you have some way to prevent people from spending too much more than they takein.Maybe you start by having everyone pay $100 into the pot,and then have the first few lines of the ledger read: Alice gets $100, Bob gets $100,Charlie gets $100, etc.Now, just don’t accept any transactions where someoneis spending more than they already have on that ledger.For example, if the first two transactions are Charlie pays Alice $50and Charlie pays Bob $50, if he would have tried to add Charlie pays you $20,that would be invalid, as invalid as if he had never signed it.

Notice, this means verifying a transaction requiresknowing the full history of transactions up to that point.This is also going to be true in cryptocurrencies,though there is a little room for optimization.What’s interesting here is that this step removes theconnection between the ledger and actual physical US dollars.In theory, if everyone in the world was using this ledger,you could live your whole life just sending and receiving moneyon this ledger without ever having to convert to real US dollars.

In fact, to emphasize this point, let’s start referring to thequantities on the ledger as ledger dollars, or LD for short.You are, of course, free to exchange ledger dollars for real US dollars.For example, maybe Alice gives Bob a $10 bill in the real world in exchange for himadding and signing the transaction, "$10 Bob pays Alice $10," to this communal ledger.But exchanges like that are not guaranteed by the protocol.

It’s now more analogous to how you might exchange dollarsfor Euros or any other currency on the open market.It’s just its own independent thing.

This is the first important thing to understand about Bitcoin,or any other cryptocurrency.What it is, is a ledger.The history of transactions is the currency.Of course, with Bitcoin, money doesn’t enter the ledger with people buying in using cash.I’ll get to how new money enters the ledger in just a few minutes.

But before that, there’s actually an even more significant differencebetween our current system of ledger dollars and how cryptocurrencies work.So far, I’ve said that this ledger is in some public place,like a website where anyone can add new lines.But that would require trusting a central location, namely,who hosts the website, who controls the rules of adding new lines.

To remove that bit of trust, we’ll have everybody keep their own copy of the ledger.Then when you want to make a transaction, like Alice pays Bob 100 Ledger Dollars,what you do is broadcast that out into the world for people tohear and record on their own private ledgers.But unless you do something more, this system is absurdly bad.

How could you get everyone to agree on what the right ledger is?When Bob receives a transaction, like Alice pays Bob 10 Ledger Dollars,how can he be sure that everyone else received and believes that same transaction?That he’ll be able to later on go to Charlie and usethose same 10 Ledger Dollars to make a transaction?

Really, imagine yourself just listening to transactions being broadcast.How can you be sure that everyone else is recordingthe same transactions and in the same order?This is really the heart of the issue.This is an interesting puzzle.Can you come up with a protocol for how to accept or reject transactions,and in what order, so that you can feel confident that anyone else in the worldwho’s following that same protocol has a personal ledger that looks the same as yours?

This is the problem addressed in the original Bitcoin paper.At a high level, the solution that Bitcoin offers is to trustwhichever ledger has the most computational work put into it.I'll take a moment to explain exactly what that means.It involves this thing called a cryptographic hash function.The general idea that we'll build to is that if you use computational work as abasis for what to trust, you can make it so that fraudulent transactions andconflicting ledgers would require an infeasible amount of computation to bring about.Again, I'll remind you that this is getting well into the weeds beyondwhat anyone would need to know just to use a currency like this.But it's a really cool idea, and if you understand it,you understand the heart of Bitcoin and other cryptocurrencies.

So first things first, what's a hash function?The inputs for one of these functions can be any kind of message or file,it really doesn't matter. And the output is a string of bitswith some kind of fixed length, like 256 bits.This output is called the hash or digest of the message,and the intent is that it looks random.It's not random; it always gives the same output for a given input.

But the idea is that if you slightly change the input,maybe editing just one of the characters, the resulting hash changes completely.In fact, for the hash function I'm showing here, called SHA256,the way the output changes as you slightly change that input is entirely unpredictable.You see, this is not just any hash function; it's a cryptographic hash function.That means it's infeasible to compute in the reverse direction.If I show you some string of 1s and 0s, and ask you to find an inputso that the SHA256 hash of that input gives this exact string of bits,you will have no better method than to just guess and check.

And again, if you want to feel for how much computation would be needed togo through two to the 256 guesses, just take a look at the supplement video.

I actually had way too much fun writing that thing.You might think that if you just really dig into the details of how exactly this functionworks, you could reverse engineer the appropriate input without having to guess andcheck.But no one has ever figured out a way to do that.Interestingly, there’s no cold hard rigorous proofthat it's hard to compute in the reverse direction.And yet, a huge amount of modern security depends on cryptographichash functions and the idea that they have this property.If you were to look at what algorithms underlie the secure connectionthat your browser is making with YouTube right now,or that it makes with your bank, you’ll likely see the name SHA256 show up in there.For right now, our focus will be on how such a function can prove that a particularlist of transactions is associated with a large amount of computational effort.

Imagine someone shows you a list of transactions, and they say, "Hey,I found a special number so that when you put that number at the end of this list oftransactions, and apply SHA256 to the entire thing,the first 30 bits of that output are all zeros."How hard do you think it was for them to find that number?Well, for a random message, the probability that a hash happens to startwith 30 successive zeros is 1 in 2 to the 30, which is about 1 in a billion.And because SHA256 is a cryptographic hash function,the only way to find a special number like that is just guessing and checking.So this person almost certainly had to go through about abillion different numbers before finding this special one.

And once you know that number, it's really quick to verify;you just run the hash and see that there are 30 zeros.So in other words, you can verify that they went through a large amount of work,but without having to go through that same effort yourself.This is called a proof of work.

And importantly, all of this work is intrinsically tied to the list of transactions.If you change one of those transactions, even slightly,it would completely change the hash.So you’d have to go through another billion guesses to find a new proof of work,a new number that makes it so that the hash of the altered listtogether with this new number starts with 30 zeros.

So now think back to our distributed ledger situation.Everyone is there broadcasting transactions and we wanta way for them to agree on what the correct ledger is.As I mentioned, the idea behind the original Bitcoin paper is tohave everyone trust whichever ledger has the most work put into it.

The way this works is to first organize a given ledger into blocks,where each block consists of a list of transactions together with a proof of work.That is, a special number so that the hash ofthe whole block starts with a bunch of zeros.For the moment, let’s say it has to start with 60 zeros,but later we’ll return back to a more systematic way you might want to choosethat number.

In the same way that a transaction is only considered valid whenit’s signed by the sender,a block is only considered valid if it has a proof of work.Also, to make sure there’s a standard order to these blocks,we’ll make it so that a block has to contain the hash of the previous blockat its header.

That way, if you were to go back and change any one of the blocks,or to swap the order of two blocks, it would change the block that comes after it,which changes that block's hash, which changes the one that comes after it, and so on.

That would require redoing all of the work, finding a new special numberfor each of these blocks that makes their hashes start with 60 zeros.Because blocks are chained together like this,instead of calling it a ledger, it’s common to call it a blockchain.

As part of our updated protocol, we'll now allowanyone in the world to be a block creator.What that means is that they're going to listen for transactions being broadcast,collect them into some block, and then do a whole bunch of work to find aspecial number that makes the hash of that block start with 60 zeros.Once they find it, they broadcast out the block they found.

To reward a block creator for all this work, when she puts together a block,we'll allow her to include a very special transaction at the top of it,in which she gets, say, 10 ledger dollars out of thin air.This is called the block reward, and it's an exception toour usual rules about whether or not to accept transactions.It doesn't come from anyone, so it doesn't have to be signed.

It also means that the total number of ledgerdollars in our economy increases with each new block.Creating blocks is often called mining, since it requires doing a lot of work,and it introduces new bits of currency into the economy.But when you hear or read about miners, keep in mind that what they'rereally doing is listening for transactions, creating blocks,broadcasting those blocks, and getting rewarded with new money for doing so.

From the miners' perspective, each block is like a miniature lottery,where everyone is guessing numbers as fast as they can,until one lucky individual finds a special number that makes the hash of the blockstart with many zeros, and they get the reward.

For anyone else who just wants to use this system to make payments,instead of listening for transactions, they all start listening just for blocksbeing broadcast by miners, and updating their own personal copies of the blockchain.Now the key addition to our protocol is that if you hear twodistinct blockchains with conflicting transaction histories,you defer to the longest one, the one with the most work put into it.If there's a tie, just wait until you hear anAn additional block makes one of them longer.

So even though there's no central authority, and everyone is maintaining their owncopy of the blockchain, if everyone agrees to give preference to whichever blockchainhas the most work put into it, we have a way to arrive at decentralized consensus.

To see why this makes for a trustworthy systemand to understand at what point you should trust that a payment is legit,it's actually really helpful to walk through exactly what it would take tofool someone using this system.Maybe Alice is trying to fool Bob with a fraudulent block;namely, she tries to send him one that includes her paying him 100 Ledger dollars,but without broadcasting that block to the rest of the network.That way, everyone else still thinks she has those 100 Ledger dollars.

To do this, she would have to find a valid proof of work before all the other miners,each working on their own block.And that could definitely happen; maybe Alice just happensto win this miniature lottery before everyone else.

But Bob is still going to be hearing the broadcasts made by other miners,so to keep him believing this fraudulent block,Alice would have to do all the work herself to keep adding blocks on thisspecial fork in Bob's blockchain that's different from what he's hearingfrom the rest of the miners.

Remember, as per the protocol, Bob always trusts the longest chain he knows about.Alice might be able to keep this up for a few blocks if just by chance she findsblocks more quickly than the rest of the miners on the network all combined.

But unless she has close to 50% of the computing resources among all of the miners,the probability becomes overwhelming that the blockchain that all the other minersare working on grows faster than the single fraudulent blockchain Alice is feeding toBob.So after enough time, Bob will just reject what he's hearing fromAlice in favor of the longer chain that everyone else is working on.

Notice, that means you shouldn't necessarily trust a new block you hear immediately.Instead, you should wait for several new blocks to be added on top of it.If you still haven't heard of any longer blockchains,you can trust that this block is part of the same chain that everyone else is using.

And with that, we've hit all the main ideas.This distributed ledger system based on a proof of work is more or lesshow the Bitcoin protocol works, and how many other cryptocurrencies work.There's just a few details to clear up.Earlier I said that the proof of work might be to find a specialnumber so that the hash of the block starts with 60 zeros.Well, the way the actual Bitcoin protocol works is to periodically change thatnumber of zeros so that it should take, on average, 10 minutes to find a new block.

So as there are more and more miners added to the network,the challenge gets harder and harder in such a way that thisminiature lottery only has about one winner every 10 minutes.Many newer cryptocurrencies have much shorter block times than that.And all of the money in Bitcoin ultimately comes from some block reward.In the beginning, these rewards were 50 Bitcoin per block.There's actually a great website you can go to called BlockExplorer that makes it easy to look through the Bitcoin blockchain.

And if you look at the very first few blocks on the chain,they contain no transactions other than that 50 Bitcoin reward to the miner.But every 210,000 blocks, which is about every 4 years, that reward gets cut in half.So right now, the reward is 12.5 Bitcoin per block.And because this reward decreases geometrically over time,it means there will never be more than 21 million Bitcoin in existence.

However, this doesn't mean miners will stop earning money.In addition to the block reward, miners can also pick up transaction fees.The way this works is that whenever you make a payment,you can purely optionally include a transaction fee with it.

That will go to the miner of whichever block includes that payment.The reason you might do that is to incentivize miners to actuallyinclude the transaction you broadcast into the next block.You see, in Bitcoin, each block is limited to about 2,400 transactions,which many critics argue is unnecessarily restrictive.For comparison, Visa processes an average of about 1,700 transactions per second,and they’re capable of handling more than 24,000 per second.This comparatively slow processing on Bitcoin makes for higher transaction fees,since that’s what determines which transactions miners choose to include in a new block.

All of this is far from a comprehensive coverage of cryptocurrencies.There are still many nuances and alternate design choices that I haven't even touched.But my hope is that this can provide a stable WaitButWhy-style tree-trunk ofunderstanding for anyone looking to add a few more branches with further reading.

Like I said at the start, one of the motives behind this is that a lot of money hasstarted flowing towards cryptocurrencies, and even though I don't want to make anyclaims about whether that's a good or bad investment,I really do think it's healthy for people getting into the game to at least know thefundamentals of the technology.

As always, my sincerest thanks to those of you making this channel possible on Patreon.I understand that not everyone is in a position to contribute,but if you're still interested in helping out,one of the best ways to do that is simply to share videos that you thinkmight be interesting or helpful to others.I know you know that, but it really does help.
