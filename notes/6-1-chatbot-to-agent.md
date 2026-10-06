---
slug: chatbot-to-agent
cluster: 6
cluster_title: "Agentic AI workflows and automation design"
order: 1
title: "What turns a chatbot into an agent?"
teaser: "The jump from answering to acting is small in code and enormous in consequences."
access: free
minutes: 10
mission: "Warm-up"
---

A chatbot takes text in and gives text back. Whatever it says, nothing in the world changes until a human reads it and does something. An agent is a model that can do things itself. The word gets used loosely, so here's a precise version. An agent is three pieces working together: a goal, some tools, and a loop.

A tool is a function the model is allowed to call: look up a record, fetch a web page, send a message, change a row in a database. The model doesn't run the tool. It writes a request, something like "call the search tool with these words," and a program you wrote runs it and hands the result back. From the model's side, a tool is just another source of text that arrives mid-conversation.

The loop is what makes it an agent rather than a one-shot question. The cycle goes: the model looks at the goal and what it knows so far, picks a tool and calls it, reads the result, then decides what to do next. It repeats until it decides the goal is met, or until something stops it. Each trip around is a decision made on fresh information.

Here's the analogy. A pen pal and a house-sitter can both receive your instructions. Write to a pen pal "the plants look thirsty?" and you get a thoughtful letter back about watering, and the plants stay thirsty. Give a house-sitter a key and the same goal, "keep the plants alive while I'm away," and they check the soil, decide, water, and look again tomorrow. Same intelligence. What changed is the key and the ability to return.

That key is why agents deserve a different kind of care. A wrong chatbot answer costs a reader a moment of being misled, and the reader can check. A wrong agent action has already happened by the time anyone looks. Everything in the rest of this cluster, budgets, approval gates, safe reruns, is about the question that only exists once you hand over the key: what is this thing allowed to do when nobody is watching?

## This happened to us

This one is also the first mission you'll build, so it's worth telling from the builder's side. Our job-watch agent, the pattern behind your warm-up mission, works on our job board. It reads the live board through a tool, decides which postings matter for what it's watching, and acts on that decision.

Look at what each piece is doing. The goal is a sentence, something a person could say aloud. The tool is the only way the agent sees the board; it doesn't carry a copy of the postings in its head, and it doesn't guess at what's open today. It asks, and the tool answers from live data. The loop lets it look, decide, and look again as the board changes.

A detail worth taking from this: the agent is only as honest as its tool. If the tool returns a stale listing, the agent acts on a stale listing, and every decision downstream inherits the mistake. We'll come back to that when we talk about verifying what the tool returns.

There's no scar in this story, and the plainness is the point. Nothing here is mysterious. A goal, a tool that reads real data, a loop that decides what to do next. If you can say those three things about a system, you've described an agent.

## See it yourself (2 minutes)

In any AI chat, ask it to play out the loop on paper:

> Act as an agent with one tool: search_jobs(keyword), which returns a list of job titles. My goal is: find me one remote data role. Write out your loop step by step. At each step show what you think, which tool call you would make, and then wait. I'll paste in fake tool results. Start now.

Paste something like "search_jobs('data') returned: Data Analyst (onsite), Data Engineer (remote)" and see what it does next. Notice that each decision depends on what you fed back. Then try feeding it a misleading result and watch it act on it. That's the leap, in miniature.

## What this means when you build

Your warm-up mission is an agent with one tool and a clear goal, and the whole point is to watch the loop run. Before you build, write down what you expect each step of the loop to be, and which action in it could do harm if the agent got it wrong. That list, the actions with consequences, drives every safety decision in the projects that follow.
