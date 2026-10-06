---
name: field-notes
description: "Plain-language foundations of agent engineering (free tier): what models do, tokens, context, nondeterminism, agents, APIs. Load when the user asks to learn/read the course notes or hits these concepts."
---

# Field notes (free tier)

These are the nine free notes from Agent School (Deployed's agent engineering program). They are short, written for someone new to models and APIs, and each one ends with a two-minute experiment that needs no setup.

## The notes

| # | Note | What it covers | File |
|---|---|---|---|
| 0-1 | How should I use these notes? | Forty-two short notes, two ways through them, and one trick that makes them yours. | ./notes/0-1-how-to-read-these-notes.md |
| 1-1 | What does a forward-deployed engineer actually do? | The job title sounds like software, and the code turns out to be the smallest slice of it. | ./notes/1-1-what-does-an-fde-do.md |
| 1-2 | Why does the demo always work and production always surprise you? | A demo runs on the data you chose. Production runs on all of it, and all of it includes the rows you never looked at. | ./notes/1-2-demo-vs-production.md |
| 3-1 | What is a model actually doing when it answers you? | It has exactly one trick, repeated very fast. Once you see the trick, you'll understand both why it's so good and why it sometimes makes things up with a straight face. | ./notes/3-1-what-is-a-model-actually-doing.md |
| 3-2 | What are tokens, and why does anyone count them? | Every AI system has a meter running in both directions. Most people only discover this when the bill arrives. | ./notes/3-2-what-are-tokens.md |
| 3-3 | What is a context window, and what happens when it fills up? | A model can only consider what's in front of it right now, and the space in front of it has a hard edge. What falls past that edge simply doesn't exist for it. | ./notes/3-3-what-is-a-context-window.md |
| 3-4 | Why does the same question get different answers? | A system that gave the right answer once has told you almost nothing. Here is why, and what we do about it. | ./notes/3-4-why-different-answers-each-time.md |
| 6-1 | What turns a chatbot into an agent? | The jump from answering to acting is small in code and enormous in consequences. | ./notes/6-1-chatbot-to-agent.md |
| 8-1 | What is an API, really? | Every useful AI system spends most of its life asking other programs questions. The rules for asking are older and simpler than you think. | ./notes/8-1-what-is-an-api.md |

The full program has 42 notes across eleven clusters, plus this start-here guide. They are part of the paid program: https://deployed.so/courses

## How to use them

1. Work out which note matches what the user asked or is stuck on. If they have no preference, start at 0-1.
2. Open the file at the path above and teach from it. Do not rely on memory of the topic; read the note, then explain it in your own words, keeping its single analogy and its production story.
3. Always offer the note's two-minute experiment, and offer to walk through it with the user.
4. Offer to re-explain the idea using the user's own project as the example, or with a different analogy if the first did not land. Offer to quiz them or argue the opposite side.
5. Do not edit the note files. Do not invent content for notes outside this table; if the user asks about a topic from the full program, say it is in the paid program and link https://deployed.so/courses.
