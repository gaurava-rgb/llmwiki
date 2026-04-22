---
title: "How DoorDash uses AI Models to Understand Restaurant Menus"
reader_id: "01k4t7smgn4ke41b0njjm7zsrb"
notion_page_id: ""
category: "email"
source_type: ""
reader_url: "https://read.readwise.io/read/01k4t7smgn4ke41b0njjm7zsrb"
source_url: "mailto:reader-forwarded-email/892082a7b2485c1ad02e092f0de63cdb"
author: "ByteByteGo"
site: "Substack"
tags: []
published: "2025-09-10"
saved_at: "2025-09-10"
reading_time: "8 mins"
summary: "DoorDash uses OCR, large language models, and multimodal models to turn menu photos into structured digital menus.  \nA guardrail model checks image quality, OCR output, and LLM results to decide whether to publish automatically or route to a human.  \nThe hybrid system boosts automation while keeping accuracy and can improve with fine-tuning and better photo preprocessing."
content_hash: "0d30bb64f6592dc9d85400164009072d120da15bddb0ed4c06d180faa5d12613"
---

Forwarded this email? [ Subscribe here ](<https://substack.com/redirect/2/eyJlIjoiaHR0cHM6Ly9ibG9nLmJ5dGVieXRlZ28uY29tL3N1YnNjcmliZT91dG1fc291cmNlPWVtYWlsJnV0bV9jYW1wYWlnbj1lbWFpbC1zdWJzY3JpYmUmcj0zOGp3diZuZXh0PWh0dHBzJTNBJTJGJTJGYmxvZy5ieXRlYnl0ZWdvLmNvbSUyRnAlMkZob3ctZG9vcmRhc2gtdXNlcy1haS1tb2RlbHMtdG8tdW5kZXJzdGFuZCIsInAiOjE3Mjg4OTk5MSwicyI6ODE3MTMyLCJmIjp0cnVlLCJ1Ijo1NDM3OTAzLCJpYXQiOjE3NTc1MTg3MDcsImV4cCI6MjA3MzA5NDcwNywiaXNzIjoicHViLTAiLCJzdWIiOiJsaW5rLXJlZGlyZWN0In0.EQnm-4Ofk4_OSMw0cWlnSCTtJumTTYBkzzPbe5CZIAE?>) for more

#  [ How DoorDash uses AI Models to Understand Restaurant Menus ](<https://substack.com/app-link/post?publication_id=817132&post_id=172889991&isFreemail=true&r=38jwv>)

[ ByteByteGo ](<https://substack.com/@bytebytego399569>)

Sep 10

[ ![](https://substackcdn.com/image/fetch/$s_!U1Ej!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc9941c68-e5b7-4b93-be75-df7cc4ffef02_504x540.png) ](<https://substack.com/@bytebytego399569>)

[ ![](https://substackcdn.com/image/fetch/$s_!PeVs!,w_36,c_scale,f_png,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Ficon%2FLucideHeart%3Fv%3D4%26height%3D36%26fill%3Dnone%26stroke%3D%2523808080%26strokeWidth%3D2) ](<https://substack.com/app-link/post?publication_id=817132&post_id=172889991&isFreemail=true&submitLike=true&r=38jwv>)

[ ![](https://substackcdn.com/image/fetch/$s_!x1tS!,w_36,c_scale,f_png,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Ficon%2FLucideComments%3Fv%3D4%26height%3D36%26fill%3Dnone%26stroke%3D%2523808080%26strokeWidth%3D2) ](<https://substack.com/app-link/post?publication_id=817132&post_id=172889991&isFreemail=true&comments=true&r=38jwv&action=post-comment>)

[ ![](https://substackcdn.com/image/fetch/$s_!_L14!,w_36,c_scale,f_png,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Ficon%2FLucideShare2%3Fv%3D4%26height%3D36%26fill%3Dnone%26stroke%3D%2523808080%26strokeWidth%3D2) ](<https://substack.com/app-link/post?publication_id=817132&post_id=172889991&action=share&triggerShare=true&isFreemail=true&r=38jwv>)

[ ![](https://substackcdn.com/image/fetch/$s_!5EGt!,w_36,c_scale,f_png,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Ficon%2FNoteForwardIcon%3Fv%3D4%26height%3D36%26fill%3Dnone%26stroke%3D%2523808080%26strokeWidth%3D2) ](<https://substack.com/redirect/2/eyJlIjoiaHR0cHM6Ly9vcGVuLnN1YnN0YWNrLmNvbS9wdWIvYnl0ZWJ5dGVnby9wL2hvdy1kb29yZGFzaC11c2VzLWFpLW1vZGVscy10by11bmRlcnN0YW5kP3V0bV9zb3VyY2U9c3Vic3RhY2smdXRtX21lZGl1bT1lbWFpbCZ1dG1fY2FtcGFpZ249ZW1haWwtcmVzdGFjay1jb21tZW50JmFjdGlvbj1yZXN0YWNrLWNvbW1lbnQmcj0zOGp3diZ0b2tlbj1leUoxYzJWeVgybGtJam8xTkRNM09UQXpMQ0p3YjNOMFgybGtJam94TnpJNE9EazVPVEVzSW1saGRDSTZNVGMxTnpVeE9EY3dOeXdpWlhod0lqb3hOell3TVRFd056QTNMQ0pwYzNNaU9pSndkV0l0T0RFM01UTXlJaXdpYzNWaUlqb2ljRzl6ZEMxeVpXRmpkR2x2YmlKOS41cDhrUmQ5dzBGQzVJSDNLQlpQOThuQXhtbURwd3R3cy1Fcjh1bkFTeXpZIiwicCI6MTcyODg5OTkxLCJzIjo4MTcxMzIsImYiOnRydWUsInUiOjU0Mzc5MDMsImlhdCI6MTc1NzUxODcwNywiZXhwIjoyMDczMDk0NzA3LCJpc3MiOiJwdWItMCIsInN1YiI6ImxpbmstcmVkaXJlY3QifQ.cvtY4B-Om44p3I0l7SNDs8s6Q26qE1cYhsWaSaK2NJM>)

[ READ IN APP ![](https://substackcdn.com/image/fetch/$s_!ET-_!,w_36,c_scale,f_png,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Ficon%2FLucideArrowUpRight%3Fv%3D4%26height%3D36%26fill%3Dnone%26stroke%3D%2523808080%26strokeWidth%3D2) ](<https://open.substack.com/pub/bytebytego/p/how-doordash-uses-ai-models-to-understand?redirect=app-store>)

##  [ Make tribal knowledge self-serve (Sponsored) ](<https://substack.com/redirect/76691614-40bd-48bf-8384-384375621466?j=eyJ1IjoiMzhqd3YifQ.5A9UDKbxtmTMpf48aHOFTZVvvXtwbwJ-khjaPLWh8tA>)

[ ![](https://substackcdn.com/image/fetch/$s_!hLDS!,w_1100,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fda6fb6e6-bacd-43f6-8ca8-1e97180d224b_1999x1050.heic) ](<https://substack.com/redirect/76691614-40bd-48bf-8384-384375621466?j=eyJ1IjoiMzhqd3YifQ.5A9UDKbxtmTMpf48aHOFTZVvvXtwbwJ-khjaPLWh8tA>)

Cut onboarding time, reduce interruptions, and ship faster by surfacing the knowledge locked across GitHub, Slack, Jira, and Confluence (and more). You get:

  * Instant answers to questions about your architecture, past workarounds, and current projects.
  * An MCP Server that supercharges Claude and Cursor with your team knowledge so they generate code that makes sense in your codebase.
  * Agent that posts root cause and fix suggestions for CI failures directly in your Pull Request.
  * A virtual member of your team that automates internal support without extra overhead.



[ Check out Unblocked ](<https://substack.com/redirect/c392bcb2-f692-4631-bfb0-dbce2e3431c6?j=eyJ1IjoiMzhqd3YifQ.5A9UDKbxtmTMpf48aHOFTZVvvXtwbwJ-khjaPLWh8tA>)

* * *

_Disclaimer: The details in this post have been derived from the official documentation shared online by the DoorDash Engineering Team. All credit for the technical details goes to the DoorDash Engineering Team. The links to the original articles and sources are present in the references section at the end of the post. We’ve attempted to analyze the details and provide our input about them. If you find any inaccuracies or omissions, please leave a comment, and we will do our best to fix them._

When we order food online, the last thing we want is an out-of-date or inaccurate menu.

However, for delivery platforms, keeping menus fresh is a never-ending challenge. Restaurants constantly update items, prices, and specials, and doing all of this manually at scale is costly and slow.

DoorDash tackled this problem by applying large language models (LLMs) to automate the process of turning restaurant menu photos into structured, usable data. The technical goal of their project was clear: achieve accurate transcription of menu photos into structured menu data while keeping latency and cost low enough for production at scale.

On the surface, the idea is straightforward: take a photo, run it through AI, and get back a clean digital menu. In practice, though, the messy reality of real-world images (cropped photos, poor lighting, cluttered layouts) quickly exposes the limitations of LLMs on their own.

But the key insight was that LLMs, while strong at summarization and organization, break down when faced with noisy or incomplete inputs. To overcome this, DoorDash designed a system with guardrails. These are mechanisms that decide when automation is reliable enough to use and when a human needs to step in.

In this article, we will look at how DoorDash designed such a system and the challenges they faced.

[ ![](https://substackcdn.com/image/fetch/$s_!kzBG!,w_1100,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0c8d65bd-e9e5-48d7-8526-036c42cd7899_1647x1999.heic) ](<https://substack.com/redirect/c98c40fc-b4c6-451d-9327-7814076fc08e?j=eyJ1IjoiMzhqd3YifQ.5A9UDKbxtmTMpf48aHOFTZVvvXtwbwJ-khjaPLWh8tA>)

##  Baseline MVP

The first step was to prove whether menus could be digitized at all in an automated way.

The engineering team started with a simple pipeline: OCR to LLM. The OCR system extracted raw text from menu photos, and then a large language model was tasked with converting that text into a structured schema of categories, items, and attributes.

[ ![](https://substackcdn.com/image/fetch/$s_!pmVv!,w_1100,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F051cafa2-71b4-4248-a93a-e0fc1ba69bb9_1600x895.heic) ](<https://substack.com/redirect/32a87299-1d6e-47c6-b1ac-8a07962b4418?j=eyJ1IjoiMzhqd3YifQ.5A9UDKbxtmTMpf48aHOFTZVvvXtwbwJ-khjaPLWh8tA>)

Source: [ DoorDash Engineering Blog ](<https://substack.com/redirect/d6618f95-2453-4bc0-bd02-2cb7f915a1e4?j=eyJ1IjoiMzhqd3YifQ.5A9UDKbxtmTMpf48aHOFTZVvvXtwbwJ-khjaPLWh8tA>)

This approach worked well enough as a prototype.

It showed that a machine could, in principle, take a photo of a menu and output something resembling a digital menu. But once the system was tested at scale, cracks began to appear. Accuracy suffered in ways that were too consistent to ignore.

The main reasons were as follows:

  * **Inconsistent menu structures:** Real-world menus are not neatly ordered lists. Some are multi-column, others use mixed fonts, and many scatter categories and items in unpredictable ways. OCR tools often scramble the reading order, which means the LLM ends up pairing items with the wrong attributes or misplacing categories entirely.
  * **Incomplete menus:** Photos are often cropped or partial, capturing only sections of a menu. When the LLM receives attributes without their parent items, or items without their descriptions, it makes guesses. These guesses lead to mismatches and incorrect entries in the structured output.
  * **Low photographic quality:** Many menu photos are taken in dim lighting, with glare from glass frames or clutter in the background. Small fonts and angled shots add to the noise. Poor image quality reduces OCR accuracy, and the errors cascade into the LLM stage, degrading the final transcription.



Through human evaluation, the team found that nearly all transcription failures could be traced back to one of these three buckets.

* * *

##  [ The Gold standard for AI news (Sponsored) ](<https://substack.com/redirect/8ddf6183-b3b6-4106-9d50-71c20dc0b07e?j=eyJ1IjoiMzhqd3YifQ.5A9UDKbxtmTMpf48aHOFTZVvvXtwbwJ-khjaPLWh8tA>)

AI is the most essential technical skill of this decade.

CEOs of GitHub, Box, and others are prioritising hiring engineers with AI skills.

Engineers, devs, and technical leaders at Fortune 1000s + leading Silicon Valley startups read Superhuman AI to stay ahead of the curve and future-proof their skills.

[ Join 1M+ pros ](<https://substack.com/redirect/8ddf6183-b3b6-4106-9d50-71c20dc0b07e?j=eyJ1IjoiMzhqd3YifQ.5A9UDKbxtmTMpf48aHOFTZVvvXtwbwJ-khjaPLWh8tA>)

* * *

##  LLM Guardrail Model

To solve the accuracy problem, the engineering team introduced what they call a guardrail model.

At its core, this is a classifier that predicts whether the transcription produced from a given menu photo will meet the accuracy bar required for production. The logic is straightforward:

  * If the guardrail predicts that the output is good enough, the structured menu data is automatically published.
  * If the guardrail predicts a likely failure, the photo is routed to a human for transcription.



Building the guardrail meant more than just looking at the image.

The team realized the model needed to understand how the photo, the OCR system, and the LLM all interacted with each other. So they engineered features from three different sources:

  * **Image-level features:** These capture the quality of the photo itself, whether it is dark, blurry, has glare, or is cluttered with background objects.
  * **OCR-derived features:** These measure the reliability of the text extraction, such as how orderly the tokens are, whether confidence scores are high, or if the system has produced fragments and junk text.
  * **LLM-output features:** These reflect the quality of the structured transcription, such as how internally consistent the categories and attributes are, or whether the coverage looks incomplete.



This multi-view approach directly targets the three failure modes identified earlier: inconsistent menu structure, incomplete menus, and poor photographic quality.

By combining signals from the image, the OCR process, and the LLM itself, the guardrail learns to separate high-confidence transcriptions from those that are likely to go wrong.

##  Guardrail Model Training and Performance

Designing the guardrail model opened up the question of which architecture would actually work best in practice.

The team experimented with a three-component neural network design that looked like this:

  * **Image encoding:** The raw menu photo was passed through a pretrained vision backbone. They tried CNN-based models like VGG16 and ResNet, as well as transformer-based models such as ViT (Vision Transformer) and DiT (Document Image Transformer).
  * **Tabular features:** Alongside the image encoding, the network ingested features derived from the OCR output and the LLM transcription.
  * **Fusion and classification:** These inputs were combined through fully connected layers, ending in a classifier head that predicted whether a transcription was accurate enough.



The diagram below illustrates this design: an image model on one side, OCR/LLM tabular features on the other, both feeding into dense layers and then merging into a final classifier. It’s a standard multimodal fusion approach designed to capture signals from multiple sources simultaneously.

[ ![](https://substackcdn.com/image/fetch/$s_!9x7Y!,w_1100,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F70398ea0-7304-4bd5-aa00-77c22805afef_1999x1297.heic) ](<https://substack.com/redirect/3f1ae544-3a37-4d57-b0d8-416ca7b28ca9?j=eyJ1IjoiMzhqd3YifQ.5A9UDKbxtmTMpf48aHOFTZVvvXtwbwJ-khjaPLWh8tA>)

The results, however, were surprising.

Despite the sophistication of the neural network, the simplest model (LightGBM: a gradient-boosted decision tree) outperformed all the deep learning variants.

LightGBM not only achieved higher accuracy but also ran faster, which made it far more suitable for production deployment. Among the neural network variants, ResNet-based encoding came closest, while ViT-based models performed worst. The main reason was data: limited labeled samples made it difficult for the more complex architectures to shine.

##  Production Pipeline

Once the guardrail model was in place, the team built a full production pipeline that balanced automation with human review. It works step by step:

  * **Photo validation:** Every submitted menu photo goes through basic checks to ensure the file is usable.
  * **Transcription stage:** The candidate model (initially the OCR + LLM pipeline) generates a structured transcription from the photo.
  * **Guardrail inference:** Features from the photo, OCR output, and LLM summary are fed into the guardrail model, which predicts whether the transcription meets accuracy requirements.
  * **Routing decisions:** If the guardrail predicts the transcription is accurate, the structured data is published automatically. If the guardrail predicts likely errors, the photo is escalated to human transcription.



The diagram below shows this pipeline as a flow: menu photos enter, pass through the transcription model, then are evaluated by the guardrail. From there, accurate cases flow directly into the system, while uncertain ones branch off toward human operators.

[ ![](https://substackcdn.com/image/fetch/$s_!QnTC!,w_1100,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc9af8ffd-02c1-4d34-95bf-18a41079c802_1999x1287.heic) ](<https://substack.com/redirect/50b27938-1860-4695-997b-44b88b3d688c?j=eyJ1IjoiMzhqd3YifQ.5A9UDKbxtmTMpf48aHOFTZVvvXtwbwJ-khjaPLWh8tA>)

This setup immediately raised efficiency. Machines handled the straightforward cases quickly, while humans focused their effort on the difficult menus. The result was a balanced process: automation sped up operations and cut costs without lowering the quality of the final menu data.

##  Rapid Evolution with Multimodal GenAI

The pace of AI research did not stand still. In the months after the first guardrail model went live, multimodal LLMs (models that could process both images and text directly) became practical enough to try in production. Instead of relying only on OCR to extract text, these models could look at the raw photo and infer structure directly.

The DoorDash engineering team integrated these multimodal models alongside the existing OCR + LLM pipeline. Each approach had clear strengths and weaknesses:

  * Multimodal LLMs proved excellent at understanding context and layout. They could better interpret menus with unusual designs, multi-column layouts, or visual cues that OCR often scrambled. However, they were also more brittle when the photo itself was of poor quality, with dark lighting, glare, or partial cropping.
  * OCR and LLM models were more stable across noisy or degraded inputs, but they struggled with nuanced layout interpretation, often mislinking categories and attributes.



The diagram below shows how the two pipelines now coexist under the same guardrail system.

Both models attempt transcription, and their outputs are evaluated. The guardrail then decides which transcriptions meet the accuracy bar and which need human review.

This hybrid setup led to the best of both worlds. By letting the guardrail arbitrate quality between multimodal and OCR-based models, the system boosted automation rates while still preserving the high accuracy required for production.

##  Conclusion

Automating the transcription of restaurant menus from photos is a deceptively complex problem. What began as a simple OCR-to-LLM pipeline quickly revealed its limits when confronted with messy, real-world inputs: inconsistent structures, incomplete menus, and poor image quality.

The engineering team’s solution was not just to push harder on the models themselves, but to rethink the system architecture. The introduction of a guardrail classifier allowed automation to scale responsibly, ensuring that customers and restaurants always saw accurate menus while machines handled the simpler cases.

As the field of generative AI evolved, the system evolved with it.

By combining OCR and LLM models with newer multimodal approaches under the same guardrail framework, DoorDash was able to harness the strengths of both families of models without being trapped by their weaknesses.

Looking ahead, several opportunities remain open:

  * **Domain fine-tuning:** The growing dataset of human-verified transcriptions can be used to fine-tune LLMs and multimodal models for the specific quirks of restaurant menus.
  * **Upstream quality controls:** Investing in photo preprocessing with techniques like de-glare, de-noising, de-skewing, and crop detection will lift the accuracy of both OCR-based and multimodal systems.
  * **Guardrail refinement:** As models continue to improve, so can the guardrail. Expanding its feature set, retraining LightGBM, or even exploring hybrid architectures will push safe automation further.



**References:**

  * [ Using LLM to Transcribe Restaurant Menu Photos ](<https://substack.com/redirect/d6618f95-2453-4bc0-bd02-2cb7f915a1e4?j=eyJ1IjoiMzhqd3YifQ.5A9UDKbxtmTMpf48aHOFTZVvvXtwbwJ-khjaPLWh8tA>)
  * [ What are AI guardrails? ](<https://substack.com/redirect/eb92452d-fa79-4d61-8584-aee0150e958f?j=eyJ1IjoiMzhqd3YifQ.5A9UDKbxtmTMpf48aHOFTZVvvXtwbwJ-khjaPLWh8tA>)



* * *

##  ByteByteGo Technical Interview Prep Kit

Launching the All-in-one interview prep. We’re making all the books available on the [ ByteByteGo website ](<https://substack.com/redirect/761229fa-d373-4091-a1d7-4e617ac21b33?j=eyJ1IjoiMzhqd3YifQ.5A9UDKbxtmTMpf48aHOFTZVvvXtwbwJ-khjaPLWh8tA>) .

[ ![](https://substackcdn.com/image/fetch/$s_!ElNh!,w_1100,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff836cb42-7734-4a14-8e10-a1f7a8efaac0_4406x6238.png) ](<https://substack.com/redirect/761229fa-d373-4091-a1d7-4e617ac21b33?j=eyJ1IjoiMzhqd3YifQ.5A9UDKbxtmTMpf48aHOFTZVvvXtwbwJ-khjaPLWh8tA>)

What's included:

  * System Design Interview
  * Coding Interview Patterns
  * Object-Oriented Design Interview
  * How to Write a Good Resume
  * Behavioral Interview (coming soon)
  * Machine Learning System Design Interview
  * Generative AI System Design Interview
  * Mobile System Design Interview
  * And more to come



[ Launch sale: 50% off ](<https://substack.com/redirect/761229fa-d373-4091-a1d7-4e617ac21b33?j=eyJ1IjoiMzhqd3YifQ.5A9UDKbxtmTMpf48aHOFTZVvvXtwbwJ-khjaPLWh8tA>)

* * *

##  **SPONSOR US**

Get your product in front of more than 1,000,000 tech professionals.

Our newsletter puts your products and services directly in front of an audience that matters - hundreds of thousands of engineering leaders and senior engineers - who have influence over significant tech decisions and big purchases.

Space Fills Up Fast - Reserve Today

Ad spots typically sell out about 4 weeks in advance. To ensure your ad reaches this influential audience, reserve your space now by emailing **[ sponsorship@bytebytego.com ](<mailto:sponsorship@bytebytego.com>) . **

[ ![](https://substackcdn.com/image/fetch/$s_!PeVs!,w_36,c_scale,f_png,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Ficon%2FLucideHeart%3Fv%3D4%26height%3D36%26fill%3Dnone%26stroke%3D%2523808080%26strokeWidth%3D2) Like ](<https://substack.com/app-link/post?publication_id=817132&post_id=172889991&isFreemail=true&submitLike=true&r=38jwv>)

[ ![](https://substackcdn.com/image/fetch/$s_!x1tS!,w_36,c_scale,f_png,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Ficon%2FLucideComments%3Fv%3D4%26height%3D36%26fill%3Dnone%26stroke%3D%2523808080%26strokeWidth%3D2) Comment ](<https://substack.com/app-link/post?publication_id=817132&post_id=172889991&isFreemail=true&comments=true&r=38jwv&action=post-comment>)

[ ![](https://substackcdn.com/image/fetch/$s_!5EGt!,w_36,c_scale,f_png,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Ficon%2FNoteForwardIcon%3Fv%3D4%26height%3D36%26fill%3Dnone%26stroke%3D%2523808080%26strokeWidth%3D2) Restack ](<https://substack.com/redirect/2/eyJlIjoiaHR0cHM6Ly9vcGVuLnN1YnN0YWNrLmNvbS9wdWIvYnl0ZWJ5dGVnby9wL2hvdy1kb29yZGFzaC11c2VzLWFpLW1vZGVscy10by11bmRlcnN0YW5kP3V0bV9zb3VyY2U9c3Vic3RhY2smdXRtX21lZGl1bT1lbWFpbCZ1dG1fY2FtcGFpZ249ZW1haWwtcmVzdGFjay1jb21tZW50JmFjdGlvbj1yZXN0YWNrLWNvbW1lbnQmcj0zOGp3diZ0b2tlbj1leUoxYzJWeVgybGtJam8xTkRNM09UQXpMQ0p3YjNOMFgybGtJam94TnpJNE9EazVPVEVzSW1saGRDSTZNVGMxTnpVeE9EY3dOeXdpWlhod0lqb3hOell3TVRFd056QTNMQ0pwYzNNaU9pSndkV0l0T0RFM01UTXlJaXdpYzNWaUlqb2ljRzl6ZEMxeVpXRmpkR2x2YmlKOS41cDhrUmQ5dzBGQzVJSDNLQlpQOThuQXhtbURwd3R3cy1Fcjh1bkFTeXpZIiwicCI6MTcyODg5OTkxLCJzIjo4MTcxMzIsImYiOnRydWUsInUiOjU0Mzc5MDMsImlhdCI6MTc1NzUxODcwNywiZXhwIjoyMDczMDk0NzA3LCJpc3MiOiJwdWItMCIsInN1YiI6ImxpbmstcmVkaXJlY3QifQ.cvtY4B-Om44p3I0l7SNDs8s6Q26qE1cYhsWaSaK2NJM>)

© 2025 ByteByteGo
548 Market Street PMB 72296, San Francisco, CA 94104
[ Unsubscribe ](<https://substack.com/redirect/2/eyJlIjoiaHR0cHM6Ly9ibG9nLmJ5dGVieXRlZ28uY29tL2FjdGlvbi9kaXNhYmxlX2VtYWlsP3Rva2VuPWV5SjFjMlZ5WDJsa0lqbzFORE0zT1RBekxDSndiM04wWDJsa0lqb3hOekk0T0RrNU9URXNJbWxoZENJNk1UYzFOelV4T0Rjd055d2laWGh3SWpveE56ZzVNRFUwTnpBM0xDSnBjM01pT2lKd2RXSXRPREUzTVRNeUlpd2ljM1ZpSWpvaVpHbHpZV0pzWlY5bGJXRnBiQ0o5Lmt2cDljWFFXcFlES1dNUUhVeVZNTWZDVFJSX0dQYjRTbzc2MnN4bmlmZDQiLCJwIjoxNzI4ODk5OTEsInMiOjgxNzEzMiwiZiI6dHJ1ZSwidSI6NTQzNzkwMywiaWF0IjoxNzU3NTE4NzA3LCJleHAiOjIwNzMwOTQ3MDcsImlzcyI6InB1Yi0wIiwic3ViIjoibGluay1yZWRpcmVjdCJ9.jL0rZOngURWGyQ3_yzCWWUR5jCrzfgGhWe3o1-SH-qw?>)

[ ![Start writing](https://substackcdn.com/image/fetch/$s_!LkrL!,w_270,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Fimg%2Femail%2Fpublish-button%402x.png) ](<https://substack.com/redirect/2/eyJlIjoiaHR0cHM6Ly9zdWJzdGFjay5jb20vc2lnbnVwP3V0bV9zb3VyY2U9c3Vic3RhY2smdXRtX21lZGl1bT1lbWFpbCZ1dG1fY29udGVudD1mb290ZXImdXRtX2NhbXBhaWduPWF1dG9maWxsZWQtZm9vdGVyJmZyZWVTaWdudXBFbWFpbD1nLmFyb3JhOTk1MzRAZ21haWwuY29tJnI9Mzhqd3YiLCJwIjoxNzI4ODk5OTEsInMiOjgxNzEzMiwiZiI6dHJ1ZSwidSI6NTQzNzkwMywiaWF0IjoxNzU3NTE4NzA3LCJleHAiOjIwNzMwOTQ3MDcsImlzcyI6InB1Yi0wIiwic3ViIjoibGluay1yZWRpcmVjdCJ9.Hxx_tuz5kwbLR168wAaMREGCTCrF8R4LDs6FjHnZZUs?>)
