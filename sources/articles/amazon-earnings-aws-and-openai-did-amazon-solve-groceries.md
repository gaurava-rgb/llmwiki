---
title: "Amazon Earnings, AWS and OpenAI, Did Amazon Solve Groceries?"
reader_id: "01k98067000kxpb2q21dv9d5wr"
notion_page_id: "3484ebe7-f118-8117-818c-fa38d5df0ac1"
category: "rss"
source_type: "Reader RSS"
reader_url: "https://read.readwise.io/read/01k98067000kxpb2q21dv9d5wr"
source_url: "https://stratechery.com/2025/amazon-earnings-aws-and-openai-did-amazon-solve-groceries/"
author: "Ben Thompson"
site: "Stratechery by Ben Thompson"
tags: []
published: "2025-11-04"
saved_at: "2025-11-04"
reading_time: "9 mins"
summary: "Amazon says the constraint right now is power, not chips; it's giving plenty of the latter to OpenAI. Then, Amazon solves groceries by getting faster tat delivering everything else."
content_hash: "cc92146963a65b46755577a9f18d77521687bc0915287f2193d5f002722f74d2"
---

Amazon says the constraint right now is power, not chips; it's giving plenty of the latter to OpenAI. Then, Amazon solves groceries by getting faster tat delivering everything else.

* * *

