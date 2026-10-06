---
slug: demo-vs-production
cluster: 1
cluster_title: "AI deployment mindset and FDE responsibilities"
order: 2
title: "Why does the demo always work and production always surprise you?"
teaser: "A demo runs on the data you chose. Production runs on all of it, and all of it includes the rows you never looked at."
access: free
minutes: 10
mission: "Week 0"
---

Every AI demo works, and the reason is selection. The person building a demo picks a handful of examples, tries them, tweaks the instructions until they behave, and shows you the ones that came out well. Nothing dishonest happened. But the examples were chosen by someone who already knew roughly what would work, so they tell you very little about what happens on the thousand examples nobody chose.

Production is the opposite situation. The system runs on everything that arrives: the malformed entries, the odd formats, the cases at the edges of your rule, the ones you did not think of because you never saw them. Two words help here. The **sample** is the small set you looked at. The **population** is everything the system will eventually meet. A demo describes the sample. Production lives in the population, and the gap between them is where surprises are stored.

You cannot remove the gap by being careful or clever. You can only measure it, which means running your system on real data before it matters and counting what happens.

Here is the analogy. Passing a driving test in an empty car park proves you can steer. It says almost nothing about rush hour in a city you have never visited, with buses, cyclists, and a delivery van stopped in the road. Nobody would let you drive for a living on the car park result alone. Yet that is exactly how many AI systems get approved.

## This happened to us

Our pipeline classifies job postings, and for some of them it sends the job for a second, more expensive look: a bigger model reads it more carefully. We wrote an escalation rule to pick out only the postings that deserved that extra attention. On paper the rule read sensibly. We expected it to select a small, specific slice.

Before running it for real, we ran a dry run: ask the rule how many rows it would send, without sending any. The count came back at 8,021. Only 151 of those actually qualified. The rest were jobs located in India that the rule was supposed to ignore and did not, because of how it treated their location data. The rule matched roughly fifty times more rows than we intended.

Nothing went wrong in the end, and that is the point. Because the check ran against the real data before any spend, we caught it for the price of reading one number. Had we launched on the strength of how the rule looked, the first signal would have been the bill for the second look on thousands of rows that never needed it. We got lucky in one respect: we checked. The rule would have looked just as sensible on the day we ran it and been just as wrong.

## See it yourself (2 minutes)

Open any AI chat and paste this:

> Here is a rule: "flag any customer message that mentions a refund."
> Invent twelve realistic customer messages, including some tricky ones,
> and tell me which the rule would flag. Then tell me which flags would be
> wrong and which real refund requests it would miss.

Look at the tricky ones: "I don't want a refund, I want it fixed," or "refunds policy link broken." A rule that sounded complete in one sentence leaks in both directions the moment real-looking text touches it. You have just built a very small production test.

## What this means when you build

In Project 1 you will be asked, before you build anything, to write down what you expect the system to do on real data and then compare it with what it did. Do the count first. Before any step that costs money or touches people, run the cheap version that only counts, and ask whether the number is the one you predicted. If it is off by a lot, the surprise has been moved to a moment when it costs almost nothing.

Plan to be surprised. The only choice you get is how expensive the surprise is.

## Check yourself

Your escalation rule was meant to send 151 postings for a second, expensive look. A dry run says it would send 8,021. Roughly how many times over budget would you have been, and what did catching it cost?

<details><summary>Decide on your answer, then open</summary>

About fifty-three times over, which matches the note's "roughly fifty times more rows than we intended." Catching it cost the price of reading one number from a count-only run. Launching on the strength of how the rule looked would have meant finding out from the bill.

</details>
