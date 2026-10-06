---
slug: why-different-answers-each-time
cluster: 3
cluster_title: "GenAI and LLM foundations"
order: 4
title: "Why does the same question get different answers?"
teaser: "A system that gave the right answer once has told you almost nothing. Here is why, and what we do about it."
access: free
minutes: 10
mission: "Week 0"
---

Ask a model the same question twice and you may get two different answers.
Sometimes the wording differs. Sometimes the conclusion does. If you come
from ordinary programming, where the same input produces the same output,
this feels like a bug. It is a design choice, and understanding it changes
how you test everything.

Recall from the earlier notes that a model writes by predicting the next
chunk of text. What we skipped is what that prediction looks like. The
model doesn't produce one chunk. It produces a score for every possible
next chunk, which can be turned into probabilities: "the" is quite likely,
"a" a bit less, "banana" almost impossible. Something then has to choose.

The choosing step is called sampling, and it's a weighted roll. Here's the
analogy. Imagine a die with thousands of faces, where likelier chunks
occupy more of the surface. Most rolls land on one of the favourites, but
a less likely face turns up now and then. The answer you receive is one
particular sequence of rolls, and the next time you ask, the die is rolled
again. Early rolls matter more than they appear to: once one chunk is
chosen, every later prediction builds on it, so a different early roll
sends the whole answer down a different road.

```interactive
widget: sampling
```

Many tools expose a setting called temperature, which controls how
much the die is loaded. Low temperature squeezes the odds toward the
favourite, so answers become steadier and more repetitive. High
temperature flattens the odds, and answers become more varied and
sometimes odder. Even at the lowest setting, results can still wobble a
little, because the surrounding machinery has its own sources of tiny
variation. Treat "identical every time" as something to verify, never
something to assume.

Is the variation good or bad? It depends on the job. For brainstorming
names or drafting a poem, you want the die. For deciding whether a job
posting is remote, you want the same answer every time, or at least a
known rate of disagreement. That rate is the quantity worth caring about.

This leads to the principle that matters most in this note: a system that
is right once is not yet a system. If you ran your classifier on one
posting, got the right label, and shipped it, you've learned that it can
be right. You haven't learned how often it is right, and a single draw
from a die can't tell you that. Run it many times on the same inputs and
look at how stable the answers are. Stability is evidence. A lucky run is
an anecdote.

## This happened to us

Our pipelines process large batches of job postings overnight, and in the
early builds we kept finding that a second run did not leave the database
the way the first run had. Reruns created duplicate rows.

To be exact about the cause: those duplicates came from our own code
writing the same record again, and the model's dice weren't to blame. But
the lesson widened the moment we looked at it, because a rerun can go
wrong in two separate ways. The code might repeat itself, as ours did. And
the model might answer differently the second time, so that "the same
run" produces different data. Both look the same from outside: you ran it
twice and the world changed.

So we wrote a doctrine and now apply it to everything. Run the pipeline
twice, then compare the database state before and after. They should
match, or differ in ways you can explain. Then kill the pipeline halfway
through a run, restart it, and check that resuming corrupts nothing: no
double rows, no half-written ones. Until a pipeline passes both checks,
we don't count it as built.

## See it yourself (2 minutes)

Open your agent or any AI chat. Start a fresh conversation for each try,
or use the regenerate button, and send this same message five times:

> Job title: "Junior Data Analyst, hybrid, London office 2 days a week."
> Is this job remote? Answer with exactly one word: yes, no, or partly.

Tally your five answers. If they all agree, try a murkier title, such as
"Customer Success Lead, flexible location, some travel." Watch where the
agreement frays. The posting where answers split is the one a real
pipeline would need extra care for.

## What this means when you build

From your first mission, you'll run each of your builds more than once
and keep the results side by side. Your prediction sheet will include a
line for stability: if I run this ten times, how many answers will match?
You'll also meet the run-twice check as an explicit gate in later
missions. Treat the first correct answer as a hypothesis. The pattern
across ten runs is the finding.

## Check yourself

You run your pipeline twice and find duplicate rows. The model's answers were identical both times, and you had set temperature to its lowest. Is sampling the culprit, yes or no? What is?

<details><summary>Decide on your answer, then open</summary>

No. Identical answers rule the dice out, and the duplicates came from our own code writing the same record again. A rerun can go wrong two ways, repeated code or a different model answer, so you check the database before and after a second run and after a mid-run kill.

</details>