[Listen to this Update in your podcast player](<https://stratechery.passport.online/>)

* * *

Good morning,

Jon at [Asianometry](<https://asianometry.passport.online/>) has [a new video](<https://www.youtube.com/watch?v=vkx2zIanSpc>) out about TSMC’s curvy masks, a new innovation in its upcoming 2nm process.

On to the Update:

### Amazon Earnings

From the [Wall Street Journal](<https://www.wsj.com/business/earnings/amazon-amzn-q3-earnings-report-2025-553e6d16>):

> Seen as a laggard in artificial intelligence, Amazon.com assuaged some concerns Thursday, reporting faster-than-expected increases in AI-related revenue and aggressive plans to grow data-center capacity. The e-commerce giant said sales for the period rose 13%, to $180 billion. Net profit surged 39% to $21.2 billion. Amazon shares gained more than 10% in after-hours trading.
>
> Revenue from Amazon Web Services, the source of much of the company’s profits, climbed 20% in the three-month period—the fastest rate of growth since 2022. Rivals Alphabet and Microsoft said Wednesday that their cloud-computing businesses grew 40% and 34%, respectively. On a call with analysts, Chief Executive Andy Jassy noted that Amazon’s growth was from a much higher base.

Amazon, like the other big hyperscalers, has said repeatedly that demand outpaces supply; what was notable on [the earnings call](<https://seekingalpha.com/article/4835958-amazon-com-inc-amzn-q3-2025-earnings-call-transcript>) was where Jassy said the shortage was. First, from his opening remarks:

> Because of its advantaged capabilities, security, operational performance and customer focus, AWS continues to earn most of the big enterprise and government transformations to the cloud. As a result, AWS is where the preponderance of company’s data and workloads reside and part of why most companies want to run AI and AWS. To enable customers to do so, we need to have the requisite capacity, and we’ve been focused on accelerating capacity the last several months, adding more than 3.8 gigawatts of power in the past 12 months, more than any other cloud provider.
>
> To put that into perspective, we’re now double the power capacity that AWS was in 2022, and we’re on track to double again by 2027. In the last quarter of this year alone, we expect to add at least another 1 gigawatt of power. This capacity consists of power, data center and chips, primarily our custom silicon, Trainium and Nvidia.

Note the emphasis on power; Jassy later said in response to an analyst question:

> On the capacity side, we brought in quite a bit of capacity, as I mentioned in my opening comments, 3.8 gigawatts of capacity in the last year with another gigawatt plus coming in the fourth quarter and we expect to double our overall capacity by the end of 2027. So we’re bringing in quite a bit of capacity today, overall in the industry, maybe the bottleneck is power. I think at some point, it may move to chips, but we’re bringing in quite a bit of capacity. And as fast as we’re bringing in right now, we are monetizing it.

This is very interesting, as it is the opposite of how I was thinking about it: my assumption was that chips were in short supply, and the power shortage was looming; Jassy is saying it is actually the opposite. I’m not completely surprised about the power part, to be clear; I do think it’s notable that Jassy doesn’t consider access to chips a limiter. He added in response to another question about Trainium:

> We’re always going to have multiple chip options for our customers. It’s been true in every major technology building block or component that we’ve had in AWS. Really in the history of AWS, it’s never just one player that over a long period of time has the entire market segment and then it can satisfy everybody’s needs on every dimension. And so we have a very deep relationship with Nvidia. We have for a very long time. And we will for as long as I can foresee the future. We buy a lot of Nvidia. We are not constrained in any way in buying Nvidia, and I expect that we’ll continue to buy more Nvidia both next year and in the future.

I will add that, to the extent this is true, it’s a good thing for the long-term effects of the AI bubble. One of the biggest questions I’ve had is what is the durable capital good that is being built that wouldn’t be built otherwise, a la railroads or fiber? My hope has been that the answer is power generation — chips don’t count, given their limited lifespan — and if we are already in the phase where capacity and expansion plans are measured on earnings calls in gigawatts then that speaks to the most powerful incentive possible to build something that will be truly enduring and essential to the future.

### AWS and OpenAI

Meanwhile, more evidence of Amazon’s plentiful access to Nvidia chips came yesterday. From [CNBC](<https://www.cnbc.com/2025/11/03/open-ai-amazon-aws-cloud-deal.html>):

> OpenAI has signed a deal to buy $38 billion worth of capacity from Amazon Web Services, its first contract with the leader in cloud infrastructure and the latest sign that the $500 billion artificial intelligence startup is no longer reliant on Microsoft. Under the agreement announced on Monday, OpenAI will immediately begin running workloads on AWS infrastructure, tapping hundreds of thousands of Nvidia’s graphics processing units (GPUs) in the U.S., with plans to expand capacity in the coming years. Amazon stock closed 4% higher on Monday, a record closing high for the stock. The e-commerce giant is up 14% over the last two trading days, the best two-day period since Nov 2022.
>
> The first phase of the deal will use existing AWS data centers, and Amazon will eventually build out additional infrastructure for OpenAI. “It’s completely separate capacity that we’re putting down,” said Dave Brown, vice president of compute and machine learning services at AWS, in an interview. “Some of that capacity is already available, and OpenAI is making use of that.”

This is — and yes, this is a crazy thing to say — a pretty small deal, at least in OpenAI terms. The company has a $300 billion deal with Oracle, and a $250 billion deal with Microsoft, as well as an undisclosed cloud deal with Google. I suspect the Google deal is the closest analogy to this deal, in that the key differentiating factor is time: OpenAI is going to use AWS capacity right now.

That, however, raises what is to my mind the biggest oddity of this announcement: did AWS just have a bunch of unused Nvidia instances lying around, and if so what does that say about AI demand outside of OpenAI?

I think the answer is probably in the last paragraph of that excerpt, and in Jassy’s comments above: Amazon is in the process of bringing online a bunch of new capacity, and letting OpenAI jump the line; you can certainly see why the company would do that given the now customary OpenAI stock bump. OpenAI, meanwhile, continues to diversify its supply base on one hand, and tie another tech giant to its fate. Oh, and actually get some more capacity right now, not at some unknown point in the future.

### Did Amazon Solve Groceries?

I noted above that GPUs are not long-lasting capital assets; you might even say they are perishable. However, maybe the most interesting takeaway from Amazon’s earnings call, at least in terms of old Stratechery Articles, was about true perishables: groceries. First, from Jassy’s prepared remarks:

> Everyday Essentials continues to grow quickly, and year-to-date is growing nearly twice as fast as the rest of the business. We continue to make it easier for customers to order low-priced perishable groceries from Amazon, and customers in more than 1,000 cities and towns now can shop fresh groceries alongside millions of Amazon.com products with free same-day delivery. This is a game changer for customers who can now order milk alongside electronics, check out with one cart and have everything delivered to their doorstep within hours.

CFO Brian Olsavsky added in his prepared remarks:

> By leveraging our existing infrastructure, we’re now offering U.S. customers the ability to order perishable groceries and receive them the same day in as little as 5 hours. We’re seeing positive early results since launching in January, when customers start shopping fresh groceries on Amazon, they are visiting the site more often and returning twice as often as nonperishable shoppers.

This led to a very thought-provoking question from analyst Mark Mahaney:

> I think last quarter, you talked about 70% or something of users had never purchased from perishables from Amazon before. I think you used the term, game changer, before. Does this mean that maybe you no longer need Amazon Fresh stores? You always had this delivery and density advantage. And have you kind of reached a point you think of scale and speed that you really can change people’s habit and really have them consider Amazon as one of their first grocery options? Do you really feel like you’re at that point?

Jassy said nice things about Amazon’s other grocery efforts, like its non-perishable business, Whole Foods, etc., but didn’t really disagree with Mahaney’s argument; in fact, he argued that Amazon was benefiting from — and helping to drive — a fundamental shift in consumer behavior:

> The one that we are most excited about is what you referenced, which is the ability to provide perishable groceries with same-day deliveries. And if you think about how many of our customers are buying from us multiple times a week and who are buying things like shampoo or detergent or paper cups or water, where the ability to add milk and eggs and yogurt and other perishables to their order and have it live in the same shop in cart and then show up a few hours later, is very compelling.
>
> We started with a few markets about a year ago, and we were really taken aback at the adoption, not just the number of people that started buying perishables from us very quickly, but how often they came back downstream to buy perishables and groceries from us in the future. And so we’ve now expanded that to 1,000 cities around the U.S. and will be in 2,300 by the end of the year. And it’s really changing the trajectory and the size of our grocery business.
>
> And I also believe that this many year’s tradition of the weekly stock up grocery stock up is changing. And I think we’re a big part of that. And I think there’s a lot of potential there for the grocery side. It doesn’t mean that we won’t continue to experiment with other physical formats, but we’re on to something very significant with what we’re doing with perishables from our same-day facilities.

One of the most popular Articles ever on Stratechery was after Amazon bought Whole Foods; I wrote in [Amazon’s New Customer](<https://stratechery.com/2017/amazons-new-customer/>):

> This is the key to understanding the purchase of Whole Foods: from the outside it may seem that Amazon is buying a retailer. The truth, though, is that Amazon is buying a customer — the first-and-best customer that will instantly bring its grocery efforts to scale.
>
> Today, all of the logistics that go into a Whole Foods store are for the purpose of stocking physical shelves: the entire operation is integrated. What I expect Amazon to do over the next few years is transform the Whole Foods supply chain into a service architecture based on primitives: meat, fruit, vegetables, baked goods, non-perishables (Whole Foods’ outsized reliance on store brands is something that I’m sure was very attractive to Amazon). What will make this massive investment worth it, though, is that there will be a guaranteed customer: Whole Foods Markets.

Well, here we are nearly a decade later, and Amazon appears to finally be succeeding in perishable grocery delivery — and I think my explanation as to how Whole Foods would enable that was completely wrong. I haven’t seen any evidence that Amazon’s increased ability to deliver perishable goods — which are a massive challenge, given the fact they go bad — has to do with modularizing the Whole Foods supply chain. Rather, Amazon relentlessly invested in and improved its overall logistics capabilities such that a whole host of items now arrive same day; that, it turns out, is the key prerequisite for selling perishable goods online.

This seems so obvious in retrospect: instead of building a specialized grocery delivery network, make your network so fast that groceries slot in along with everything else! I don’t feel bad for not considering the possibility back in 2017 though; it only cost me an Article. Buying Whole Foods cost Amazon $13.7 billion (back when that was real money!).

* * *

This Update will be available as a podcast later today. To receive it in your podcast player, [visit Stratechery](<https://stratechery.passport.online/>).

The Stratechery Update is intended for a single recipient, but occasional forwarding is totally fine! If you would like to order multiple subscriptions for your team with a group discount (minimum 5), please contact me directly.

Thanks for being a subscriber, and have a great day!

* * *

Add to your podcast player: [Stratechery](<https://stratechery.passport.online/>) | [Sharp Tech](<https://sharptech.fm/>) | [Dithering](<https://dithering.passport.online/>) | [Sharp China](<https://sharpchina.fm/>) | [GOAT](<https://goat.passport.online/>) | [Asianometry](<https://asianometry.passport.online/>)

* * *

Subscription Information
[Manage your account](<https://stratechery.passport.online/>)
