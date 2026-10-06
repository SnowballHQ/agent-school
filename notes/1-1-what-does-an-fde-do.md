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

## This happened to us

We built Deployed, our own job board for remote roles, with exactly this shape. The same people who sat with the problem, working out what someone looking for remote work needs from a job board and where existing ones fall short, were the people who built the pipeline that collects and cleans the listings. The same people then verified it, checking the output against reality instead of trusting it. And the same people presented it, explaining what the board does and what it does not.

The honest cost of this is that we had nobody to hand a mistake to. When a number looked wrong, there was no upstream team to blame and no downstream team to catch it, so the person who built the thing was also the person who had to doubt it. That is slower in the first week. It is also why the misunderstandings that usually surface months into a project, when someone finally sees the finished product, tended to surface while we were still holding the pen.

We would not claim the code was the hard part. The part that mattered was understanding the problem well enough that the code had a chance of pointing the right way.

## See it yourself (2 minutes)

Open any AI chat and paste this:

> I want to build a tool that helps small shops track their inventory.
> Before you suggest anything, ask me the ten questions an engineer would
> need answered to avoid building the wrong thing. Do not write any code.

Read the questions. Notice how few of them are technical: who counts stock, when, what goes wrong today, what a mistake costs. Answer two of them honestly and see how your picture of the problem shifts. That shift is the work.

## What this means when you build

Across the program you will do all four jobs in every project: interview the problem, build the system, verify it against a measure you wrote down before you started, and present it in plain words. Your mentor skill will push you toward the verifying and presenting parts, because those are where most beginners stop early. Employers hiring for this role mostly cannot see your code at a glance, but they can read a clear account of a problem you understood and a result they can check.

When a mission feels like it has less coding than you expected, that is intended. The code is how you earn the right to the other three parts.
