---
title: "The Game Theory Behind Prediction Markets."
reader_id: "01k50d07f3vzpdj7rphhk778bq"
notion_page_id: ""
category: "tweet"
source_type: "Reader Share Sheet iOS"
reader_url: "https://read.readwise.io/read/01k50d07f3vzpdj7rphhk778bq"
source_url: "https://x.com/baheet_/status/1965758390430208066/?s=12&rw_tt_thread=True"
author: "Baheet"
site: "X (formerly Twitter)"
tags: []
published: "2025-09-10"
saved_at: "2025-09-13"
reading_time: "8 mins"
summary: "Prediction markets use money and game theory so traders reveal their true beliefs. Rules like the LMSR cost function reward accurate bets and make honesty a dominant strategy. With liquidity, good incentive design, and tech (AI, oracles, blockchain) they can beat polls but must guard against manipulation."
content_hash: "24c7e4beb7307a7990ff55d1b2cc29626c65e4c1a70970d8d29783d0ea10fa99"
---

![The Game Theory Behind Prediction Markets.](https://pbs.twimg.com/media/G0ewmGsW0AA8SSd.jpg)

Prediction markets are a fascinating intersection of economics, human behavior and their desire to gamble on outcomes…

where bets on future events including elections, celebrity news , or even tech breakthroughs are turned into accurate forecasts.

Unlike polls or expert opinions, which rely on intuition or stated beliefs, prediction markets depend on financial incentives to draw out truth, harnessing the wisdom of crowds.

At the core of their design lies game theory; the study of strategic decision-making, which ensures that self-interested traders reveal their true knowledge through trades.

**TL;DR**

  * Game theory forms the basis of prediction markets
  * We can encourage honest participation in prediction markets through proper incentives alignment
  * The end goal of prediction markets is to give an accurate forecast
  * If you're building a prediction market you need a good economist and game theory expert on your team.
  * If you skipped your economics classes you might want to skip this one :)



This article dives into the basics of the game theory principles that powers prediction markets.

I will try to explore:

  * how incentives align with truth-telling,
  * why prediction markets are more efficient than polls
  * and personal takes on how to design markets that can withstand manipulation.



* * *

## The Game-Theoretic Foundation: Truth is the Dominant Strategy

Prediction markets work because they’re designed as games where the winning move is honesty.

They are basically a mechanism for information aggregation by pooling dispersed knowledge.

**But how does it reveal the true beliefs of traders?**

Game theory provides the answer through incentive compatibility.

In a well-designed market, revealing your true information about an event is a dominant strategy. Why?

It maximizes your payoff regardless of other traders’ actions.

Consider a trader with private info about the outcome of an election. If the market price for the event is priced at $0.60 (60%), the trader buys, expecting profit when the price corrects upward.

This simple move aligns the trader's personal gain with market accuracy, a concept that is well formalized in mechanism design.

This leads us to the LSMR.

## What is the Logarithmic Market Scoring Rule (LMSR)?

The LMSR is a mathematical tool used in prediction markets to price contracts and incentivize traders to reveal their true beliefs about the likelihood of future events (e.g., “Will Candidate X win?”).

It’s a type of proper scoring rule, meaning it’s designed so that a trader’s best strategy is to report their honest probability estimate, aligning with game theory’s concept of incentive compatibility.

In a prediction market, traders buy or sell shares tied to event outcomes.

The price of a share reflects the market’s collective probability (e.g., $0.60 per share implies a 60% chance).

The key tool here is using a proper scoring rule, (the LMSR).

In LMSR, the market maker’s cost function is:

C(Q) = b * log(∑ e^{q_i / b}),

Traders pay the cost difference to shift probabilities, incentivizing them to move prices toward their true own beliefs.

For example, pushing a price from 60% to 80% costs more if you’re wrong, so only confident traders act. This ensures an equilibrium, where each trader’s best move is to bet based on their honest assessment.

If you find the whole LSMR thingy too complex, I will try to break it down;

The LMSR basically ensures these prices adjust dynamically as traders act, rewarding those who move prices closer to the true probability.

**Breaking Down the LMSR Cost Function:**

_C(Q) = b * log(∑ e^{q_i / b})_

  * Q = {q_1, q_2, ..., q_n}: Represents the quantities of shares for each possible outcome (e.g., q_1 for “Candidate X wins,” q_2 for “Candidate X loses”).



