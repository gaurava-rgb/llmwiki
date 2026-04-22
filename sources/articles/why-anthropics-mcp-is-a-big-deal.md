---
title: "Why Anthropic’s MCP is a Big Deal"
reader_id: "01k6dsr79e6na0vaz8sagdxsn5"
notion_page_id: "34a4ebe7-f118-817b-9294-dea30c24576f"
category: "email"
source_type: ""
reader_url: "https://read.readwise.io/read/01k6dsr79e6na0vaz8sagdxsn5"
source_url: "mailto:reader-forwarded-email/a90a8a4ef932b951b513dbd91f3d9914"
author: "ByteByteGo"
site: "Substack"
tags: []
published: "2025-09-30"
saved_at: "2025-09-30"
reading_time: "9 mins"
summary: "MCP is a standard that lets AI connect to any data source or tool. It cuts integration work because each app and each data source only needs one MCP implementation, and major companies are already using it. Its transport, protocol, and capability layers let models fetch live data securely and become connected assistants."
content_hash: "1da1588f2f528cf727b8a631ecf30acf84ba329d89a895ad36cafab31c96f57b"
---

Forwarded this email? [ Subscribe here ](<https://substack.com/redirect/2/eyJlIjoiaHR0cHM6Ly9ibG9nLmJ5dGVieXRlZ28uY29tL3N1YnNjcmliZT91dG1fc291cmNlPWVtYWlsJnV0bV9jYW1wYWlnbj1lbWFpbC1zdWJzY3JpYmUmcj0zOGp3diZuZXh0PWh0dHBzJTNBJTJGJTJGYmxvZy5ieXRlYnl0ZWdvLmNvbSUyRnAlMkZ3aHktYW50aHJvcGljcy1tY3AtaXMtYS1iaWctZGVhbCIsInAiOjE3NDU1OTU5MiwicyI6ODE3MTMyLCJmIjp0cnVlLCJ1Ijo1NDM3OTAzLCJpYXQiOjE3NTkyNDY3MTcsImV4cCI6MjA3NDgyMjcxNywiaXNzIjoicHViLTAiLCJzdWIiOiJsaW5rLXJlZGlyZWN0In0.XKsXmph2Yvgo9pvcWUbrOLZrjQ6kLTB-vF21BGnr_vs?>) for more

#  [ Why Anthropic’s MCP is a Big Deal ](<https://substack.com/app-link/post?publication_id=817132&post_id=174559592&isFreemail=true&r=38jwv>)

[ ByteByteGo ](<https://substack.com/@bytebytego399569>)

Sep 30

[ ![](https://substackcdn.com/image/fetch/$s_!U1Ej!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc9941c68-e5b7-4b93-be75-df7cc4ffef02_504x540.png) ](<https://substack.com/@bytebytego399569>)

[ ![](https://substackcdn.com/image/fetch/$s_!PeVs!,w_36,c_scale,f_png,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Ficon%2FLucideHeart%3Fv%3D4%26height%3D36%26fill%3Dnone%26stroke%3D%2523808080%26strokeWidth%3D2) ](<https://substack.com/app-link/post?publication_id=817132&post_id=174559592&isFreemail=true&submitLike=true&r=38jwv>)

[ ![](https://substackcdn.com/image/fetch/$s_!x1tS!,w_36,c_scale,f_png,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Ficon%2FLucideComments%3Fv%3D4%26height%3D36%26fill%3Dnone%26stroke%3D%2523808080%26strokeWidth%3D2) ](<https://substack.com/app-link/post?publication_id=817132&post_id=174559592&isFreemail=true&comments=true&r=38jwv&action=post-comment>)

[ ![](https://substackcdn.com/image/fetch/$s_!_L14!,w_36,c_scale,f_png,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Ficon%2FLucideShare2%3Fv%3D4%26height%3D36%26fill%3Dnone%26stroke%3D%2523808080%26strokeWidth%3D2) ](<https://substack.com/app-link/post?publication_id=817132&post_id=174559592&action=share&triggerShare=true&isFreemail=true&r=38jwv>)

[ ![](https://substackcdn.com/image/fetch/$s_!5EGt!,w_36,c_scale,f_png,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Ficon%2FNoteForwardIcon%3Fv%3D4%26height%3D36%26fill%3Dnone%26stroke%3D%2523808080%26strokeWidth%3D2) ](<https://substack.com/redirect/2/eyJlIjoiaHR0cHM6Ly9vcGVuLnN1YnN0YWNrLmNvbS9wdWIvYnl0ZWJ5dGVnby9wL3doeS1hbnRocm9waWNzLW1jcC1pcy1hLWJpZy1kZWFsP3V0bV9zb3VyY2U9c3Vic3RhY2smdXRtX21lZGl1bT1lbWFpbCZ1dG1fY2FtcGFpZ249ZW1haWwtcmVzdGFjay1jb21tZW50JmFjdGlvbj1yZXN0YWNrLWNvbW1lbnQmcj0zOGp3diZ0b2tlbj1leUoxYzJWeVgybGtJam8xTkRNM09UQXpMQ0p3YjNOMFgybGtJam94TnpRMU5UazFPVElzSW1saGRDSTZNVGMxT1RJME5qY3hOeXdpWlhod0lqb3hOell4T0RNNE56RTNMQ0pwYzNNaU9pSndkV0l0T0RFM01UTXlJaXdpYzNWaUlqb2ljRzl6ZEMxeVpXRmpkR2x2YmlKOS5HVHY0ZmVoUVQ1ZDgxOHd2QmRPT0dvMERma3BOT3FyTjJpdTFNOGtIS0xNIiwicCI6MTc0NTU5NTkyLCJzIjo4MTcxMzIsImYiOnRydWUsInUiOjU0Mzc5MDMsImlhdCI6MTc1OTI0NjcxNywiZXhwIjoyMDc0ODIyNzE3LCJpc3MiOiJwdWItMCIsInN1YiI6ImxpbmstcmVkaXJlY3QifQ.A83ddZYglmiX7fTO8bFCxRR4DDk6kQzp0onBRmqz030>)

[ READ IN APP ![](https://substackcdn.com/image/fetch/$s_!ET-_!,w_36,c_scale,f_png,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Ficon%2FLucideArrowUpRight%3Fv%3D4%26height%3D36%26fill%3Dnone%26stroke%3D%2523808080%26strokeWidth%3D2) ](<https://open.substack.com/pub/bytebytego/p/why-anthropics-mcp-is-a-big-deal?redirect=app-store>)

##  [ Ship code that breaks less: Sentry AI Code Review (Sponsored) ](<https://substack.com/redirect/2adae73c-ceac-45f6-9f9b-e10d9525c398?j=eyJ1IjoiMzhqd3YifQ.5A9UDKbxtmTMpf48aHOFTZVvvXtwbwJ-khjaPLWh8tA>)

[ ![](https://substackcdn.com/image/fetch/$s_!Gsez!,w_1100,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc2cb7194-207a-416e-a1b6-ffe87da64d98_1430x715.png) ](<https://substack.com/redirect/2adae73c-ceac-45f6-9f9b-e10d9525c398?j=eyJ1IjoiMzhqd3YifQ.5A9UDKbxtmTMpf48aHOFTZVvvXtwbwJ-khjaPLWh8tA>)

Catch issues before they merge. Sentry’s AI Code Review inspects pull requests using real error and performance signals from your codebase. It surfaces high-impact bugs, explains root causes, and generates targeted unit tests in separate branches. Currently supports GitHub and GitHub Enterprise. Free while in open beta.

[ Try AI Code Review ](<https://substack.com/redirect/2adae73c-ceac-45f6-9f9b-e10d9525c398?j=eyJ1IjoiMzhqd3YifQ.5A9UDKbxtmTMpf48aHOFTZVvvXtwbwJ-khjaPLWh8tA>)

* * *

Imagine asking an AI assistant about tomorrow’s meetings, only to receive a polite response that it cannot access calendar information. Or requesting current stock prices and getting data from months ago.

This disconnect between AI capabilities and real-world data represents one of the most significant limitations in artificial intelligence today.

The root of this problem lies in how AI models work. Large language models like GPT-4 or Claude are trained on vast amounts of text data, but this training happens at a specific point in time. Once training completes, the model’s knowledge becomes frozen. It cannot learn about events that happened after its training date, cannot access private company data, and cannot interact with external systems or databases. Even the most sophisticated AI becomes an island of outdated information without connections to the current world.

Traditionally, connecting AI to external data sources meant writing custom integration code for each system. A developer would need separate code to connect their AI to Google Drive, different code for Slack, another implementation for their database, and so on.

This approach quickly becomes unsustainable. As more AI applications emerge and more data sources need integration, the complexity multiplies exponentially.

The Model Context Protocol (MCP), introduced by Anthropic in 2024, offers a solution to this fragmentation.

MCP provides a standardized way for AI systems to connect with any data source or tool. Major technology companies, including OpenAI, Microsoft, and Google, have already adopted this protocol, signaling its emergence as a universal standard for AI connectivity.

In this article, we will look at MCP in detail and explore what makes it such an important component in the AI landscape.

[ ![](https://substackcdn.com/image/fetch/$s_!Hzmy!,w_1100,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6624e7fc-84d6-402f-9ab3-a28e1db96e8b_1429x1600.png) ](<https://substack.com/redirect/9c9b5048-11ba-420b-b287-04dcad248036?j=eyJ1IjoiMzhqd3YifQ.5A9UDKbxtmTMpf48aHOFTZVvvXtwbwJ-khjaPLWh8tA>)

* * *

##  [ Avoid 5 Costly Kafka Challenges at Scale (Sponsored) ](<https://substack.com/redirect/da18a757-f81a-43fe-9d7a-8543fbf94d23?j=eyJ1IjoiMzhqd3YifQ.5A9UDKbxtmTMpf48aHOFTZVvvXtwbwJ-khjaPLWh8tA>)

[ ![](https://substackcdn.com/image/fetch/$s_!R1-6!,w_1100,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbf684881-433e-4622-9dd9-a06860d3969c_1200x628.png) ](<https://substack.com/redirect/da18a757-f81a-43fe-9d7a-8543fbf94d23?j=eyJ1IjoiMzhqd3YifQ.5A9UDKbxtmTMpf48aHOFTZVvvXtwbwJ-khjaPLWh8tA>)

If you’re running Kafka in production, you know scaling can introduce risks that most teams don’t see until it’s too late, including data quality issues, hidden costs, compliance gaps, and even production failures.

This free ebook isn’t just a checklist — it’s a framework for understanding and preventing costly mistakes. Inside, you’ll:

  * Learn the  **five most common scaling pitfalls** and why they happen.
  * See  **real-world examples** of failures in production.
  * Apply  **practical strategies** to spot weaknesses early and build resilience.



Walk away with actionable insights to keep Kafka running smoothly at enterprise scale.

[ Download the free ebook now ](<https://substack.com/redirect/da18a757-f81a-43fe-9d7a-8543fbf94d23?j=eyJ1IjoiMzhqd3YifQ.5A9UDKbxtmTMpf48aHOFTZVvvXtwbwJ-khjaPLWh8tA>)

* * *

##  What is MCP?

Think of MCP as a universal adapter for artificial intelligence. Just as USB-C provides a single standard that connects phones, laptops, monitors, and countless other devices, MCP creates one standard way for AI models to connect with any data source or tool.

The Model Context Protocol exists as both a specification and actual working code.

  * The specification defines the rules and standards for how AI systems should communicate with external data sources.
  * The implementations are the actual software libraries and tools that developers use to build these connections.



Before MCP, the AI industry faced a multiplication problem. For example, if we had 10 AI applications that each needed to connect to 20 different data sources, we would need to write 200 separate integration programs (10 multiplied by 20). Each combination required its own custom code. MCP transforms this multiplication into simple addition. Now those same 10 AI applications and 20 data sources only need 30 implementations total: each AI application implements MCP once, and each data source implements MCP once. They can all then communicate freely with each other.

Anthropic provides everything needed to implement MCP. This includes:

  * The protocol specification that defines how everything works .
  * Software development kits in popular programming languages like Python, TypeScript, and Java.
  * Reference implementations for common services like GitHub, Slack, and PostgreSQL, and development tools for testing and debugging MCP connections.



All of this is released as open source software, meaning anyone can use, modify, and contribute to it without paying licensing fees.

This open approach mirrors how HTTP became the foundation of the web. Just as HTTP created a common language that any web browser could use to talk to any web server, MCP creates a common language for AI to talk to any data source. The open nature ensures no single company controls the standard, encouraging widespread adoption and innovation.

##  Three Components of MCP Architecture

MCP operates through three essential components that work together seamlessly. See the diagram below:

[ ![](https://substackcdn.com/image/fetch/$s_!6AmU!,w_1100,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F829f461e-6da6-46b7-9b50-132fd6125a07_1600x958.png) ](<https://substack.com/redirect/6cef232d-116c-4b1a-8ad2-d5ea55b5b172?j=eyJ1IjoiMzhqd3YifQ.5A9UDKbxtmTMpf48aHOFTZVvvXtwbwJ-khjaPLWh8tA>)

Understanding each component and its role helps clarify how AI systems gain access to real-world data and capabilities.

###  1 - MCP Host Application

The Host Application represents the software that people actually use and interact with. This could be Claude Desktop, where users chat with an AI assistant, ChatGPT running in a web browser, or a custom application built by a company for specific tasks.

The host application serves as the orchestrator of the entire interaction. It manages the user interface, receives user requests, determines what external data or tools are needed, and presents responses back to the user in a meaningful way.

Different hosts serve different purposes. Claude Desktop focuses on general-purpose AI assistance for individual users. Development environments like Cursor or GitHub Copilot help programmers write code more efficiently. Enterprise applications might be designed for specific workflows like customer service or data analysis. Regardless of their specific purpose, all host applications share the common need to connect their AI capabilities with external data sources.

###  2 - MCP Client

The MCP Client acts as the translator that lives inside each host application.

When the host needs to connect to an external data source, it creates an MCP client specifically for that connection. Each client maintains a dedicated one-to-one relationship with a single MCP server.

If a host application needs to access multiple data sources, it creates multiple clients, one for each server it needs to communicate with. The client handles all the technical details of the MCP protocol, converting requests from the host into properly formatted MCP messages and translating responses back into a format the host can use.

###  3 - MCP Server

The MCP Server forms the bridge between the MCP protocol and actual data sources.

Each server typically focuses on one specific integration, wrapping around a particular service or system to expose its capabilities through MCP. For example, a PostgreSQL MCP server knows how to connect to PostgreSQL databases and translate MCP requests into SQL queries. Similarly, a GitHub MCP server understands how to interact with GitHub’s API to fetch repository information or create issues.

These servers can run locally on the same machine as the host application, useful for accessing local files or databases. They can also run remotely on cloud infrastructure, enabling connections to web services and APIs.

Servers are built by various parties. Anthropic provides reference implementations for common services, companies build servers for their internal systems, and individual developers create and share servers for tools they use.

##  MCP Protocol Stack

MCP’s technical architecture consists of three distinct layers, each handling a specific aspect of communication between AI systems and data sources.

###  1 - Transport Layer

The Protocol Stack Overview begins with the Transport Layer, which handles the actual transmission of messages.

  * For local connections, MCP uses STDIO (standard input/output), where messages flow through simple text streams between processes on the same computer. This approach works perfectly when an MCP server runs on the same machine as the AI application.
  * For remote connections, MCP employs HTTP for sending requests and Server-Sent Events (SSE) for receiving responses, enabling secure communication across networks and the internet.



See the diagram below:

[ ![](https://substackcdn.com/image/fetch/$s_!XTJX!,w_1100,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4e92380d-932b-421a-880f-a9e343b8eb2b_1600x886.png) ](<https://substack.com/redirect/5f8a1d09-aafc-4ac2-a6a0-e7c969f44027?j=eyJ1IjoiMzhqd3YifQ.5A9UDKbxtmTMpf48aHOFTZVvvXtwbwJ-khjaPLWh8tA>)

###  2 - Protocol Layer

The Protocol Layer uses JSON-RPC 2.0, a lightweight standard for remote procedure calls. JSON-RPC was chosen because it provides a simple, well-established format that developers already understand.

Every message is just JSON text with a clear structure: a method name, parameters, and an ID to track responses. This simplicity makes debugging straightforward since developers can read the messages directly.

###  3 - The Capability Layer

The Capability Layer defines what MCP can actually do through three main primitives.

  * Tools are functions that AI can execute to perform actions like sending emails or creating database entries.
  * Resources provide read-only access to data without causing any changes to the system.
  * Prompts are templates that help AI combine multiple operations effectively, similar to saved workflows that can be reused.



##  The Journey of a Request

Understanding how MCP works becomes clearer when we trace a single request from start to finish.

See the diagram below:

[ ![](https://substackcdn.com/image/fetch/$s_!Z7GB!,w_1100,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0f15c917-7cc0-481b-b443-960b7b8aecdc_1600x1371.png) ](<https://substack.com/redirect/83a8b8db-38f1-489c-9f57-024a8ff1b0c5?j=eyJ1IjoiMzhqd3YifQ.5A9UDKbxtmTMpf48aHOFTZVvvXtwbwJ-khjaPLWh8tA>)

Let’s follow what happens when someone asks their AI assistant: “What’s our top-selling product?”

  * The journey begins when the user types this question into their AI application.
  * The AI model analyzes the question and recognizes that it needs current sales data from the company database to provide an accurate answer. The AI cannot access this information from its training data, so it must retrieve it through MCP.
  * The host application activates its MCP client for the database server. The client takes the AI’s request and formats it as a JSON-RPC message. This message contains a method name indicating it wants to execute a database query tool, the query as a parameter, and a unique identifier like “request-789” to track this specific request. Note that the query is not a complete SQL query. It is abstract, such as “get top top-selling product for last month”. The formatted message looks like structured text that clearly specifies what action needs to be taken.
  * The transport layer now takes over to deliver this message. If the database MCP server runs on the same computer, the message travels through STDIO, essentially passing from one program to another through the operating system. If the server runs on a remote machine, the message travels as an HTTP request across the network, with proper authentication headers to ensure security.
  * The MCP server receives this message and begins its crucial translation work. It extracts the query from the MCP request, prepares an actual SQL query for the PostgreSQL database, and connects to the actual PostgreSQL database using standard database protocols. The server executes the query, which might look for products sorted by sales volume. This interaction with the database happens entirely outside of MCP, using PostgreSQL’s native communication methods.
  * The database processes the query and returns results. For example, the query may answer that “Product A” led sales with $487,000 in revenue last month.
  * The MCP server receives these raw database results and formats them into an MCP response message. This response includes the same request identifier “request-789” and the data structured in a way that MCP clients understand.
  * The response travels back through the transport layer to the waiting client. The client matches the response ID to its outstanding request and extracts the sales data. It passes this information to the host application, which provides it to the AI model along with the original question.
  * Finally, the AI model crafts a natural language response: “Our top-selling product last month was Product A, which generated $487,000 in revenue, representing 30% of total sales.”



This entire journey demonstrates MCP’s modular design.

Each component handles one specific task: the AI understands language, the client speaks MCP protocol, the server translates to database queries, and the database manages data. No component needs to understand the others’ internal workings.

##  Conclusion

The Model Context Protocol is fast becoming an essential infrastructure piece in the AI landscape that makes everything else possible. While AI models capture headlines with their reasoning capabilities, MCP quietly solves the fundamental problem of connecting these models to real-world data and systems.

Just as TCP/IP transformed isolated computers into the global internet, MCP is transforming isolated AI models into connected, capable assistants that can interact with the world. This shift from static knowledge to dynamic access represents a fundamental evolution in how AI systems work.

For developers entering the field now, MCP offers a unique opportunity.

The ecosystem is young enough that individual contributions can have a significant impact, yet mature enough to build production-ready solutions. Every new MCP server expands what AI can do, and every improvement to the protocol benefits the entire ecosystem.

The future of AI is not just about smarter models but about better connections between AI and the tools we use daily. Whether through exploring existing MCP servers, building new ones for untapped data sources, or contributing to the protocol itself, developers today have the chance to shape how AI interacts with our world for years to come.

**References:**

  * [ Introducing Model Context Protocol ](<https://substack.com/redirect/38514de9-27f9-4fc1-a3fd-f9e81973ec13?j=eyJ1IjoiMzhqd3YifQ.5A9UDKbxtmTMpf48aHOFTZVvvXtwbwJ-khjaPLWh8tA>)
  * [ What is Model Context Protocol? ](<https://substack.com/redirect/d6c4ceaf-20e6-411c-a38f-854b31700a3c?j=eyJ1IjoiMzhqd3YifQ.5A9UDKbxtmTMpf48aHOFTZVvvXtwbwJ-khjaPLWh8tA>)



* * *

##  **SPONSOR US**

Get your product in front of more than 1,000,000 tech professionals.

Our newsletter puts your products and services directly in front of an audience that matters - hundreds of thousands of engineering leaders and senior engineers - who have influence over significant tech decisions and big purchases.

Space Fills Up Fast - Reserve Today

Ad spots typically sell out about 4 weeks in advance. To ensure your ad reaches this influential audience, reserve your space now by emailing **[ sponsorship@bytebytego.com ](<mailto:sponsorship@bytebytego.com>) . **

[ ![](https://substackcdn.com/image/fetch/$s_!PeVs!,w_36,c_scale,f_png,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Ficon%2FLucideHeart%3Fv%3D4%26height%3D36%26fill%3Dnone%26stroke%3D%2523808080%26strokeWidth%3D2) Like ](<https://substack.com/app-link/post?publication_id=817132&post_id=174559592&isFreemail=true&submitLike=true&r=38jwv>)

[ ![](https://substackcdn.com/image/fetch/$s_!x1tS!,w_36,c_scale,f_png,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Ficon%2FLucideComments%3Fv%3D4%26height%3D36%26fill%3Dnone%26stroke%3D%2523808080%26strokeWidth%3D2) Comment ](<https://substack.com/app-link/post?publication_id=817132&post_id=174559592&isFreemail=true&comments=true&r=38jwv&action=post-comment>)

[ ![](https://substackcdn.com/image/fetch/$s_!5EGt!,w_36,c_scale,f_png,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Ficon%2FNoteForwardIcon%3Fv%3D4%26height%3D36%26fill%3Dnone%26stroke%3D%2523808080%26strokeWidth%3D2) Restack ](<https://substack.com/redirect/2/eyJlIjoiaHR0cHM6Ly9vcGVuLnN1YnN0YWNrLmNvbS9wdWIvYnl0ZWJ5dGVnby9wL3doeS1hbnRocm9waWNzLW1jcC1pcy1hLWJpZy1kZWFsP3V0bV9zb3VyY2U9c3Vic3RhY2smdXRtX21lZGl1bT1lbWFpbCZ1dG1fY2FtcGFpZ249ZW1haWwtcmVzdGFjay1jb21tZW50JmFjdGlvbj1yZXN0YWNrLWNvbW1lbnQmcj0zOGp3diZ0b2tlbj1leUoxYzJWeVgybGtJam8xTkRNM09UQXpMQ0p3YjNOMFgybGtJam94TnpRMU5UazFPVElzSW1saGRDSTZNVGMxT1RJME5qY3hOeXdpWlhod0lqb3hOell4T0RNNE56RTNMQ0pwYzNNaU9pSndkV0l0T0RFM01UTXlJaXdpYzNWaUlqb2ljRzl6ZEMxeVpXRmpkR2x2YmlKOS5HVHY0ZmVoUVQ1ZDgxOHd2QmRPT0dvMERma3BOT3FyTjJpdTFNOGtIS0xNIiwicCI6MTc0NTU5NTkyLCJzIjo4MTcxMzIsImYiOnRydWUsInUiOjU0Mzc5MDMsImlhdCI6MTc1OTI0NjcxNywiZXhwIjoyMDc0ODIyNzE3LCJpc3MiOiJwdWItMCIsInN1YiI6ImxpbmstcmVkaXJlY3QifQ.A83ddZYglmiX7fTO8bFCxRR4DDk6kQzp0onBRmqz030>)

© 2025 ByteByteGo
[ 548 Market Street ](<https://www.google.com/maps/search/548+Market+Street?entry=gmail&source=g>) PMB 72296, San Francisco, CA 94104
[ Unsubscribe ](<https://substack.com/redirect/2/eyJlIjoiaHR0cHM6Ly9ibG9nLmJ5dGVieXRlZ28uY29tL2FjdGlvbi9kaXNhYmxlX2VtYWlsP3Rva2VuPWV5SjFjMlZ5WDJsa0lqbzFORE0zT1RBekxDSndiM04wWDJsa0lqb3hOelExTlRrMU9USXNJbWxoZENJNk1UYzFPVEkwTmpjeE55d2laWGh3SWpveE56a3dOemd5TnpFM0xDSnBjM01pT2lKd2RXSXRPREUzTVRNeUlpd2ljM1ZpSWpvaVpHbHpZV0pzWlY5bGJXRnBiQ0o5Lll2UFZhcjgyczhmTTlIdGtLV25fR21uRS1BcnlVQ1BZV3JoTG5wa2NqME0iLCJwIjoxNzQ1NTk1OTIsInMiOjgxNzEzMiwiZiI6dHJ1ZSwidSI6NTQzNzkwMywiaWF0IjoxNzU5MjQ2NzE3LCJleHAiOjIwNzQ4MjI3MTcsImlzcyI6InB1Yi0wIiwic3ViIjoibGluay1yZWRpcmVjdCJ9.8oFmTevlXqZ6YwKXLarDAmSpGcpeV2j5PFefuG7pNGE?>)

[ ![Start writing](https://substackcdn.com/image/fetch/$s_!LkrL!,w_270,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Fimg%2Femail%2Fpublish-button%402x.png) ](<https://substack.com/redirect/2/eyJlIjoiaHR0cHM6Ly9zdWJzdGFjay5jb20vc2lnbnVwP3V0bV9zb3VyY2U9c3Vic3RhY2smdXRtX21lZGl1bT1lbWFpbCZ1dG1fY29udGVudD1mb290ZXImdXRtX2NhbXBhaWduPWF1dG9maWxsZWQtZm9vdGVyJmZyZWVTaWdudXBFbWFpbD1nLmFyb3JhOTk1MzRAZ21haWwuY29tJnI9Mzhqd3YiLCJwIjoxNzQ1NTk1OTIsInMiOjgxNzEzMiwiZiI6dHJ1ZSwidSI6NTQzNzkwMywiaWF0IjoxNzU5MjQ2NzE3LCJleHAiOjIwNzQ4MjI3MTcsImlzcyI6InB1Yi0wIiwic3ViIjoibGluay1yZWRpcmVjdCJ9.7BefotkBfxdb_5QGKA9TCAxlwzauC-g1qTHuC1qB650?>)
