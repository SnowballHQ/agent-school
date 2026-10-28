---
title: "Week 6: Project 3, a knowledge agent that cites and refuses"
access: free
---
# Week 6: Project 3, a knowledge agent that cites and refuses

Portfolio mission. Goes in your own repo. You build an agent that answers questions about your own work, shows where each answer came from, and says "I don't know" when the documents do not say.

**Start here if** you have used a chatbot over documents but never measured whether it refuses when it should. Skip it if you already have a golden question set written before the retriever, with separate answer, citation and refusal scores.

## The three ideas you need

1. **Retrieval means finding the few passages worth reading before the model answers.** You cannot paste everything in, because the window fills and the model loses the thread. So you split documents into **chunks**, turn each into an **embedding** (a list of numbers that places similar meaning close together), and at question time fetch the nearest chunks. Field notes: "Why can't you just paste all the company's documents into the prompt?" and "What is retrieval, and what is an embedding?"
2. **A grounded answer carries its evidence, and sometimes it is a refusal.** A **citation** names the exact passage that supports a claim. When the passages do not contain the answer, the right output is a refusal, not a plausible guess. Field note: "Why must a knowledge agent sometimes refuse to answer?"
3. **Measure three things and never blend them.** A system can answer right but cite the wrong passage, or cite well but refuse too much. You report **answer correctness**, **citation correctness** and **refusal correctness** separately. Field note: "How do you measure a system that answers questions?"

## Who builds

You do not type the code. You write the brief and the prediction; your agent builds; you read the trace and the result. The golden questions are yours alone: they are the ruler.

## The mission

**The corpus is your own project:** `ONE_PAGER.md`, `MEMO.md`, `RESULTS.md`, `GAP.md`, `CHURN_REPORT.md`, `PREDICTION.md` files, `DECISIONS.md`, and traces. Put copies in `corpus/`. You need at least fifteen documents; if you have fewer, add field notes you used most and mark them `borrowed`. List all in `corpus_manifest.csv` (`doc_id,path,origin`, origin `own` or `borrowed`).

1. **Write the golden questions first.** `golden.csv` (`id,question,answerable,expected_answer,doc_id,passage`): twenty questions. Fourteen answerable, each with the exact `passage` copied from its document; six unanswerable (`answerable` = `no`, other columns blank), things your documents never say but sound like they might. Commit it before the retriever. `BRIEF.md` carries a line `Retriever files: <paths>`.
2. **Build the agent.** Chunk, embed, store chunks in a local file, retrieve the top few, answer using only those. `README.md` has `Ask:` (a command taking the question as its argument) that prints JSON with `answer`, `citations` (list of `{doc_id, quote}`) and `refused`: a single JSON object as the last line of stdout (logs may come before it). The check runs all twenty golden questions.
3. **Put the refusal rule in code.** If the best chunk scores below `refusal_threshold` in `config.json`, refuse without asking the model. Your code is the wall; the prompt is a second chance.
4. **Score it.** `score_p3.py` prints five lines: `answer correctness: k/14` and `wrongly refused: k/14` (from your judgments in `judgments.csv`: `id,answer_correct,citation_supports`, yes or no), `citation quote-exists: k/N` (every quote appears word for word in the cited document), `citation supports-claim (human, 10 sampled): k/10` (open the passage and judge), `refusal correctness: k/6`. Never fold them together. The quote layer proves the citation is real, not that it backs the claim.
5. **`REPORT.md`** pastes the five lines verbatim in a fenced block and has a section `## A wrong answer with a real citation`: name one, or say you looked and how.

Every model call appends a line to `calls.jsonl` as in Week 4; count from `usage` or your provider's equivalent. Log choices in `DECISIONS.md`.

## Deliverable and how it's checked

`BRIEF.md`, `PREDICTION.md`, `DECISIONS.md`, `golden.csv`, `corpus/`, `corpus_manifest.csv`, the agent, `config.json`, `score_p3.py`, `judgments.csv`, `REPORT.md`. Two local feedback surfaces, and neither blocks the next mission: `/agent-school:check week6` and `/agent-school:defend`, which writes feedback on your reasoning into `COURSE_PROGRESS.md`.

```
Local check contract: /agent-school:check week6
- `corpus_manifest.csv` header `doc_id,path,origin`; >=15 rows; every `path` exists; `origin` is `own` or `borrowed`
- `golden.csv` has 20 rows with the header above: 14 `answerable`=yes, 6 `answerable`=no; for the 14, `passage` appears verbatim (whitespace-normalised) in the file of its `doc_id`
- `git log`: the first commit adding `golden.csv` precedes the first commit touching any path on the `Retriever files:` line of `BRIEF.md`
- `Ask:` run on all 20 golden questions prints, as the last line of stdout, a single JSON object with string `answer`, list `citations` of `{doc_id, quote}`, boolean `refused`; when `refused` is true `citations` is empty
- every citation `quote` is a substring of the file for its `doc_id`
- `config.json` has numeric `refusal_threshold`; asking the nonsense question `zzqx vvkp 7731` returns `refused: true` and adds 0 lines to `calls.jsonl`
- `python score_p3.py` exits 0 and prints lines matching `^answer correctness: \d+/14$`, `^wrongly refused: \d+/14$`, `^citation quote-exists: \d+/\d+$`, `^citation supports-claim \(human, 10 sampled\): \d+/10$`, `^refusal correctness: \d+/6$`
- `judgments.csv` has >=14 rows with `answer_correct` filled and exactly 10 with `citation_supports` filled
- `REPORT.md` contains each of the five printed lines verbatim, and a `## A wrong answer with a real citation` section with >=1 non-empty line
- `BRIEF.md` four sections plus `Retriever files:`; `PREDICTION.md` has `## Predictions` (3 numbered lines) and `## The gap`; `DECISIONS.md` has >=2 entries
```

Examiner probes:
- Which unanswerable question was your agent most tempted to answer, and what stopped it?
- How did you choose the refusal threshold, and on which questions?
- Show me an answer whose citation is real but does not back the claim.
- Did judging your own answers bias the correctness score? How would you reduce that?

## Predict before you build

Write these in `PREDICTION.md` under `## Predictions` first.

1. Of your fourteen answerable questions, how many will the agent answer correctly?
2. Of your six unanswerable ones, how many will it refuse, and which will tempt it most?
3. Which of your scores will be lowest?

## When you're stuck

- Run `/agent-school:mission` to resume. Run `/agent-school:notes 5-2` if retrieval keeps returning the wrong chunk. Run `/agent-school:notes 5-3` if your agent never refuses.
- Notes: 5-1, 5-2, 5-3, 5-4, 4-4.
- Run `/agent-school:defend` when you think you are done, even if the check fails; the feedback is the point.
