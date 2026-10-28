---
title: "Week 3: ground truth first, then the eval, then Project 2"
access: free
---
# Week 3: ground truth first, then the eval, then Project 2

Portfolio mission. Goes in your own repo. This week you stop trusting your own impression of your agent and start measuring it. Project 2 is the eval itself: a ruler you build, label and can reproduce.

**Start here if** you have an agent but only a feeling for how good it is. Skip it if you already have a teach/held-back labelled set and an eval committed before your last prompt change, and can show the git log.

## The three ideas you need

1. **Ground truth is a set of answers a person checked.** Accuracy is only as good as the labels behind it. Labels written after seeing the agent's answers are contaminated: you will quietly agree with it. Label first. Field note: "How do you know your new prompt is better and not just different?"
2. **Split your labels into a teaching set and a held-back set.** The **teaching set** is what you look at while improving the agent. The **held-back set** you do not read during improvement; you use it only to measure. Tune against the rows you measure on and the number rises while telling you nothing: **overfitting**. Same field note.
3. **Write the eval before you change anything.** An **eval** is a script that runs your agent on labeled rows and prints scores. Written first, the baseline is honest and every later change is judged by the same ruler. One run is a weak measurement; answers vary. Field note: "What happens when you run it twice?"

## Who builds

You do not type the code. You write the brief and the prediction; your agent builds; you read the trace and the result. Labelling is the exception: only you can do it, and nobody else will hold the labels, so the eval is only as trustworthy as your labelling.

## The mission

Write `BRIEF.md` for the eval first. It must contain a line `Key field: <name>` (your most important schema field) and a line `Agent files: <comma-separated paths>` (the prompt, tools and model config).

1. **Label forty rows** in `labels.csv`, your fifteen from Week 2 plus twenty-five more, without looking at agent output. Add a column `split`: twenty-five `teach`, fifteen `held`. Every legal value of the key field appears in both splits at least once; where your data cannot support that, add a line `unsupported: <value>` to `LABELER_CHECK.md`.
2. **Check yourself as a labeler.** Wait a day, relabel ten rows blind, and record in `LABELER_CHECK.md`: `Relabelled: 10`, `Changed: N`, `Agreement: P%` (your agreement with yourself, which caps how accurate any agent can look).
3. **Direct your agent to write `eval.py` and commit it before any change to the agent files.** It runs the agent twice on the held-back rows and prints accuracy per field and overall for each run, and how many rows changed between runs. The commit message must start with the baseline: `baseline: NN%`. Percentages are 0 to 100 everywhere (`85%`, never `0.85`). The check anchors on git: no commit that touches an agent file may fall between the commit that adds `labels.csv` and the commit that adds `eval.py`.
4. **Measure v0.** Record `Teach accuracy:` and `Held-back accuracy:` separately in `RESULTS.md`, as 0 to 100 percentages. The overall number `eval.py` prints must land within 10 points of your held-back number.
5. **Close the loop.** `GAP.md` has `Predicted:`, `Held-back:` and `Teach:` lines and an explanation of the gaps that points at specific row ids. A large gap with an explanation that cites rows is a good result.
6. **Say what you do not trust.** In `DECISIONS.md`, log how many labels you would redo and what would make you distrust the eval.

Count tokens from `usage`; two runs over fifteen rows cost little.

## Deliverable and how it's checked

`BRIEF.md`, `PREDICTION.md`, `DECISIONS.md`, `labels.csv`, `LABELER_CHECK.md`, `eval.py`, `RESULTS.md`, `GAP.md`. There is no hidden grader. The check verifies the ruler is reproducible; the examiner probes whether it can be trusted. Run `/agent-school:check week3` and `/agent-school:defend`; neither blocks the next mission, and the examiner writes its feedback into `COURSE_PROGRESS.md`.

```
Local check contract: /agent-school:check week3
- `labels.csv` has exactly 40 data rows; header holds `id`, `split` and every schema field; `split` is `teach` for exactly 25 rows and `held` for exactly 15
- for the field on the `Key field:` line of `BRIEF.md`, every value present appears in both splits, or `LABELER_CHECK.md` has `unsupported: <value>` for it
- `LABELER_CHECK.md` has `^Relabelled: 10$`, `^Changed: \d+$`, `^Agreement: \d+(\.\d+)?%$`, and Agreement equals 100*(10-Changed)/10
- `git log`: the first commit adding `eval.py` has a message containing `baseline: \d+(\.\d+)?%` (accuracies are 0-100), and no commit that touches a path listed on the `Agent files:` line falls after the first commit adding `labels.csv` and before the commit adding `eval.py` (no `labels.csv` commit means only the message is checked)
- `python eval.py` exits 0 and prints `^overall: \d+(\.\d+)?%`, one `^field <name>: \d+(\.\d+)?%` per schema field, and `^changed between runs: \d+$`
- the printed `overall:` value (0-100) is within 10 points of `Held-back accuracy:` (0-100) in `RESULTS.md`
- `RESULTS.md` has `^Teach accuracy: \d+(\.\d+)?%` and `^Held-back accuracy: \d+(\.\d+)?%`
- `GAP.md` has `^Predicted: \d+`, `^Held-back: \d+`, `^Teach: \d+`, and contains >=1 `id` value from `labels.csv`
- `PREDICTION.md` has `## Predictions` (3 numbered lines) and `## The gap`; `DECISIONS.md` has >=2 entries
```

Examiner probes:
- Did you ever see agent output before labelling a row? How would I know?
- Your self-agreement is P%. What does that say about the ceiling of your eval?
- Why is your held-back number different from your teaching number?
- With fifteen held-back rows, how large a change counts as real?
- Which rows would you relabel first?
- Were the labels written before you saw the agent's output? Show me the commit order.

## Predict before you build

Write these in `PREDICTION.md` under `## Predictions` before you run the eval.

1. Your accuracy on the held-back rows, as a number.
2. Whether your teaching-set number will be higher or lower than the held-back one, and by roughly how many points.
3. How many held-back rows will change answer between your two runs.

## When you're stuck

- Run `/agent-school:mission` to resume. Run `/agent-school:notes 4-4` if you cannot tell whether a change helped. Run `/agent-school:notes 5-4` to see how a question-answering system is measured; it matters again in Week 6.
- Notes: 4-4, 6-4, 5-4, 4-3, 11-2.
- Run `/agent-school:defend` when you think you are done, even if the check fails; the feedback is the point.