If 100 shares are bought for “wins,” then q_1 = 100.

  * e^{q_i / b}: The exponential term converts the share quantities into a form that reflects market dynamics. It ensures that buying more shares for one outcome increases its implied probability.
  * ∑: Sums over all possible outcomes, ensuring the market accounts for all possibilities (e.g., win or lose in a binary market).
  * log: The natural logarithm smooths the function, making price changes gradual and manageable.
  * b: A positive constant that controls liquidity; how sensitive prices are to trades. A high b means prices move less with each trade (more liquid), while a low b means prices are more volatile (less liquid).
  * C(Q): The total cost the market maker charges to maintain the market’s state. It’s the price traders interact with indirectly.



Example:

  * An election market starts with 60% probability ($0.60 per share) for “X wins.”
  * A trader believes the true probability is 80% and buys shares to push the price to $0.80.
  * The LMSR computes the cost of the new share quantities (after buying) minus the old quantities. This cost depends on:

1\. How many shares are bought (changes q_i).

1\. The liquidity parameter b (affects price sensitivity).




If the trader’s belief (80%) is wrong, the cost of pushing the price up is high, and they risk losing money if the market corrects back down but If they’re right, they profit.

This cost structure punishes inaccurate bets and rewards accurate ones.

Only traders confident in their information will pay to shift prices significantly, ensuring the market always reflects informed beliefs.

This thread from @probabilitygod clearly explains how you can run a simple prediction markets using LSMR in binary markets outcome.

