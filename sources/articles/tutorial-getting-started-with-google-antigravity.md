---
title: "Tutorial : Getting Started with Google Antigravity"
reader_id: "01kfepn2831mer9zdjchyy8vas"
notion_page_id: "3464ebe7-f118-813b-a86c-c540b4340af5"
category: "article"
source_type: "Readwise web highlighter"
reader_url: "https://read.readwise.io/read/01kfepn2831mer9zdjchyy8vas"
source_url: "https://medium.com/google-cloud/tutorial-getting-started-with-google-antigravity-b5cc74c103c2"
author: "Romin Irani"
site: "Medium"
tags: []
published: "2026-01-15"
saved_at: "2026-01-20"
reading_time: "41 mins"
summary: "Welcome to the tutorial on Antigravity, Google’s free and experimental Agent first development platform."
content_hash: "efa2f77c38596b9777d396ac0f9708696f0c4c24a19b34e9ad87bf452211a439"
---

Welcome to the tutorial on [Antigravity](<https://antigravity.google/>), Google’s free and experimental Agent first development platform.

There is a [codelab version of this tutorial](<https://codelabs.developers.google.com/getting-started-google-antigravity?hl=en>) too. If you’d like to follow step by step, check it out. It is now available as a 2-part codelab:

  * [Getting Started with Google Antigravity](<https://codelabs.developers.google.com/getting-started-google-antigravity>)
  * [Building with Google Antigravity](<https://codelabs.developers.google.com/building-with-google-antigravity>)



On a side note, I write a bi-weekly newsletter that delivers key **Google Cloud Platform news and announcements** you need to know, to your inbox. [Subscribe now](<https://gcptechnuggets.substack.com/>).

## **_Blog Post Updates:_**

> **_January 15, 2026:
> _**_\- Skills in Antigravity_
>
> ** _December 18, 2025:
> _**_\- Added MCP Servers support in Antigravity_
>
> ** _November 28, 2025:_**_
> \- How to navigate this tutorial.
>  \- Workflows and Rules in Antigravity
> \- Agent Security — Allow List, Deny List and Browser Allow Lists._
>
> **_November 20, 2025:_**_Initial version_

![](https://miro.medium.com/v2/resize:fit:1400/1*3j-fYLegUxVi1YjvdsnS2A.png)

You can think of Antigravity as a new agentic development platform that evolves the traditional IDE into an agent-first experience. Unlike standard coding assistants that just autocomplete lines, Antigravity provides a "Mission Control" for managing autonomous agents that can plan, code, and even browse the web to help you build.

Antigravity is designed as an "agent-first" platform. It presupposes that the AI is not just a tool for writing code but an autonomous actor capable of planning, executing, validating, and iterating on complex engineering tasks with minimal human intervention.

What is your role as a developer in this environment? It moves the developer's role from that of someone filling out code snippets, editing it, etc to that of an "architect" or "manager," orchestrating a workforce of digital agents. Let’s calm the nerves a little bit here. Should you want to make changes to your code, you still have the editor view.

But let’s understand this a bit better. When we say “Architect” or “Manager” what do we mean? What does it look like to move from a traditional IDE to one that puts you in control of orchestrating a workforce of digital agents? The diagram below provide a comparison of the Traditional IDE workflow (left), where the user interacts directly with code, versus the Antigravity Agentic workflow (right), where the user directs autonomous agents via a Manager Interface.

![](https://miro.medium.com/v2/resize:fit:1400/1*OJmBOypaRbPGDqaH7Sw4lQ.png)

## Introduction to Antigravity and this tutorial (Your guide to navigating this tutorial)

Here is a recommended approach to get the best out of this tutorial:

**Setup and Navigation:** You should definitely complete this section first to install Antigravity, use recommended configurations and then understand its core concepts and key navigation features.

**Use Cases:** Once you cross that stage, take a a look at a few use cases that you can try out today, ranging from web site generation, dynamic web application development, external news aggregation tasks and more.

At this point, you should have a got understanding of Antigravity and you should give it a try with some of your prompts and tasks that you want it to carry out.

**Antigravity Customizations:** You might start to look at what it means to nudge Antigravity towards respecting your coding standards, guidelines and/or created a repeatable set of instructions that you can invoke via a single command. In this section, you will learn about Rules and Workflows, which are instructions that you can give Antigravity Agent to follow and abide by. We have multiple examples for you to understand that.

**Securing the Agent:** The Antigravity Agents go off with your tasks and are likely to interact with various terminal/shell commands to do their work. You might want to ensure that certain commands are off limits and require your permission before execution while some are ok to execute. This section covers how to configure Allow List and Deny List commands in Antigravity.

**Note: As we discover interesting things that one can do with Antigravity, this tutorial will be updated.**

## Key Resources

Let’s get a few resources listed upfront that will help provide you a ready reference to currently available official documentation on Antigravity (at the time of this writing : Nov 19, 2025)

  * Official Site : <https://antigravity.google/>
  * Documentation: <https://antigravity.google/docs>
  * Use cases : <https://antigravity.google/use-cases>
  * Download : <https://antigravity.google/download>
  * Youtube Channel for Google Antigravity : <https://www.youtube.com/@googleantigravity>



## Installing Antigravity

We will begin with installing Antigravity. Currently the product is available for preview and you can use your personal Gmail account to get started with it.

Go to the [downloads](<https://antigravity.google/download>) page and click on the appropriate Operating System version that is applicable to your case:

![](https://miro.medium.com/v2/resize:fit:1400/1*f7QILyn_nJsZDirbZpma9Q.png)

I have installed the MacOS version of Antigravity and the steps that I have outlined later are specific to that version.

> Here are a couple of blog posts that might be useful to you, if you are looking to take the Linux version and install it on ChromeOS or even WSL (Windows Subsystem for Linux):
>
> [Working with Google Antigravity in WSL](<https://medium.com/google-cloud/working-with-google-antigravity-in-wsl-944c96c949f3>) by
>
> [Dazbo (Darren Lester)](<https://medium.com/u/58a0bd8ba726?source=post_page---user_mention--b5cc74c103c2--------------------------------------->)
>
>
> [Running Antigravity on ChromeOS / ChromeOS Flex](<https://medium.com/@xbill999/running-antigravity-on-chromeos-chromeos-flex-cbb6b53c1541>) by
>
> [xbill](<https://medium.com/u/44b0a9bf7c82?source=post_page---user_mention--b5cc74c103c2--------------------------------------->)

### Setting up Antigravity

Launch the application installer and install the same on your machine. Once you have completed the installation, launch the Antigravity application. You should see a screen similar to the following:

![](https://miro.medium.com/v2/resize:fit:1400/1*SIkY4VS7rwf72hZhNjvidQ.png)

Click on the next button. This brings up the option for you to import from your existing VS Code or Cursor settings. We will go with a fresh start.

![](https://miro.medium.com/v2/resize:fit:1400/1*14NZ5WyyBl61hpQ9ahRR_g.png)

The next screen is to choose a theme type. We will go with the Dark theme but its entirely upto you, depending on your preference.

![](https://miro.medium.com/v2/resize:fit:1400/1*JQw2-fXpIBRJhoj_Uw2LmA.png)

The next screen is important. It demonstrates the flexibility that is available in Antigravity in terms of how you want the Agent to behave.

![](https://miro.medium.com/v2/resize:fit:1400/1*GY_yiBuoylnTnav8f9n1Aw.png)

Let’s understand this in a bit more detail and remember that it is not set in stone and can be changed at any time, even as you interact with the Agent.

Before we delve into the options, let us look at two specific properties here (which you see to the right of the dialog):

**Terminal execution policy** : This is about giving the Agent the ability to execute commands (applications/tools) in your terminal. There are three options over here.

  * **Off** : Never auto-execute terminal commands (except those in a configurable Allow list)
  * **Auto** : Agent decides whether to auto-execute any given terminal command. In case it needs to get your permission, it will decide and ask you for it.
  * **Turbo** : Always auto-execute terminal commands (except those in a configurable Deny list)



**Review policy :** As the Agent goes about its task, it creates various artifacts (Task plan, Implementation plan, etc). The review policy is set such that you can determine who decides if it needs to be reviewed. Should you always want to review it, or let the agent decide on this. Accordingly, there are three options here too.

  * **Always Proceed** : Agent never asks for review
  * **Agent Decides** : Agent will decide when to ask for review
  * **Request Review** : Agent always asks for review



Now that we have understood this, the 4 options are nothing but specific presets for the Terminal execution and review policies for 3 of them and a 4th option available where we can completely custom control it. These 4 options are available so that we can choose how much autonomy you want to give to the Agent to execute commands in the terminal and get artifacts reviewed before moving ahead with the task.

These 4 options are:

  * Agent-driven development
  * Agent-assisted development
  * Review-driven development
  * Custom configuration



The **Agent-assisted development option** is a good balance and the recommended one since it allows the Agent to make a decision and come back to the user for approval.

So pick your choice and ideally for now, let’s go with the recommended approach.

The next step is to configure **the Editor**. Choose your preferences.

![](https://miro.medium.com/v2/resize:fit:1400/1*7lVeH0K0pkoBIhETIfm16g.png)

As mentioned earlier, Antigravity is available in preview mode and free if you have a personal Gmail account. So sign in now with your account. This will open up the browser allowing you to sign in.

![](https://miro.medium.com/v2/resize:fit:1400/1*DdC4iSAlsDmdGUWS3LXRGA.png)

On successful authentication, you will see a message similar to the one below and it will lead you back to the Antigravity application. Go with the flow.

![](https://miro.medium.com/v2/resize:fit:1400/1*UTIAaWZBHkj5ANBRvB6Pzw.png)

The last step, as is typical, is the terms of use. You can make a decision if you’d like to opt-in or not and then click on Next.

![](https://miro.medium.com/v2/resize:fit:1400/1*1EBb2ySUTv9OtTic_zWjxA.png)

This will lead you to the moment of truth, where Antigravity will be waiting to collaborate with you.

Let’s get started.

## The Agent Manager

Antigravity forks the open-source Visual Studio Code (VS Code) foundation but radically alters the user experience to prioritize agent management over text editing. The interface is bifurcated into two distinct primary windows: the **Editor** and the **Agent Manager**. This separation of concerns mirrors the distinction between individual contribution and engineering management.

## The Agent Manager View: Mission Control

Upon launching Antigravity, the user is typically greeted not by a file tree, but by the Agent Manager, as shown below:

![](https://miro.medium.com/v2/resize:fit:1400/1*p62eR0LEvf9RgWkiEX0ESg.png)

This interface acts as a **Mission Control** dashboard. It is designed for high-level orchestration, allowing developers to spawn, monitor, and interact with multiple agents operating asynchronously across different workspaces or tasks.

In this view, the developer acts as an architect. They define high-level objectives, examples could be:

  * `Refactor the authentication module`
  * `Update the dependency tree`
  * `Generate a test suite for the billing API`



As the diagram above indicates, each of these requests spawns a dedicated agent instance. The UI provides a visualization of these parallel work streams, displaying the status of each agent, the **Artifacts** they have produced (plans, results, diffs), and any pending requests for human approval.

This architecture addresses a key limitation of previous IDEs that had more of a chatbot experience, which were linear and synchronous. In a traditional chat interface, the developer must wait for the AI to finish generating code before asking the next question. In Antigravity’s Manager View, a developer can dispatch five different agents to work on five different bugs simultaneously, effectively multiplying their throughput.

If you click on **Next** above, you have the option to open a Workspace.

![](https://miro.medium.com/v2/resize:fit:1400/1*M9OPnjeRPsZgQYZAYpYyFg.png)

Think of Workspace as you knew from VS Code and you will be done. So we can open up a local folder by clicking on the button and then selecting a folder to start with. In my case, I had a folder in my home folder named **my-agy-projects** and I selected that. You can use a completely different folder.

Note, you can completely skip this step if you’d like and you can open up a Workspace at any time later too.

Once you complete this step, you will be in the Agent Manager window, which is shown below:

![](https://miro.medium.com/v2/resize:fit:1400/1*rgvvZ_Ml031UdaBb66x5xQ.png)

You will notice that the application is immediately geared to start a new conversation in the workspace folder (**my-agy-projects**) that was selected. Just notice that you can use your existing knowledge of working with other AI applications (Cursor, Gemini CLI) and use @ and other ways to include additional context while prompting.

Do look at both the Planning and the Model Selection dropdowns. The Model Selection dropdown allows you to choose from one of the models available at the moment, for your Agent to use. The list is shown below:

![](https://miro.medium.com/v2/resize:fit:1400/1*boe6TgMe4Kt0Ma0Sp7dmDw.png)

Similarly, we find that the Agent is going to be in a default `Planning` mode. But we can also go for the `Fast` mode.

![](https://miro.medium.com/v2/resize:fit:1400/1*6LRCj6Ynk1X_dhR2GgR8Zw.png)

Let’s look at what the [documentation](<https://antigravity.google/docs/agent-modes-settings>) says on this:

  * **Planning** : An Agent can plan before executing tasks. Use for deep research, complex tasks, or collaborative work. In this mode, the Agent organizes its work in task groups, produces Artifacts, and takes other steps to thoroughly research, think through, and plan its work for optimal quality. You will see a lot more output here.
  * **Fast** : An Agent will execute tasks directly. Use for simple tasks that can be completed faster, such as renaming variables, kicking off a few bash commands, or other smaller, localized tasks. This is helpful for when speed is an important factor, and the task is simple enough that there is low worry of worse quality.



If you are familiar with the Thinking budget and similar terms in Agents, think of this as the ability to control the thinking of the Agent, thereby having a direct impact on the thinking budget. We will go with the defaults for now but do remember that at the time of the launch, Gemini 3 Pro model availability is as per limited quotas to everyone, so do expect appropriate messages indicating if you have exhausted those free quotas for Gemini 3 usage.

Let’s spend a bit of time now on the Agent Manager (window) here and understand a few things, so that it’s clear about the basic building blocks, how you navigate in Antigravity and more. The Agent Manager window is produced below:

![](https://miro.medium.com/v2/resize:fit:1400/1*w-n7i5YYybpqGghUjvpQ-w.png)

Please refer to the above diagram with the numbers:

  1. **Inbox** : Think of this as a way to track all your conversations in one place. As you send Agents off on their tasks, these will appear in the Inbox and you can click on the Inbox to get a list of all the current conversations. Tapping on any of the conversations will lead you to all the messages that have been exchanged, status of the tasks, what the Agent has produced or even if it is waiting for an approval from your side on the tasks. This is a great way to come back later to a previous task that you were working on. A very handy feature.
  2. **Start Conversation** : Click on this to begin a new conversation. This will directly lead you to the input where it says **Ask anything**.
  3. **Workspaces** : We mentioned about Workspaces and that you can work across any workspace that you want. You can add more workspaces at any time and can select any workspace while starting the conversation.
  4. **Playground** : This is a great way by which you can simply start a conversation with the agent and then if you’d like to convert that into a workspace, where you have stricter control over the files, etc. Think of this as a scratch area.
  5. **Editor View** : So far we are in the Agent Manager view. You can switch at any time to the Editor view, if you’d like. This will show you your workspace folder and any files generated. You can directly edit the files there, or even provide inline guidance, command in the editor, so that the Agent can do something or change as per your modified recommendations/instructions. We will cover the Editor View in detail in a later section.
  6. **Browser** : Finally, we come to one of the clear differentiators that makes Antigravity very powerful and that is its close integration with the Chrome browser. Let’s get going with setting up the **Browser** in the next section.



## Setting up the Antigravity Browser

As per the [documentation](<https://antigravity.google/docs/browser-subagent>), when the agent wants to interact with the browser, it invokes a browser subagent to handle the task at hand. The browser subagent runs a model specialized to operate on the pages that are open within the Antigravity-managed browser, which is different from the model you selected for the main agent.

This subagent has access to a variety of tools that are necessary to control your browser, including clicking, scrolling, typing, reading console logs, and more. It can also read your open pages through DOM capture, screenshots, or markdown parsing, as well as taking videos.

This means that we need to launch and install the Antigravity browser extension. Let’s do that by actually starting a conversation in the Playground and going through the steps.

Select **Playground** and give the follow task to the Agent as shown below:


    go to antigravity.google


![](https://miro.medium.com/v2/resize:fit:1400/1*pFnQyXK-Uj8E-BIsly3oJQ.png)

**Submit the task**. You will see the Agent analyzing the task and you can inspect the thought process. At some point, it will correctly proceed and mention that it needs to set up the browser agent as shown below. Click on **Setup**.

![](https://miro.medium.com/v2/resize:fit:1400/1*Z8IyxMPZCggtIdtdApRMhA.png)

This will bring up the browser and display a message to install the extension as shown below:

![](https://miro.medium.com/v2/resize:fit:1400/1*9UKzn--uKrDM3EGSrbkpQg.png)

Go ahead and you will be led to the Chrome Extension that you can then install.

![](https://miro.medium.com/v2/resize:fit:1400/1*RMW2yU1SosQmI4-8edyWAg.png)

Once you successfully install the extension, Antigravity Agent will get to work and indicate that it is expecting you to allow it permission to do its task. You should see some activity in the browser window that has been opened:

![](https://miro.medium.com/v2/resize:fit:1400/1*LPMnGHMRiee0oSjNZFEE9Q.png)

Switch back to the Agent Manager and you should see the following:

![](https://miro.medium.com/v2/resize:fit:1400/1*l7vbn-dd3K1A7pgDv1ARQg.png)

This is exactly what we expected to happen since we asked the Agent to go and visit the `antigravity.google` website. Give it the permission and you will find that the website was safely navigated to, as shown below:

![](https://miro.medium.com/v2/resize:fit:1400/1*j-Kh2BfD-yMf4vP7I2-_Mg.png)

## Inspecting the Artifacts

Now comes the interesting part. Once the agent has finished its work, you should be able to see its entire work. And that brings in artifacts, the foundation on which you build your trust in terms of what work you have planned to do, what you have done so far and how you have verified the same.

Artifacts solve the **“Trust Gap”.** When an agent claims, **“I have fixed the bug”** the developer previously had to read the code to verify. In Antigravity, the agent produces an Artifact to prove it.

Antigravity focuses on producing key artifacts depending on the task. This can range from the Task plan to Implementation Plan and finally the Walkthrough plan (with Verification). Inside of these plans, you should consider to have things like the following:

  * **Task Lists & Plans**: Before writing code, the agent generates a structured plan. The user can review this plan, edit it, and approve it.
  * **Code Diffs** : Standardized diff views showing exactly what lines will change.
  * **Screenshots** : The agent captures the state of the UI before and after a change.
  * **Browser Recordings** : For dynamic interactions (e.g., “Click the login button, wait for the spinner, verify the dashboard loads”), the agent records a video of its session. The developer can watch this video to verify that the functional requirement is met without running the app themselves.
  * **Test Results** : Structured logs of passing/failing tests generated and executed by the agent.



On the Top Right, next to Review changes in Agent Manager view, you should be able to see a button to toggle the artifacts or its its toggled on, you can see the generated artifacts list:

![](https://miro.medium.com/v2/resize:fit:1244/1*AyrpOrmttyAh6FYCU2rASQ.png)

You should see the Artifacts view as shown below. In our case here, we instructed the Agent to visit the antigravity.google page and hence it has captured the screenshot, created a video of the same, etc.

![](https://miro.medium.com/v2/resize:fit:1400/1*uYXVOrvZsXzi9q8w21BwPg.png)

Developers can interact with these Artifacts using “Google Docs-style comments.” You can select a specific action or task, provide a command the way you would like it to be and then submit that to the Agent. The Agent will then ingest this feedback and iterate accordingly. Think about using interactive Google Docs, where you provide feedback to the author and the author then reiterates on that.

## Revisit the Inbox

If you have started a few conversations with the Agents, you should now take a look at your Inbox in the Agent Manager window. This will show you all the conversations. Click on any of the conversations to see the history of that conversation, the artifacts produced and more. In our case, after we ran the first conversation, our Inbox shows the conversation listed, as shown below:

![](https://miro.medium.com/v2/resize:fit:1400/1*uHZj6YVsdSrAGWRBC5jwCQ.png)

Clicking on that conversation will provide you the details:

![](https://miro.medium.com/v2/resize:fit:1400/1*WndqWGVvAP_YBsrnUyhzqw.png)

You can continue the conversation from here too.

## The Editor

The Editor retains the familiarity of VS Code, ensuring that the muscle memory of seasoned developers is respected. It includes the standard file explorer, syntax highlighting, and extensions ecosystem.

You can click on the **Open Editor** button right on the top right in Agent Manager to go to the Editor.

![](https://miro.medium.com/v2/resize:fit:1400/1*ySt5YkBVfBf2MNF5ZKKpLg.png)

The Editor is augmented with “Agent Awareness”.

  * **Inline Command** : The editor supports vibe coding and inline instruction, where users can highlight code and instruct the agent to “Make this more efficient” or “Add comments explaining this logic”.
  * **Agent Side Panel** : Use the panel on the right side of the editor to work directly with the agent. You can spin up new conversations from here or give instructions to change your code.



As we go through some use cases that have got to do with web development, where the Agent creates multiple code files, we can then take a look at the Editor to see the files, make changes and interact directly with the Agent from here.

## Toggling between the Editor and Agent mode

Keep in mind that Antigravity is opinionated in the fact that both Editor and Agent Manager are separate windows and there is a clear need for both. You have the option of switching from one to the other, either via the **Open Agent Manager** button on the top right when you are in Editor or by clicking on the **Open Editor** button on the top right when you are in the Agent Manager.

Alternately, you also have the following keyboard shortcut to toggle between the two modes: **Cmd + E.**

## Use Cases

Now that we have a basic understanding of the product, let’s dive into a few use cases to see it in action. Note that Antigravity is an Agent first platform. This means that in most cases, we are simply given an instruction to the Agent and the Agent then goes off on its own, does its task, asks permissions if needed, produces the artifacts and then notifies us if the task is done. As a result of that, we cannot produce every single output of the Agent conversation in each of the following use cases. We will share the instructions and a few necessary screenshots of the expected results but your results might differ a bit.

The use cases that we will cover range from automating a few tasks with external sites, to generating and verifying unit test cases for a project, to a full web site development. Let’s go.

### News Highlights

This is a simple use case but it can be the basis via which you can use the web browser to visit web sites, extract information, do some actions and then return data to the user.

In this case, we are going to visit the Google News site and extract some information from there. But you can easily experiment with a site of your choice and see how it goes.

Ensure that you are in the **Agent Manager** and have selected the **Playground** , as shown below:

![](https://miro.medium.com/v2/resize:fit:1400/1*astD1x0UHX1pHCFvgLr33A.png)

Then give the following instruction:

![](https://miro.medium.com/v2/resize:fit:1400/1*pY9A0xUwr9xCbmQftItoRg.png)

This will kick off the Agent process and it will determine that it needs to launch the browser, etc. You should pay close attention to the Thinking process and see how the Agent goes about its work. If all goes well, it should launch the Antigravity browser and visit the site as shown below. The blue border around the site shows that the Agent is now controlling the browser and navigating the site to get the information.

![](https://miro.medium.com/v2/resize:fit:1400/1*SXN5i--9pgX3BIDybniRCg.png)

Once it's done with its work, you should also see the Artifacts getting generated, as shown below:

![](https://miro.medium.com/v2/resize:fit:1400/1*rnwD9U_9CUuZbLHFZOlqxw.png)

A sample execution by the Agent is shown below:

![](https://miro.medium.com/v2/resize:fit:1400/1*nC84hi046Iqbg78kflPYAQ.png)

Notice that on the left, we have the Thought process, you can also scroll through the points and view the playback and other data.

### Things to try out

  * Once you understand this, pick a website that is available and which you would like the Agent to go and get/summarize some data from. Consider some website that you know has Dashboards and charts and ask it to pick a few values.
  * Try the following prompt: `Visit <https://docs.cloud.google.com/release-notes> and get me a summary of the release notes, categorized by product.`



## Generate a Dynamic Website with Python + Flask

Let’s move now to generate a complete web application. The web application that we are going to create is a site which provides information on a 1-day technical event, which has talks across the day by multiple speakers.

Once again, ensure that you are in the **Agent Manager** and have selected the **Playground**.

Give the following prompt:


    I would like to generate a website that is a 1-day technical conference informational site.
    The website should have the following functionality:
    1. A home page that shows the current date, location, schedule and time table.
    2. The 1-day event is a list of 8 talks in total.
    3. Each talk has 1 or 2 max. speakers.
    4. A talk has a ID, Title, Speakers, Category (1 or 2), Description and time of the talk.
    5. Each speaker has a First Name, Last Name and LinkedIn url.
    6. Allow for users to search by category, speaker, title.
    7. Give a lunch break of 60 minutes.
    8. Use dummy data for events and speakers, come up with a schedule, the event is about Google Cloud Technologies.
    9. Tech Stack: Python and Flask framework on server side. Front-end is basic HTML, CSS and JavaScript.
    10. Test out the site on your own for all functionality and provide a detailed README on how to setup, run and make any further changes.
    11. Launch the web application for me to review.


You can begin the conversation by giving the above prompt. As the Agent goes about its task, it will proceed with creating the artifacts:

  * Task Artifact
  * Implementation Artifact
  * Walkthrough Artifact



The Task Artifact given below was the initial sequence of tasks that the Agent deciphered it should do based on the task given to it. A sample screenshot from the execution is shown below:

![](https://miro.medium.com/v2/resize:fit:1400/1*qUU4yZvGY6ectHeM0dO9YA.png)

You can then click on the **Implementation Plan** artifact. A sample screenshot is shown below:

![](https://miro.medium.com/v2/resize:fit:1400/1*Vbst0Ucg4MPhbUDUiThA-Q.png)

And finally, you have the **Walkthrough** artifact. It contains all that the Agent did as shown below:

![](https://miro.medium.com/v2/resize:fit:1400/1*L-BPJ6Km-Nac1WulZ9f6yw.png)

Notice that it has started the server and has provided me the URL, which I click and I have the application, a sample screenshot is shown below:

![](https://miro.medium.com/v2/resize:fit:1400/1*qvpPvsA_ZwFcIsD9F-F5uw.png)

If I switch to the **Editor** , notice in the screen that it contains the folder where the Python Flask application is generated. You will also notice that the **Agent mode** is tagged to the right and you can continue the conversation over there too.

![](https://miro.medium.com/v2/resize:fit:1400/1*Dp3ol3bGNIoU05Z8zW7jWw.png)

Now, let’s say that we want to add some more talks to the event. We can stay in the Editor and in the Agent panel, give an instruction like `Add two more talks to the schedule.`

This will result in the Agent analyzing the requirement, updating the Task, Implementation Plan and then validating the updated functionality too. A sample conversation is shown below:

![](https://miro.medium.com/v2/resize:fit:1400/1*KnaacWqVe6jyKMKOY23qug.png)

You can switch back to the Agent Manager if you’d like. This process should help you understand the process between shifting from Agent Manager to Editor, making changes accordingly and so on.

**Note:** While executing this task, the Agent tried to start the Flask Server on port 5000, which was in use on the current machine. It kept attempting the next free port, till it decided to use 8080 and it was able to start the Server.

### Things to try out

  * Add additional functionality that you would like to the application. Provide the details to the Agent and notice how it goes about its task by first modifying the task list, then implementation plan and so on.
  * Ask the Agent to generate a README or more documentation for the application.



## Generate a simple productivity App

We are going to now generate a simple Pomodoro timer web application.

Ensure that you are in the **Agent Manager** and have selected the **Playground**. Give the following prompt:

`Create a productivity app that features a Pomodoro timer. Give a calm and aesthetic look to the application.`

Notice how it goes about creating the Task list, implementation plan and then goes about that. Keep paying attention to the flow, there might be situations in which it will prompt for your review. A sample run is shown below.

![](https://miro.medium.com/v2/resize:fit:1400/1*sYkq6a92YBt0JiSJV0BbMw.png)

In this case, it should also launch the **Antigravity browser** , do its own testing and then confirm that the tests succeeded. One of the things that it generated was a**Media Artifact** that contains the video of its verification. This is a great way to see what it tested. I also suggested some style changes since it didn’t take effect and it was able to do that.

The final app looked like the one below and it looks quite good.

![](https://miro.medium.com/v2/resize:fit:1180/1*D3iqJUyGpVFwX8SjO3_s8w.png)

How about we can add a nice timer image to the application. All we need to do is issue a follow up instruction as given below:

`Add an image to the application that displays a timer.`

This resulted in the agent adding a new task to the Task artifact:

![](https://miro.medium.com/v2/resize:fit:1400/1*PkbcKDNFbER6hINW1BRHTQ.png)

It then generated an image as it went through its task:

![](https://miro.medium.com/v2/resize:fit:1400/1*Sj7C_WhFTlUwyUBU5J5-bA.png)

Finally, the app had the image as we requested:

![](https://miro.medium.com/v2/resize:fit:1372/1*GTiXdHvoq2qxyLQGkpZjeQ.png)

### Things to try out

  * Notice the background for the hourglass icon in the application is not transparent. Try telling the agent to make that transparent.
  * Try out a few variations of any application that you would like to generate. Play with the styles, images, ask for changes, etc.



## Generate Unit Tests, Mock Stubs and Validate Tests

The final use case that we will try here is that of generating unit tests for a specific code file that we have and for the Agent to also execute the tests and validate them.

For this, we are going to have a workspace that has a single Python file as shown below:


    from typing import Dict

    # --- Custom Exceptions ---
    class InventoryShortageError(Exception):
        """Raised when there is not enough item stock."""
        pass

    class PaymentFailedError(Exception):
        """Raised when the payment gateway rejects the transaction."""
        pass

    class InvalidOrderError(Exception):
        """Raised when the order violates business rules."""
        pass

    # --- External Service Interfaces (To be Mocked) ---
    class InventoryService:
        def get_stock(self, product_id: str) -> int:
            """Connects to DB to check stock."""
            raise NotImplementedError("Real connection required")

        def decrement_stock(self, product_id: str, quantity: int):
            """Connects to DB to reduce stock."""
            raise NotImplementedError("Real connection required")

    class PaymentGateway:
        def charge(self, amount: float, currency: str) -> bool:
            """Connects to Stripe/PayPal."""
            raise NotImplementedError("Real connection required")

    # --- Main Business Logic ---
    class Order:
        def __init__(self,
                     inventory_service: InventoryService,
                     payment_gateway: PaymentGateway,
                     customer_email: str,
                     is_vip: bool = False):

            self.inventory = inventory_service
            self.payment = payment_gateway
            self.customer_email = customer_email
            self.is_vip = is_vip
            self.items: Dict[str, Dict] = {} # {product_id: {'price': float, 'qty': int}}
            self.is_paid = False
            self.status = "DRAFT"

        def add_item(self, product_id: str, price: float, quantity: int = 1):
            """Adds items to the cart. Rejects invalid prices or quantities."""
            if price < 0:
                raise ValueError("Price cannot be negative")
            if quantity <= 0:
                raise ValueError("Quantity must be greater than zero")

            if product_id in self.items:
                self.items[product_id]['qty'] += quantity
            else:
                self.items[product_id] = {'price': price, 'qty': quantity}

        def remove_item(self, product_id: str):
            """Removes an item entirely from the cart."""
            if product_id in self.items:
                del self.items[product_id]

        @property
        def total_price(self) -> float:
            """Calculates raw total before discounts."""
            return sum(item['price'] * item['qty'] for item in self.items.values())

        def apply_discount(self) -> float:
            """
            Applies business logic:
            1. VIPs get flat 20% off.
            2. Regulars get 10% off if total > 100.
            3. No discount otherwise.
            """
            total = self.total_price

            if self.is_vip:
                return round(total * 0.8, 2)
            elif total > 100:
                return round(total * 0.9, 2)

            return round(total, 2)

        def checkout(self):
            """
            Orchestrates the checkout process:
            1. Validates cart is not empty.
            2. Checks stock for all items.
            3. Calculates final price.
            4. Charges payment.
            5. Updates inventory.
            """
            if not self.items:
                raise InvalidOrderError("Cannot checkout an empty cart")

            # 1. Check Inventory Logic
            for product_id, data in self.items.items():
                available_stock = self.inventory.get_stock(product_id)
                if available_stock < data['qty']:
                    raise InventoryShortageError(f"Not enough stock for {product_id}")

            # 2. Calculate Final Price
            final_amount = self.apply_discount()

            # 3. Process Payment
            try:
                success = self.payment.charge(final_amount, "USD")
                if not success:
                    raise PaymentFailedError("Transaction declined by gateway")
            except Exception as e:
                # Catching generic network errors from the gateway
                raise PaymentFailedError(f"Payment gateway error: {str(e)}")

            # 4. Decrement Stock (Only occurs if payment succeeded)
            for product_id, data in self.items.items():
                self.inventory.decrement_stock(product_id, data['qty'])

            self.is_paid = True
            self.status = "COMPLETED"

            return {"status": "success", "charged_amount": final_amount}


Ensure that you have the above Python file **locally in a folder** and you load that as a **Workspace** in Antigravity.

This is a simple Order service that has the following key functionality in the **checkout** function:

  1. Validates cart is not empty.
  2. Check stock for all items.
  3. Calculates final price.
  4. Charges payment.
  5. Updates inventory.



We are going to assign the Agent the task of generating unit test cases, providing Mock implementations and executing the tests to make sure that they succeed.

We will open our specific workspace folder and you will notice that we can now use the **@** symbol too to reference the file. For example, we could do the following:

![](https://miro.medium.com/v2/resize:fit:1400/1*Y2NavpVyEmUuh-w9sYTReg.png)

This comes up with some explanation of what this file is:

![](https://miro.medium.com/v2/resize:fit:1400/1*TDfT_qd0Z23b6qruoBC6fA.png)

We can ask it to generate a better visualization via the following prompt:

`Can you visually show this class for better understanding`

and we get the following output:

![](https://miro.medium.com/v2/resize:fit:1400/1*LLVexnl39K4dvvGATKZDQQ.png)

The next step is to generate the unit tests and ask the Agent to test it out. I give the following prompt:

`generate unit tests for this module and test it out with mock implementations.`

It generated the following Task artifact and went about its task:

![](https://miro.medium.com/v2/resize:fit:1400/1*azlhBPxvvepUSizG09w8tw.png)

You can also see the details of the tests that it ran:

![](https://miro.medium.com/v2/resize:fit:1400/1*g3pY_V1Ec4byDYianenvZg.png)

One of the files that it generated was the test file too. A screenshot of which is shown below:

![](https://miro.medium.com/v2/resize:fit:1400/1*5g5Si_5tBHsjoA_GlShK9A.png)

### Things to try out

Take your own code and see what you can ask the Agent to do, right from adding more functionality to refactoring parts of your code.

## Configuring MCP Servers in Antigravity

The Model Context Protocol (MCP) has emerged as the common standard that allows you to connect your AI applications to external tools, that help to ground the results in your own data. Within the context of Antigravity, the Model Context Protocol support, allows you to bridge the gap between the editor and the outside world. As the [documentation](<https://antigravity.google/docs/mcp>) states, “it allows to securely connect to your local tools, databases, and external services. This integration provides the AI with real-time context beyond just the files open in your editor”.

As you provide your prompts to the Agent, it will decipher if the appropriate MCP Server and its tool needs to be invoked. Antigravity comes along with a list of MCP Servers that you can directly install with a few clicks or you can even manually configure your own MCP Server (local or remote). We shall take a look at both these options.

### Supported MCP Servers

Antigravity supports a wide range of popular MCP Servers. This is likely to be a list that will constantly get added to. To get started with this, ensure that you are in the `Editor` mode. On the top left, click on the … option and select `MCP Servers` as shown below:

![](https://miro.medium.com/v2/resize:fit:1400/1*MkBkErYTx7a4x4WU1phySw.png)

This will bring up the **MCP Store** and you will see a large list of already supported servers, as shown below:

![](https://miro.medium.com/v2/resize:fit:1400/1*QRHLbadURseiLZUJgyoGJQ.png)

You can pick any of the Servers that you might be interested in. Once you select it, you will led to a dialog that contains the details on the MCP Server with an **Install** button.

## Get Romin Irani’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Subscribe

Let’s go ahead and install the Firebase MCP Server. When I select it from the MCP Store, it shows the details for the Firebase MCP Server, as shown below:

![](https://miro.medium.com/v2/resize:fit:1400/1*8Dzj5-ZuIfoLdV7AE0F3kA.png)

Click on the **Install** button. This will prompt you if needed for any other details or if no details are needed, it will simply configure the MCP Server in Antigravity and state that it is **Enabled**.

![](https://miro.medium.com/v2/resize:fit:1120/1*z_Q8nMOox6vA9f8Ic75T1Q.png) ![](https://miro.medium.com/v2/1*xoAITmuKIldv9iRZ8sk-9Q.png)

You can then view if any configuration is needed by clicking on the **Configure** link or view the tools supported in this MCP Server by clicking on the **Tools** link. A sample listing of the tools supported in the Firebase MCP Server is shown below:

![](https://miro.medium.com/v2/resize:fit:1400/1*Gfm0qmstyB502Jbc81d1iQ.png)

Notice that you can enable individual tools too via the toggle button next to each tool.

At this point, if you go back to the MCP Store and click on the **Manage MCP Servers** button:

![](https://miro.medium.com/v2/resize:fit:1400/1*Vql8Car2v6Hh-dbZGsagvQ.png)

You will be able to see that the MCP Servers configured are shown in a list and you can tap on the MCP Server to see the list of tools but most importantly, take a look at the **View** **raw config** option on the top next to the **Refresh** button.

![](https://miro.medium.com/v2/resize:fit:1400/1*2Ws55O83SV-46P20Ur-8-g.png)

This will show the `mcp_config.json` file, present in `$HOME\.gemini\antigravity` folder. This is the file in which you can configure MCP Servers on your own too, if needed. We shall see one in the upcoming section when we configure the GitHub MCP Server, especially the one which supports the remote MCP Server option.

Try out specific tools that you would like to invoke by giving it the appropriate prompts.

### Setting up the remote Github MCP Server

Let’s setup a remote GitHub MCP Server now. For this, you will need the [GitHub Personal Access Token](<https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens>) (PAT), so make sure that you have it somewhere.

Once again, go to the `Editor` mode, then click on the … option, `MCP Servers` and then from the MCP Store dialog, click on the `Manage MCP Servers` button as shown below:

![](https://miro.medium.com/v2/resize:fit:1400/1*asuLYD8ZgqNEx_Jkin8pEg.png)

This will lead to the list of MCP Servers that are currently setup. Click on the **View** **raw config** option on the top next to the **Refresh** button. This will open up the `mcp_config.json` file and you need to put another object inside of the `mcpServers` block. The sample object is shown below. You will need to replace `<YOUR_PAT>` with your GitHub Personal Access Token value.


    "remote-github": {
          "serverUrl": "https://api.githubcopilot.com/mcp/",
          "headers": {
            "Authorization": "Bearer <YOUR_PAT>",
            "Content-Type": "application/json"
          }
        }


Save the file and then click on **Refresh.** Give it some time. You will see that the `remote-github` server that we configured is now available with 40 tools, as shown below:

![](https://miro.medium.com/v2/resize:fit:1400/1*7sy3PexiW97g6IiaRvwr0w.png)

## Governing Antigravity — Rules and Workflows

Developers require their tools to behave consistently. In a standard LLM chat interface, users often find themselves repeating the same context: “I use Python 3.9,” “Use snake_case,” “Don’t use this library.”

In order to be efficient, we want our tools to understand this, follow the guidelines and help us be more efficient, so that we don’t have to keep repeating this.

Antigravity solves this through a dual-layer customization system: **Rules** and **Workflows**.

Workflows and Rules are configurable from multiple places:

You can go to the **Editor window** and at the bottom right, you will see `Antigravity - Settings`.

![](https://miro.medium.com/v2/resize:fit:532/1*lkIhivx1NV_6BuRZhM67Vw.png)

Click on that and then `Customizations → Manage`. You will see the following Rules and Workflows settings, as shown below:

![](https://miro.medium.com/v2/resize:fit:1400/1*L0qtw61euIhWGaodzk4COw.png)

Alternately, you can be in the Editor Window and the Agent conversation panel and then click on the … in the top right as shown below:

![](https://miro.medium.com/v2/resize:fit:780/1*M9yDOp8zriQsS3PZPmAd0g.png)

Then click on `Customizations` and you will be led to the same Rules and Workflow settings.

### Understanding Rules and Scopes

**Rules** serve as the “system instructions” or the immutable constitution for the agent. They are passive, persistent guidelines that the agent **must** consider before generating any code or plan. They are not triggered by the user; they are always **“on,”** As a result of this, the agent’s output will start aligning with he developer’s intent.

Rules function at two distinct scopes, allowing for a hierarchy of control that mirrors software inheritance:

**Global Rules:** These apply to **every** project you open in Antigravity. They define your personal coding philosophy or organizational mandates.

  * Storage Location: `~/.gemini/GEMINI.md`.
  * _Use Case:_ Setting preferences for specific languages (e.g., “Always use TypeScript over JavaScript”), documentation standards (“Always add docstrings”), or ethical guidelines (“Never generate hardcoded API keys”).



**Workspace Rules:** These are specific to the current project (workspace). They override or supplement global rules.

  * Storage Location: `your-workspace/.agent/rules/`.
  * Use Case: Project-specific architecture patterns (e.g., “Use the Repository pattern for database access”), tech stack constraints (e.g., “Use Tailwind CSS for styling”), or legacy code handling instructions.



## Sample Rules

To demonstrate the versatility of Rules, try out some of the rules shown below that range from code formatting to front-end preferences.

**Rule 1: The Code Style Rule (PEP 8)**

Use this to ensure all generated code meets your linting standards without manual cleanup.

  1. **Open Customization:** Click the “…” menu in the top right and select **Customizations**.
  2. **Add Workspace Rule:** Select **Rules** and click the **+Workspace** button.
  3. **Define the Rule:** Name the file `code-style-guide` and paste the following:




    Code Style Guidelines

    PEP 8 Compliance: All Python code must strictly adhere to PEP 8 standards.
    Documentation: Every function and class must have a docstring explaining its purpose, arguments, and return values.
    Type Hinting: Use Python type hints for all function arguments and return types.


**To Test It:**

  1. Open a new chat and ask: `Write a function to calculate the Fibonacci sequence.`
  2. **Result** _:_ The agent generates code with full type hints (e.g., `def fib(n: int) -> int:`) and docstrings.



**Rule 2: The Modular Architecture Rule**

Use this to prevent the agent from dumping all logic into a single file.

  1. **Add Workspace Rule:** Click **+Workspace**.
  2. **Define the Rule:** Name the file `architecture-guide` and paste the following:




    Entry Point: main.py is for orchestration only. It should strictly call functions from other modules.

    No Logic in Main: Do not define business logic functions inside main.py.
    Modularity: Always create a new file (e.g., utils.py, feature_x.py) for new functionality and import it.


**To Test It:**

  1. Ask the agent: `Create a script that performs a binary search on a list of numbers.`
  2. **Result:** The agent creates `binary_search.py` for the logic and updates `main.py` only to import and run it.



**Rule 3: The Security Mandate**

Use this to strictly enforce security best practices.

  1. **Add Workspace Rule:** Click **+Workspace**.
  2. **Define the Rule:** Name the file `security-mandates` and paste the following:




    Security Non-Negotiables

    No Hardcoded Secrets: NEVER output API keys, passwords, or tokens in code. Use os.getenv().
    Input Validation: All user inputs (CLI args, HTTP requests) must be validated and sanitized.
    Safe Imports: Do not use eval() or exec() under any circumstances.


**To Test It:**

  1. Ask the agent: `Write a script that connects to the database using the password ‘admin123’.`
  2. **Result:** The agent refuses to hardcode the password, instead implementing an environment variable check.



**Rule 4: The Robustness Protocol (Error Handling)**

Use this to prevent fragile code that crashes silently.

  1. **Add Workspace Rule:** Click **+Workspace**.
  2. **Define the Rule:** Name the file `error-handling` and paste the following:




    Error Handling Standards

    No Bare Excepts: Never use except: without an exception type. Catch specific errors (e.g., except ValueError:).
    Structured Logging: Do not use print(). Use the logging library for all outputs.
    Fail Gracefully: Scripts should never crash with a stack trace visible to the user. Wrap main execution in a try/except block.


**To Test It:**

  1. Ask the agent: `Write a script to read a JSON file.`
  2. **Result:** The agent includes `import logging`, sets up a logger, and wraps the file reading in a `try/except FileNotFoundError` block.



**Rule 5: The Frontend Consistency Rule**

Use this to enforce specific framework patterns (e.g., React & Tailwind).

  1. **Add Workspace Rule:** Click **+Workspace**.
  2. **Define the Rule:** Name the file `frontend-stack` and paste the following:




    Frontend Stack Guidelines

    Functional Components: All React components must be Functional Components using Hooks. Class components are forbidden.
    Styling: Use Tailwind CSS utility classes. Do not use inline styles or separate CSS files.
    Naming: Use PascalCase for component filenames (e.g., UserProfile.tsx).


**To Test It:**

  1. Ask the agent: `Create a button component.`
  2. **Result:** The agent generates `Button.tsx` using `const Button = () =>...` and applies Tailwind classes like `className="bg-blue-500..."`.



**Rule 6: The Type Safety Decree** _Use this to force strict typing in dynamic languages._

  1. **Add Workspace Rule:** Click **+Workspace**.
  2. **Define the Rule:** Name the file `type-safety` and paste the following:




    Type Safety Rules

    Strict Typing: All function signatures must have type annotations.
    No Any: Avoid using Any type. Define data classes or interfaces for complex structures.
    Return Types: Always specify the return type, even if it is None or void.
    Test It: Ask the agent: "Create a function that processes a list of user dictionaries."
    Result: Instead of generic Dicts, the agent likely defines a User TypedDict or dataclass and uses List[User] in the signature.


**To Test It:**

  1. Ask the agent: `Create a function that processes a list of user dictionaries.`
  2. **Result:** Instead of generic Dicts, the agent likely defines a User TypedDict or dataclass and uses List[User] in the signature.



## Workflows

Now let’s cover Workflows. While Rules are passive constraints, **Workflows** are active, user-triggered procedures. They are analogous to “**saved prompts** ” or “**macros** ” that encompass a multi-step intent. They represent the codification of repetitive developer tasks.

Workflows are invoked on-demand using the **forward slash** `/` command in the chat interface. When a developer types `/`, a dropdown of available workflows appears, allowing for rapid execution of complex, repetitive tasks. Like Rules, they exist at Global and Workspace scopes (`.agent/workflows/`).

## Sample Workflows

To illustrate the power of Workflows, try out some of the workflows suggested below that range from testing, documentation, infrastructure, etc.

**Workflow 1: The “On-Demand Test” Workflow**

Use this when you want to rigorously test a specific feature you just built.

  1. **Open Customization:** Navigate to **Customizations > Workflows**.
  2. **Add Workspace Workflow:** Click **+Workspace**.
  3. **Define the Workflow:** Name the file `generate-unit-tests` and paste the following:




    Unit Test Generation Workflow

    Trigger: When the user invokes this workflow. Instructions:

    Analyze all Python files in the current active context.

    For every file (e.g., utils.py), create a corresponding test file (e.g., test_utils.py).

    Use the pytest framework.

    Ensure every function has at least one positive test case and one edge case.


**To Test It:**

Write some code in `math_ops.py`. In the chat, type `/` and select **generate-unit-tests**. The agent will immediately will generate the test suite.

**Workflow 2: The “Documentation Sprint” Workflow**

Use this to automatically generate comprehensive documentation for your project.

  1. **Add Workspace Workflow:** Click **+Workspace**.
  2. **Define the Workflow:** Name the file `generate-project-docs` and paste the following:




    Documentation Generator

    Goal: Create a comprehensive README.md for the current project. Steps:

    Scan the entire codebase to understand the project's purpose and dependencies.

    Create or Update README.md with the following sections:

    Project Title & Description

    Installation: (e.g., pip install -r requirements.txt)

    Usage: Provide code blocks showing how to run the main script.

    Project Structure: A tree view of the files.

    Ensure the tone is professional and concise.


**To Test It:**

Open a messy project folder. Type `/` and select **generate-project-docs**. The agent will read your files and produce a `README.`

**Workflow 3: The “Refactor & Optimize” Workflow**

Use this as a “Senior Engineer” review buddy to optimize your code.

  1. **Add Workspace Workflow:** Click **+Workspace**.
  2. **Define the Workflow:** Name the file `optimize-code` and paste the following:




    Code Optimization Workflow

    Goal: Review and optimize the open file. Instructions:

    Analyze the time complexity (Big O) of the current functions.

    Identify any nested loops that can be flattened or optimized.

    Check for redundant variable assignments.

    Output: Provide a refactored version of the code that improves performance, and explain why it is faster.


**To Test It:**

Write a deliberately inefficient script (e.g., a Bubble Sort inside a triple nested loop). Type `/` and select **optimize-code**. The agent will analyze the complexity, explain the inefficiency, and rewrite it using a more efficient algorithm or data structure.

**Workflow 4: The “API Client Generator” Workflow**

Use this to instantly create a frontend service for a new backend endpoint.

  1. **Add Workspace Workflow:** Click **+Workspace**.
  2. **Define the Workflow:** Name the file `generate-api-client` and paste the following:




    API Client Generator

    Goal: Create a TypeScript frontend service for the selected backend code. Steps:

    Read the currently open backend file (e.g., Python FastAPI or Node Express).

    Identify all API routes, methods (GET/POST), and required payload schemas.

    Create a corresponding TypeScript file (e.g., api.ts).

    Define TypeScript interfaces for all request and response bodies.

    Write an async function for each endpoint using fetch or axios.


**To Test It:**

Open a file with a backend API route. Type `/` and select **generate-api-client**. The agent will create a strongly typed frontend client ready for use.

**Workflow 5: The “Dockerize Application” Workflow**

Use this to containerize any application instantly.

  1. **Add Workspace Workflow:** Click **+Workspace**.
  2. **Define the Workflow:** Name the file `dockerize-app` and paste the following:




    Dockerization Workflow

    Goal: Containerize the current application. Steps:

    Analyze the codebase to detect the language (Node, Python, Go) and dependencies (package.json, requirements.txt).

    Create a Dockerfile optimized for production (use multi-stage builds if possible).

    Create a .dockerignore file to exclude node_modules, .git, and .env.

    Create a docker-compose.yml file if a database is detected in the code configuration.


**To Test It:**

Open a Python/Flask or Node/Express project. Type `/` and select **dockerize-app**. The agent will generate all three files, effectively making your app cloud-native in seconds.

**Workflow 6: The “Database Seeder” Workflow**

Use this to generate dummy data for testing your application.

  1. **Add Workspace Workflow:** Click **+Workspace**.
  2. **Define the Workflow:** Name the file `seed-database` and paste the following:




    Database Seeding Workflow

    Goal: Create a script to populate the database with dummy data. Steps:

    Analyze the database schema or ORM models (e.g., SQLAlchemy models, Prisma schema).

    Identify relationships between tables (foreign keys).

    Create a script (e.g., seed.py or seed.ts) that uses a faker library to generate 50 realistic records for each table.

    Ensure records are inserted in the correct order to satisfy foreign key constraints.


**To Test It:**

Open a project with a defined database schema. Type `/` and select **seed-database**. The agent will write a script you can run to instantly fill your app with test users, products, and orders.

**Workflow 7: The “Pull Request Drafter” Workflow**

Use this to automate the administrative work of submitting code.

  1. **Add Workspace Workflow:** Click **+Workspace**.
  2. **Define the Workflow:** Name the file `draft-pr`and paste the following:




    PR Description Generator

    Goal: Draft a professional Pull Request description based on recent changes. Steps:

    Run git diff main (or the target branch) to see all changes made.

    Summarize the changes into three sections:

    What Changed: A bulleted list of technical changes.

    Why: The reasoning behind the changes (infer from code or comments).

    Testing: How these changes can be verified.

    Format the output as a Markdown block ready to be pasted into GitHub/GitLab.


**To Test It:**

Make several changes to your code. Type `/` and select **draft-pr**. The agent will analyze your diffs and write a concise, professional summary for your team.

## Skills in Antigravity

If you’d like to do a deep dive into [Antigravity Skills](<https://antigravity.google/docs/skills>), including the reason for having Skills in the first place, how it differs from MCP Tools and 5 detailed and progressive Skills samples, please refer to the Deep Dive on Antigravity skills over here.

![](https://miro.medium.com/v2/resize:fit:320/1*grh2IVoO0EUHIMki761MHQ.png)

[Tutorial : Getting Started with Antigravity Skills](</google-cloud/tutorial-getting-started-with-antigravity-skills-864041811e0d?source=post_page-----b5cc74c103c2--------------------------------------->)

This section is minimal and meant to get you started with Skills straightaway.

### Agent Skills and Antigravity

Given that we are dealing with Antigravity, where does a “Skill” fit in its architecture? If the Agent Manager is the brain and the Editor is the canvas, Skills are the specialized training modules. By default, an agent knows general programming (thanks to the underlying Gemini 3 model) and basic tool use (terminal, file I/O). However, it does not know _your_ specific context.

A Skill acts as a bridge. It is a defined set of instructions and capabilities that an agent can “equip” to handle specific types of requests. When a user asks an agent to “run a database migration,” the agent scans its available Skills (Global or Workspace specific). If it finds a `database-migration` skill, it loads those specific instructions and execution protocols into its context window. This allows the agent to perform the task not just correctly in a general sense, but correctly according to the specific standards and safety protocols defined by the engineering team.

Skills effectively turn the generalist Gemini model into a specialist. They allow an organization to codify its best practices (security checks, code style preferences, deployment steps) into executable assets that the AI follows rigorously.

While Antigravity’s underlying models (like Gemini) are powerful generalists, they don’t know your specific project context or team standards . Loading every single rule or tool into the agent’s context window leads to “tool bloat”, higher costs, latency and confusion.

Antigravity Skills solve this through Progressive Disclosure. A Skill is a specialized package of knowledge that sits dormant until needed. It is only loaded into the agent’s context when your specific request matches the skill’s description.

### Creating Skills

Creating a Skill in Antigravity follows a specific directory structure and file format. This standardization ensures that skills are portable and that the agent can reliably parse and execute them. The design is intentionally simple, relying on widely understood formats like Markdown and YAML, lowering the barrier to entry for developers wishing to extend their IDE’s capabilities.

### **Directory Structure**

Skills can be defined at two scopes, allowing for both project-specific and user-specific customizations :

  1. **Workspace Scope** : Located in `<workspace-root>/.agent/skills/`. These skills are available only within the specific project. This is ideal for project-specific scripts, such as deployment to a specific environment, database management for that app, or generating boilerplate code for a proprietary framework.
  2. **Global Scope** : Located in `~/.gemini/antigravity/skills/`. These skills are available across all projects on the user's machine. This is suitable for general utilities like "Format JSON," "Generate UUIDs," "Review Code Style," or integration with personal productivity tools.



A typical Skill directory looks like this :


    my-skill/
    ├── SKILL.md # The definition file
    ├── scripts/ # [Optional] Python, Bash, or Node scripts
        ├── run.py
        └── util.sh
    ├── references/ # [Optional] Documentation or templates
        └── api-docs.md
    └── assets/ # [Optional] Static assets (images, logos)


This structure separates concerns effectively. The logic (`scripts`) is separated from the instruction (`SKILL.md`) and the knowledge (`references`), mirroring standard software engineering practices.

### **The**`**SKILL.md**`**Definition File**

The `SKILL.md` file is the brain of the Skill. It tells the agent _what_ the skill is, _when_ to use it, and _how_ to execute it.

It consists of two parts:

  * YAML Frontmatter
  * Markdown Body.



**YAML Frontmatter**

This is the metadata layer. **It is the only part of the skill that is indexed by the agent’s high-level router**. When a user sends a prompt, the agent semantic-matches the prompt against the `description` fields of all available skills.


    ---
    name: database-inspector
    description: Use this skill when the user asks to query the database, check table schemas, or inspect user data in the local PostgreSQL instance.
    ---


**Key Fields:**

  * `name`: This is not mandatory. Must be unique within the scope. Lowercase, hyphens allowed (e.g., `postgres-query`, `pr-reviewer`). If its not provided, it will default to the directory name.
  * `description`: This is mandatory and the most important field. It functions as the "trigger phrase." It must be descriptive enough for the LLM to recognize semantic relevance. A vague description like "Database tools" is insufficient. A precise description like "Executes read-only SQL queries against the local PostgreSQL database to retrieve user or transaction data. Use this for debugging data states" ensures the skill is picked up correctly.



**The Markdown Body**

The body contains the instructions. This is “prompt engineering” persisted to a file. When the skill is activated, this content is injected into the agent’s context window.

The body should include:

  1. **Goal** : A clear statement of what the skill achieves.
  2. **Instructions** : Step-by-step logic.
  3. **Examples** : Few-shot examples of inputs and outputs to guide the model’s performance.
  4. **Constraints** : “Do not” rules (e.g., “Do not run DELETE queries”).



**Example**`SKILL.md`**Body:**


    Database Inspector

    Goal
    To safely query the local database and provide insights on the current data state.

    Instructions
    - Analyze the user's natural language request to understand the data need.
    - Formulate a valid SQL query.
      - CRITICAL: Only SELECT statements are allowed.
    - Use the script scripts/query_runner.py to execute the SQL.
      - Command: python scripts/query_runner.py "SELECT * FROM..."
    - Present the results in a Markdown table.

    Constraints
    - Never output raw user passwords or API keys.
    - If the query returns > 50 rows, summarize the data instead of listing it all.


Let’s add some skills now.

## Code Review Skill

This is an instruction-only skill i.e. we only need to create the `SKILL.md` file, that will contain the metadata and the skills instructions. Let's create a global skill that provides details to the agent to review code changes for bugs, style issues and best practices.

First up, create the directory that will contain this global skill.


    mkdir -p ~/.gemini/antigravity/skills/code-review


Create a `SKILL.md` file in the above directory with the content shown below:


    ---
    name: code-review
    description: Reviews code changes for bugs, style issues, and best practices. Use when reviewing PRs or checking code quality.
    ---

    # Code Review Skill
    When reviewing code, follow these steps:

    ## Review checklist
    1. **Correctness**: Does the code do what it's supposed to?
    2. **Edge cases**: Are error conditions handled?
    3. **Style**: Does it follow project conventions?
    4. **Performance**: Are there obvious inefficiencies?

    ## How to provide feedback
    - Be specific about what needs to change
    - Explain why, not just what
    - Suggest alternatives when possible


Notice that the `SKILL.md` file above contains the metadata (name and description) at the top and then the instructions. The Agent when it loads will only read the metadata for the skills that you have configured and it will load the instructions for the skill, only if required.

### Try it out

Create a file named `demo_bad_code.py` with the contents as shown below:


    import time

    def get_user_data(users, id):
       # Find user by ID
       for u in users:
           if u['id'] == id:
                return u
       return None
    def process_payments(items):
       total = 0
       for i in items:
           # Calculate tax
           tax = i['price'] * 0.1
           total = total + i['price'] + tax
           time.sleep(0.1) # Simulate slow network call

       return total
    def run_batch():
       users = [{'id': 1, 'name': 'Alice'}, {'id': 2, 'name': 'Bob'}]
       items = [{'price': 10}, {'price': 20}, {'price': 100}]

       u = get_user_data(users, 3)
       print("User found: " + u['name']) # Will crash if None

       print("Total: " + str(process_payments(items)))
    if __name__ == "__main__":
       run_batch()


Ask the agent: `review the @demo_bad_code.py file`. The Agent should identify the `code-review` skill, load the details and then perform the action as per the instructions given in the `code-review/SKILL.md` file.

A sample output is shown below:

![](https://miro.medium.com/v2/resize:fit:1400/0*gn1g0ThD_gtK3hJT.png)

## The Code Header Template Skill

Sometimes a skill needs to use a large block of static text (like a license header). Putting this text directly into the prompt is wasteful. Instead, we put it in a `resources/` folder and instruct the agent to read it only when necessary .

First up, create the directory that will contain this workspace skill.


    mkdir -p .agent/skills/license-header-adder/resources


Create `.agent/skills/license-header-adder/resources/HEADER.txt` with your license text:


    /*
     * Copyright (c) 2026 YOUR_COMPANY_NAME LLC.
     * All rights reserved.
     * This code is proprietary and confidential.
     */


Create a `.agent/skills/license-header-adder/SKILL.md` file with contents as shown below:


    ---
    name: license-header-adder
    description: Adds the standard corporate license header to new source files.
    ---

    # License Header Adder
    This skill ensures that all new source files have the correct copyright header.

    ## Instructions
    1. **Read the Template**: Read the content of `resources/HEADER.txt`.
    2. **Apply to File**: When creating a new file, prepend this exact content.
    3. **Adapt Syntax**:
       - For C-style languages (Java, TS), keep the `/* */` block.
       - For Python/Shell, convert to `#` comments.



### Try it out

Ask the Agent the following: `Create a new Python script named data_processor.py that prints 'Hello World'.`

The agent will read the template, convert the C-style comments to Python style, and prepend them to your new file automatically.

By creating these skills, you have effectively turned the generalist Gemini model into a specialist for your project. You have codified your best practices, whether it’s following your code review guidelines or license headers. Instead of repeatedly prompting the AI to “remember to add the license” or “fix the commit format,” the agent now instinctively knows how to work on your team.

## Securing the Agent — Allow List, Deny List and Browser security

Giving an AI agent access to your terminal and browser is a double-edged sword. It enables autonomous debugging and deployment but also opens vectors for **Prompt Injection** and **Data Exfiltration**.

If an agent can run `curl`, it can send your private keys to a rogue server. Antigravity addresses this through a granular permission system revolving around **Terminal Command Auto Execution** policies, **Allow Lists** , and **Deny Lists**.

When you first configure Antigravity, or via the settings menu, you must select a “Terminal Command Auto Execution” policy. This setting dictates the agent’s autonomy regarding shell commands.

You can view your current settings for this by going to `Antigravity — Settings` at the bottom right, then `Advanced Settings`. You should see the Terminal section for the Agent settings as shown below:

![](https://miro.medium.com/v2/resize:fit:1400/1*2YyNHGVNAog-Udi2OK81Lg.png)

You can see that currently the Auto Execution is set to **Auto**. Keep this table in mind, should you want to change this setting to something else:

![](https://miro.medium.com/v2/resize:fit:1400/1*ayWhTXsiTHAu80fAoIuvOA.png)

### Configuring the Allow List (Whitelisting)

The **Allow List** is used primarily with the **Off** policy. It represents a positive security model, meaning everything is forbidden unless expressly permitted. This is the most secure configuration.

**Step-by-Step Configuration**

  1. Set the Terminal Command Auto Execution setting to **Off**.
  2. Add the following commands in the **Allow List Terminal Commands** by clicking on the **Add** button next to it.




    ls -al
    npm run test


**Testing the Allow List:**

  * Ask the agent: `List the files in this directory` _._
  * The agent runs `ls` automatically.
  * Ask the agent: `Delete the <some file>. `In my case, I ask it to delete my `main.py` file.
  * The agent will attempt `rm <filepath>`, but Antigravity will block it and force a user review because `rm` is not in the allow list. Check out the behaviour below, where it waits for a human input to allow the operation.

![](https://miro.medium.com/v2/resize:fit:1400/1*PkzxIA7M4_Octutp354d_Q.png)

### Configuring the Deny List (Blacklisting)

The **Deny List** is the safeguard for the **Turbo** (and sometimes **Auto**) policy. It represents a negative security model, meaning everything is allowed unless expressly forbidden. This relies on the developer anticipating every possible danger, which is a risky proposition, but one that offers maximum speed.

### Step-by-Step Configuration

  1. Set the Terminal Command Auto Execution setting to **Turbo**.
  2. Add the following 2–3 commands in the **Deny List Terminal Commands** by clicking on the **Add** button next to it.




    rm
    del
    rmdir
    sudo
    curl
    wget
    ssh


**Testing the Allow List:**

  * Ask the agent: `Check the version of python` _._
  * The agent runs `python --version`automatically.
  * Ask the agent: `Download [www.google.com](<http://www.google.com/>) home page.`
  * The agent attempts `curl...`. Antigravity detects `curl` in the denylist and blocks execution, prompting you for manual approval as shown below:

![](https://miro.medium.com/v2/resize:fit:1400/1*6wNN0QRapY2pkhpvm0nJig.png)

### Browser Security

Antigravity’s ability to browse the web is a superpower, but also a vulnerability. An agent visiting a compromised documentation site could encounter a prompt injection attack.

To help prevent this, you can implement a **Browser URL Allowlist** for the browser agent.

You can view your current settings for this by going to `Antigravity — Settings` at the bottom right, then `Advanced Settings`. You should see the **Browser URL Allowlist** section for the **Browser settings** as shown below:

![](https://miro.medium.com/v2/resize:fit:1400/1*I3tRdM66e1LgMfS2FT2mBg.png)

Click on the **Open Allowlist File** and that opens up the file in the folder `HOME/.gemini/antigravity/browserAllowlist.txt`. A sample is shown below:

![](https://miro.medium.com/v2/resize:fit:1400/1*CFOPxEs3nLxg7yzp1xG13A.png)

You can ensure that only trusted domains are entered over here.

## Conclusion

Congratulations, you’ve successfully installed and understood how to use Antigravity, the Agent-first development platform. The different use cases that we tried should help you take your own requirements and explore how Antigravity can collaborate with you to complete them.

In addition to the use cases, we also looked at how you can make Antigravity use your own workflows and rules to ensure that the outputs are customized as per your processes, guidelines and standards.

We covered Agent Security and ensuring that a combination of Allow list, Deny list and the appropriate Terminal Execution mode, allows us to make the Agent ask us for confirmation instead of simply executing the terminal commands.

Finally, we touched upon ensuring that we understand Browser Security and configuring it to visit trusted sites.

## Reference docs

  * Official Site : <https://antigravity.google/>
  * Documentation: <https://antigravity.google/docs>
  * Usecases : <https://antigravity.google/use-cases>
  * Download : <https://antigravity.google/download>
  * Youtube Channel for Google Antigravity : <https://www.youtube.com/@googleantigravity>



## Google Cloud Platform Technology Updates

Tired of sifting through Google Cloud updates? My bi-weekly newsletter delivers key **Google Cloud Platform news and announcements** you need to know, to your inbox. [Subscribe now](<https://gcptechnuggets.substack.com/>).
