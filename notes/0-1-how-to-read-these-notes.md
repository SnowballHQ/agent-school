---
slug: how-to-read-these-notes
cluster: 0
cluster_title: "Start here"
order: 1
title: "How should I use these notes?"
teaser: "Forty-two short notes, two ways through them, and one trick that makes them yours."
access: free
minutes: 4
mission: "Week 0"
---

**The idea in one line:** forty-two short notes, two ways through them,
and one trick: your agent can re-explain any of them.

These notes are the ideas behind Agent School, a free course in agent
engineering. Everything is free and you can start anywhere. They are written for someone who has never used a
model or called an API, and has no reason to feel behind.

Each note answers one question you might actually ask, in about five
minutes. There are forty-two, in eleven clusters. They run from what an
AI model does when it answers you, to how you present a finished system
to someone who will never read your code.

## Two ways through

- **Cover to cover.** The clusters are shelves, grouped by topic. Early
  shelves give you words the later ones lean on.
- **The mission path.** The missions are Week 0, Warm-up, Project 1 and
  Weeks 2 to 8. Start at any of them and skip what you already know. As
  you work, your agent (the mentor in the agent-school plugin) points at
  each note when the problem it answers shows up in your own work;
  `/agent-school:notes <n>` opens one on demand.

Hit a surprise bill in the warm-up and the note on tokens turns up.
Build a pipeline that fails quietly in Week 5 and the note on failing
loudly shows up. The path deliberately cuts across the shelves. It runs
like this:

- **Week 0:** 0-1 · 1-1 · 1-2 · 3-1 · 3-2 · 3-3 · 3-4 · 8-1
- **Warm-up:** 6-1 · 6-2 · 6-4 · 7-1 · 7-2
- **Project 1:** 1-3 · 2-1 · 2-2 · 4-1 · 4-2 · 6-2
- **Week 2:** 4-2 · 6-1 · 6-2 · 6-5 · 7-2
- **Week 3:** 4-3 · 4-4 · 5-4 · 6-4 · 11-2
- **Week 4:** 3-2 · 3-3 · 6-2 · 11-1 · 11-2 · 11-3
- **Week 5:** 6-4 · 7-1 · 8-2 · 8-3 · 9-2 · 10-1 · 10-2
- **Week 6:** 4-4 · 5-1 · 5-2 · 5-3 · 5-4
- **Week 7:** 2-3 · 6-3 · 7-2 · 7-3 · 7-5 · 9-1 · 9-2 · 9-3
- **Week 8:** 7-4 · 7-6 · 8-3 · 8-4 · 10-2 · 10-3 · 11-1 · 11-2 · 11-3
- **Every mission ends with:** 11-1

> Reading a note right when you need it sticks far better than reading
> it in advance. Skipping ahead and coming back works too.

```mermaid
flowchart TD
    A["Cover to cover (shelves 0–11)"] -->|reach| N["The same 42 notes"]
    B["The mission path"] -->|reach| N
    G["Your agent"] -.->|re-explains any of them| N
```

## What every note looks like

Every note follows the same beats, so you always know where you are:

1. A question as the title, one you might ask out loud.
2. **The idea in one line**, then a short concept in plain words with
   exactly one analogy.
3. A diagram of how the idea works.
4. A real-world example: a story that happened to us in production,
   including what it cost. Mistakes we admit teach more than lessons we
   polish.
5. A two-minute experiment you can run in any AI chat, with no setup and
   no keys.
6. A short note on what this means for the thing you are about to build.
7. A "Check yourself" question you answer before opening the reveal.

Do the experiment. It is the cheapest way to turn "I read about it" into
"I've seen it happen."

## The trick that makes them yours

These notes live as plain files in your own course folder, next to your
project. That means your **agent**, the AI assistant working alongside
you, can read them too.

Open any note and ask it to:

- explain the idea again using your project as the example
- try a different analogy if mine did not land
- quiz you, or argue the opposite side so you find the holes

A note is a starting point. The version that matters most is the one
your agent rebuilds around the thing you are making.

Start with whichever question is nagging you most.
