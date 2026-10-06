---
slug: what-are-tokens
cluster: 3
cluster_title: "GenAI and LLM foundations"
order: 2
title: "What are tokens, and why does anyone count them?"
teaser: "Every AI system has a meter running in both directions. Most people only discover this when the bill arrives."
access: free
minutes: 10
mission: "Week 0"
---

A model doesn't read words. It reads tokens: small chunks of text, usually
three or four characters, sometimes a whole short word. "Engineering"
might be two or three tokens. "The" is one. This note you're reading is
roughly a thousand of them.

Why should you care about a unit of text you'll never see? Because tokens
are what you pay for, in both directions. Everything you send to a model
is counted and billed, and everything it says back is counted and billed
again. The size of a model's memory is measured in tokens too, which the
next note covers.

Here's the analogy. In the telegram era, messages were priced per word,
and it changed how people wrote: "ARRIVING MONDAY" instead of "I expect
to arrive at the station on Monday." Tokens are the telegram words of AI,
with two differences. The meter runs in both directions, on what you send
and what comes back. And the meter is invisible unless you go looking for
it.

```interactive
widget: tokens
```

That second difference is where the trouble lives.

## This happened to us

Our job board classifies thousands of postings a night: is this job
remote, which country can apply, how senior is it. We moved part of that
work to a small, cheap model to save money. The task was simple, pick
answers from a fixed list, and the model was more than capable of it.

Then we watched a single job get processed. Fifty seconds. For a task
that should take five.

The model was spending around five thousand tokens per job on hidden
reasoning, thinking out loud to itself before answering, the way such
models are tuned to do by default. None of that reasoning appeared in the
output. None of it was needed for a pick-from-a-list task. All of it was
billed. We were paying for an essay and receiving a single word.

One configuration line turned the hidden reasoning off. The same work
became about ten times cheaper and ten times faster. Nothing about the
answers changed.

The lesson wasn't that the model misbehaved. It did exactly what it was
configured to do. The lesson was that nobody on our side had looked at
the meter until the behaviour was slow enough to notice. If the task had
been a little faster, we might have paid the 10× for months.

## See it yourself (2 minutes)

Open your agent, or any AI chat, and paste a paragraph from anything you
have handy. Then ask:

> Roughly how many tokens is the text I just pasted, and how many words?
> Explain the difference using my own text as the example. Then show me
> the same request I could have made in half the tokens.

Look at the ratio it reports, and look at its shortened version of your
request. You've just done, by hand, what cost-conscious systems do by
design.

## What this means when you build

Every agent you ship in this program has this meter running, and the
gateway we give you reads it per mission. You'll write a prediction
before each build: what should this cost? Then you'll compare it with
what it did cost. The gap between those two numbers is where you'll find
things like our fifty-second job.

By Project 2 you'll be reporting cost per document next to accuracy, as
one number employers can check. Treat tokens the way the telegram writers
treated words, and that number will be one you're glad to publish.

## Check yourself

Suppose the classifier from the war story runs on 3,000 jobs a night, each burning about 5,000 hidden reasoning tokens. How many tokens are billed each night for reasoning nobody reads?

<details><summary>Decide on your answer, then open</summary>

About 15 million (3,000 x 5,000), all of it billed, for answers that were a single word. Turning the hidden reasoning off cut cost and time roughly tenfold with no change in the answers, which is why you look at the meter before the bill arrives.

</details>
