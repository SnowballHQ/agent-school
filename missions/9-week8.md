---
title: "Week 8: the capstone, split, packaged and defended"
access: free
---
# Week 8: the capstone, split, packaged and defended

Portfolio mission. Goes in your own repos, in public. You turn eight weeks of work in one folder into repositories a stranger can understand, run and trust.

**Start here if** you have work worth showing but it lives in one tangled folder. Skip it if you already have three or more public repos with kept history, a README with reproducible numbers and an eval report.

## The three ideas you need

1. **A portfolio is evidence a stranger can verify in ten minutes.** A **README** answers what it does, how well, at what cost and how to run it, in the first screen. Numbers sit next to the command that reproduces them. Field notes: "How do you present numbers people can check?" and "How do you explain your system to someone who will never read the code?"
2. **History is part of the proof.** Splitting one journey repo into several should keep each project's real commits. A single commit named "initial" suggests the work was pasted in. Real history shows the eval written before the improvement, the churn caught, the fix. Field note: "What is a decision trace, and why write down the why?"
3. **One agent becomes several only when a measured problem says so.** Splitting adds cost, delay and new ways to fail, because agents pass messages and can disagree. It pays when the pieces need different tools, different permissions, or a second opinion. Field notes: "When does one agent become several?" and "What breaks when two systems quietly disagree?"

## Who builds

You do not type the code. You write the brief and the prediction; your agent builds and runs the git commands; you read the result. The design choice and the presentation are yours.

## The mission

Write `BRIEF.md` first (what the split must produce, what must never happen: a secret or a squashed history in a public repo). Log choices in `DECISIONS.md`.

1. **Split your journey repo** into at least three repos, for example extraction (Projects 1 and 2), knowledge agent (Project 3), hardened unattended agent (Project 4). Use `git filter-repo --path <folder>` on a fresh clone, or `git subtree split --prefix <folder>`. Do not squash. List them in `REPOS.md`: one `Repo: <local path or URL>` per line, the main one first, and `Split date: YYYY-MM-DD`.
2. **Clean each repo.** Remove secrets (read the hits of `git log -p | grep -iE "key|token|secret"`), use sample or synthetic data where the real data belongs to someone else, add a `LICENSE` and a `.env.example`.
3. **Write each README** with sections `## Results` (a table), `## Reproduce` (the exact command in a fenced block), `## Cost` (per thousand rows, from `usage` or your provider's equivalent), `## Limits`, and a link to the eval report. The main repo's README has a line `Reproduce: <command>` that prints `overall: NN%`.
4. **`EVAL_REPORT.md`** in the main repo, sections `## Held-back accuracy`, `## Cost curve`, `## Knowledge agent scores`, `## Churn event`, `## Injection test`, plus `Held-back accuracy: NN%`. Every number links to the file or command that produced it; a number you cannot reproduce is deleted.
5. **`DESIGN_CHOICE.md`**, one page: for your capstone, one agent or several? First line under `## Answer` is `one agent` or `several`; then `## Evidence`, `## What would change my mind`, and `Comparison: ran` or `Comparison: argued`. If you ran one (a planner plus a reviewer against your single agent on the held-back rows), save `comparison.csv` (`config,accuracy,cost_per_1k`).
6. **`PRESENTATION.md`**: an eight-minute script under `## Problem`, `## Result`, `## Cost`, `## The failure I am proudest of catching`, `## Design choice`. Record it if you like.

## Deliverable and how it's checked

Three or more public repos with README and history, `REPOS.md`, `EVAL_REPORT.md`, `DESIGN_CHOICE.md`, `PRESENTATION.md`, `BRIEF.md`, `PREDICTION.md`, `DECISIONS.md`. "Defended" means `/agent-school:defend`: the examiner asks you to defend the design choice with your own numbers and writes its feedback into `COURSE_PROGRESS.md`. Nothing blocks you, and there is no outside score: your own reproduced numbers are the evidence. The local check is `/agent-school:check week8`.

```
Local check contract: /agent-school:check week8
- `REPOS.md` has >=3 lines `^Repo: \S+` and `^Split date: \d{4}-\d{2}-\d{2}$`
- for each `Repo:` that is a local path: it is a git repo, `git rev-list --count HEAD` >= 10, and the first commit's date is earlier than `Split date` by >=1 day
- for each `Repo:` that is a URL: needs network access; `git ls-remote <url>` succeeds with no credentials (public check); it is then cloned and checked as above
- each repo has `README.md` with `## Results`, `## Reproduce` (followed by a fenced block), `## Cost`, `## Limits`; a `LICENSE` or `^License:` line; `.env.example`; no `.env` in `git ls-files`
- no match of `sk-[A-Za-z0-9_-]{20,}|AKIA[0-9A-Z]{16}|ghp_[A-Za-z0-9]{30,}` in the output of `git log -p --all` run in each repo (120 s limit per repo)
- `EVAL_REPORT.md` has the five `## ` sections above and `^Held-back accuracy: \d+(\.\d+)?%`; every relative markdown link target exists
- reproduce check: fresh clone of the main repo, run its `Reproduce:` command; stdout has `^overall: (\d+(\.\d+)?)%` within 2 points of `Held-back accuracy` in `EVAL_REPORT.md`
- `DESIGN_CHOICE.md` is <=500 words, has `## Answer` whose first non-empty line is `one agent` or `several`, `## Evidence`, `## What would change my mind` (>=1 line), and `^Comparison: (ran|argued)$`; if `ran`, `comparison.csv` has >=2 rows and header `config,accuracy,cost_per_1k`
- `PRESENTATION.md` has the five `## ` headings above and 600 to 1300 words
- `BRIEF.md` four sections; `PREDICTION.md` has `## Predictions` (3 numbered lines) and `## The gap`; `DECISIONS.md` has >=2 entries
```

Examiner probes:
- Defend the design choice: what numbers would flip it?
- Which number in your report is weakest, and what would it take to trust it?
- What will a stranger fail to understand in your README?
- Which decision in `DECISIONS.md` would you now reverse?

## Predict before you build

Write these in `PREDICTION.md` under `## Predictions` first.

1. How many commits will your oldest project have after the split?
2. Will a multi-agent version beat your single agent on accuracy, cost, both or neither?
3. What is the first question a stranger will ask that your README fails to answer?

## When you're stuck

- Run `/agent-school:mission` to resume. Run `/agent-school:notes 11-1` if your README reads like a diary. Run `/agent-school:notes 7-6` before you write the design choice.
- Notes: 7-6, 11-1, 11-2, 11-3, 10-2, 10-3, 8-3, 8-4.
- Run `/agent-school:defend` when you think you are done, even if the check fails; the feedback is the point.
