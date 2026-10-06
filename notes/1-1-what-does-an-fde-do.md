---
slug: what-does-an-fde-do
cluster: 1
cluster_title: "AI deployment mindset and FDE responsibilities"
order: 1
title: "What does a forward-deployed engineer actually do?"
teaser: "The job title sounds like software, and the code turns out to be the smallest slice of it."
access: free
minutes: 10
mission: "Week 0"
---

A forward-deployed engineer, or FDE, is an engineer who works at the customer's side of the table instead of behind a wall at the vendor. The name comes from the military idea of forward deployment: you put people near where the problem is, not near headquarters. In practice the FDE takes a business problem, builds something that solves it, proves that it works, and explains it to the people who pay for it. All four steps, one person or one small team, no handoffs.

That last part is what makes the role strange. In most software companies, work moves down an assembly line. One person talks to the customer and writes a document. A second person turns the document into a design. A third writes the code. A fourth tests it. Each handoff loses a little of what the customer actually said, the way a message loses detail passing through a line of people whispering. An FDE shortens the line to nothing.

Here is the analogy. Picture an engineer who builds a bridge, and who also walked the riverbank for a week beforehand, asked the villagers where they cross when the water is high, drove the first truck over on opening day, and then stood in front of the town council to say whether it was safe. Nobody doubts the engineering matters. But a perfectly built bridge in the wrong place is still a useless bridge, and only the person who walked the riverbank would have known.

```mermaid
flowchart LR
    W["Walk the riverbank (discover)"] -->|becomes a brief| B["Build the bridge"]
    B -->|is proven by| T["Drive the first truck (verify)"]
    T -->|is explained at| C["The town council (present)"]
    C -->|sends you back to| W
    P["One person, four jobs"] -.->|the FDE shape| W
```

## This happened to us

Deployed, the job board this course runs on, was built in exactly this shape. One small feature shows the whole loop.

Here is a real posting: "Senior Backend Engineer. Remote." Sounds open to the world. Read to the bottom and a quiet line says the company can only employ people in one country. A job seeker in Pune finds that line after an hour of writing the application, or worse, never hears back and never learns why.

**The riverbank walk.** Sitting with job seekers' actual question taught us it was never "what jobs exist?" They carry a sharper one: "can I, from where I sit, actually get this job?" No board we found answered it.

**The bridge.** So that question became a field a database can hold: who can apply, and from where. A pipeline now reads thousands of postings every night and fills that field in, posting by posting.

**The first truck over.** The same people then pulled up rows and read the original posting beside the pipeline's answer, by hand, fifty at a time. A pipeline that is quietly wrong is worse than no pipeline, because it answers the seeker's question with false confidence.

**The town council.** And the same people presented it: a filter on the site a seeker can click, and page copy where every count renders from the live database, because a hand-typed number is a promise nobody is checking.

One loop, one pair of shoes, four jobs. The cost was real: when a number looked wrong, there was no upstream team to blame and no downstream team to catch it. The builder had to be the doubter. That is slower in week one. It is also why the misunderstandings that normally surface months later, when someone finally sees the finished product, surfaced while they were still cheap to fix.

The code was never the hard part. The hard part was understanding one reader's question well enough that the code had a chance of answering it.

## See it yourself (2 minutes)

Open any AI chat and paste this:

> I want to build a tool that helps small shops track their inventory.
> Before you suggest anything, ask me the ten questions an engineer would
> need answered to avoid building the wrong thing. Do not write any code.

Read the questions. Notice how few of them are technical: who counts stock, when, what goes wrong today, what a mistake costs. Answer two of them honestly and see how your picture of the problem shifts. That shift is the work.

## What this means when you build

Across the program you will do all four jobs in every project: interview the problem, build the system, verify it against a measure you wrote down before you started, and present it in plain words. Your mentor skill will push you toward the verifying and presenting parts, because those are where most beginners stop early. Employers hiring for this role mostly cannot see your code at a glance, but they can read a clear account of a problem you understood and a result they can check.

When a mission feels like it has less coding than you expected, that is intended. The code is how you earn the right to the other three parts.

## Check yourself

You show a client a flawless working tool and they say, politely, that it solves the wrong problem. Of the four FDE jobs (interview the problem, build, verify, present), which one most likely got skipped?

<details><summary>Decide on your answer, then open</summary>

Interviewing the problem. A tool can be built and verified perfectly and still point at the wrong target, which is the bridge in the wrong place. Only someone who walked the riverbank, meaning sat with the problem first, would have caught it.

</details>
