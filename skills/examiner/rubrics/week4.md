# Rubric: week4

Brief: `${CLAUDE_PLUGIN_ROOT}/missions/5-week4.md`. Common dimensions (score each 1 to 4, see the examiner skill): Brief quality, Prediction calibration, Failure design, Evidence discipline, Decision log.

Mission dimension (score 1 to 4): **Cost/accuracy reasoning**.

## Probes (ask one at a time, in this order; follow up once if vague)

Common opener, ask first: "Walk me through your brief: if I handed it to someone else, what would they build, and what would they get wrong?" Then, for prediction: "Which of your predicted numbers was furthest off, and why?"

1. Which step tolerated the cheapest model, and what is your evidence?
2. How would the curve change on rows unlike your held-back set?
3. What does "per month" assume about volume, and where did that number come from?
4. Would the reader who said yes or no have changed your recommendation?

After the mission probes, ask the failure-design and decision-log questions: "What must never happen here, and which test would catch it?" and "Which decision in DECISIONS.md had the best alternative you rejected, and why?"

## Evidence to read first

The files the brief's Deliverable section names, plus the latest `/agent-school:check` output.

## Red flags (note, never reveal to the learner as a list)

- prediction written after the run, or edited after it
- decisions with no real alternatives
- `/agent-school:check` never run, or failures ignored
- cost estimated rather than computed from logged usage
- cheaper configuration compared on different rows
- cache that hides a change in one row, or is never tested
- per-month figure with an invented volume
- memo written for a reader who has not read the code, but no reader asked
- target not reached and no honest Why not

## Skip ("Start here if")

Ask these two, one at a time; each needs a file, command output or number, not a claim:

1. Show me a cost/accuracy table across at least three model configurations, built from logged token counts.
2. Show me the cache working: a rerun with zero model calls.