![](https://pbs.twimg.com/profile_images/1949751954520907776/ydOmAI3S.jpg)

[probability god](<https://twitter.com/probabilitygod>) [@probabilitygod](<https://twitter.com/probabilitygod>)

[ ](<https://twitter.com/probabilitygod/status/1965107369786163494>)

1/12

how to build a prediction market in 5 minutes using math from a 2016 microsoft article 🧵

(github python repo link in the last tweet)

![Image](https://pbs.twimg.com/media/G0Vy88FXkAAKDvD.jpg?name=orig)

[Posted Sep 8, 2025 at 5:38PM](<https://twitter.com/probabilitygod/status/1965107369786163494>)

## Why Prediction markets outperform Polls and expert forecasts

Game theory also explains why prediction markets often beat expert forecasts and traditional polls.

It's quite simple; **prediction markets amplify the influence of informed traders.**

In a market, participants range from noise traders (those betting on hunches) to informed ones (those with data or expertise).

The hypothesis here suggests that prices will reflect all available information but this hypothesis only assumes ideal conditions which do not always hold

**but game theory refines this:**

Informed traders dominate in thick markets (high trading volume), as their bets will always correct mispricings.

In a thick market, informed traders can place larger bets without drastically moving prices, allowing them to exploit mispricings (e.g., buying a contract at $0.50 when they know the true probability is 70%).

Their actions push prices toward accuracy.

**For Example:**

In an election market, if noise traders overvalue a candidate at $0.80 (80%) based on hype, informed traders with data showing a 60% chance are going to sell or short the contract, pushing the price down.

This corrects the market toward the true probability.

The Iowa Electronic Markets (IEM), running since 1988, consistently outperformed polls in election forecasting, as traders’ financial stakes sharpened their predictions.

![Image](https://pbs.twimg.com/media/G0e2-NmXsAAP3_B.jpg)

Also, @Polymarket's odds for Donald Trump's victory reached as high as 97% in the final days, proving more accurate than many polls.

![Image](https://pbs.twimg.com/media/G0e3pQ4WIAAm3kB.jpg)

This proves that Incentives outweigh intuition.

When money’s on the line, people naturally make the right actions.

## Core Problems in Prediction Markets

Despite their successes, prediction markets still face systemic hurdles that threaten their reliability and questions their scalability. The most pressing ones are

  * low liquidity
  * Manipulations and poor forecasts



## Using Incentive Design for Better Participation and Liquidity

Low liquidity in prediction markets arises as a result of misaligned incentives. When Prediction markets suffer from low liquidity, It basically means there aren’t enough traders or funds to keep the market active and stable.

This happens because traders see high risk in thin markets.

If only a few people are betting, a single large trade can affect the odds, making it less appealing to join.

**The Solution lies in Subsidizing Participation** ; the idea is to create incentives that make providing liquidity to the market attractive.

Subsidies should be structured to reward providers only if they maintain their capital in the market for a minimum period or meet specific conditions.

For example, a platform might offer a bonus on a $1,000 deposit, but only if the funds remain in the market for 30 days or are used in active trades.

This creates a repeated cycle where providers face a tradeoff: cash out early and lose the subsidy, or stay in for the reward, which aligns with providing liquidity.

The subsidy (reward) basically makes sustained participation a dominant strategy for liquidity providers.

Subsidies can also be tied to the impact of a provider’s contribution, such as increasing trading volume or stabilizing prices.

For instance, platforms might decide to reward providers whose trades improve price accuracy, ensuring their capital adds real liquidity rather than just inflating volume.

Polymarket uses this method to reward LPs in its order book for providing liquidity and stabilizing markets.

**How the Program Works**

  * Incentive: The primary goal is to encourage market liquidity by having users place limit orders, which allow for the immediate execution of market orders.
  * Reward Criteria: LPs are rewarded based on the competitiveness and usefulness of their limit orders.
  * Competitiveness: The closer an LP's limit order is to the market's average price (midpoint), the higher the reward.
  * Usefulness: The size of the order and its price level compared to other participants are also factored in. Orders that add depth without widening the spread are considered more helpful.

![Image](https://pbs.twimg.com/media/G0e9XzdWAAA1IZe.jpg)




This system helps maintain market stability by balancing the order book and reducing price slippage for traders. It also makes the market more difficult to manipulate.

## Preventing Manipulation in prediction markets

Manipulation in prediction markets occurs when big players (e.g., whales with large capital) place bets to distort odds for profit or influence, rather than reflecting their true beliefs about an outcome.

This can also happen in when they manipulate disputes outcomes like the case of polymarket and @UMAprotocol

The solution here is to design rules to make honest play the best strategy by using dominant strategy mechanisms and reputation penalties.

A dominant strategy mechanism ensures that honest play, betting based on your true belief about an outcome is always the best choice, no matter what other players do.

In game theory, a dominant strategy yields the highest payoff regardless of others’ actions, creating a stable equilibrium where manipulation isn’t worth it.

I already explained how using the LSMR enable platform to align traders bet with their honest beliefs,

Example: In a market on whether a climate policy passes, a whale bets $50,000 on “No” to push odds from 60% “Yes” to 40%.

If the policy passes, their bet loses, and the market’s scoring rule rewards honest “Yes” bettors more. The whale’s manipulation attempt fails because honest betting is the dominant strategy.

**Truth is the Schelling point**

A Schelling point in economics is a focal outcome where rational players naturally converge based on shared expectations.

In game theory, it’s a solution people choose when coordination is needed but an explicit agreement isn’t possible.

Example: If two strangers are told to meet in New York City without specifying a place or time, many will pick Times square at noon.. it’s a natural focal point.

In a well designed prediction market, a Schelling point is the “truth” (e.g., the actual outcome of an event) that honest participants agree on.

## Final Thoughts

Applying game theory designs to prediction markets transforms them from mere speculative platforms into better forecasting tools.

AI, oracles, blockchains, and dispute resolution systems enhance this foundation by making game-theoretic designs more practical and scalable

AI can help improve the quality of information and events in a prediction market and Blockchain choice will determine how scalable and accessible your platform is,

Imagine building your prediction platform on Etherem L1.

Oracles, integrate with external data and can adopt a decentralized voting system to verify outcomes in prediction markets and resolve disputes transparently.

Yet, while AI, oracles and other systems provide technical muscles, game theory remains the ultimate foundation, defining the rules that ensure incentives always align with truth and fairness.

Without it, even AI and oracles lack direction just like tools without a blueprint.

I believe these theories should form the basis of whatever prediction markets you are building.

I only explained how aligning incentives can promote truthfulness, aggregates information, and mitigates manipulations…. But this is only the surface level.

I'm not an economist or game theory expert myself, but I'm captivated by how these fields can impact the success of prediction markets.

## And that is awrap!

**Tagging relevant folks**

## @marvellousdefi_ , @0xNairolf , @factcheck1ntern , @_drNeyo , @iam_LeriK , @netrovertHQ , @PinnacleCrypt , @j0hnwang , @satyaki44 , @0xCheeezzyyyy , @0xwondr , @PixOnChain , @Defi0xJeff , @The_Tradeguru, @DeFiScribbler , @aulijk,

**Recommendations**

  1. [Game theory in economics](<https://www.theknowledgeacademy.com/blog/game-theory-in-economics/>)
  2. [General theory of liquidity provisioning in prediction markets](<https://arxiv.org/html/2311.08725v2>)
  3. [Ultimate guide to game theory](<https://www.investopedia.com/terms/g/gametheory.asp>)
