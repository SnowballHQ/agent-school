# Rubric: week5

Brief: `${CLAUDE_PLUGIN_ROOT}/missions/6-week5.md`. Common dimensions (score each 1 to 4, see the examiner skill): Brief quality, Prediction calibration, Failure design, Evidence discipline, Decision log.

Mission dimension (score 1 to 4): **Crash and drift thinking**.

## Probes (ask one at a time, in this order; follow up once if vague)

Common opener, ask first: "Walk me through your brief: if I handed it to someone else, what would they build, and what would they get wrong?" Then, for prediction: "Which of your predicted numbers was furthest off, and why?"

1. What exactly happens if the kill lands during a checkpoint write?
2. How did your eval notice the churn, and how many days would a real one have gone unseen?
3. Is your guard checking shape only, or also meaning? What would it miss?
4. Which row, if reprocessed, would cost the most?

After the mission probes, ask the failure-design and decision-log questions: "What must never happen here, and which test would catch it?" and "Which decision in DECISIONS.md had the best alternative you rejected, and why?"

## Evidence to read first

The files the brief's Deliverable section names, plus the latest `/agent-school:check` output.

## Red flags (note, never reveal to the learner as a list)

- prediction written after the run, or edited after it
- decisions with no real alternatives
- `/agent-school:check` never run, or failures ignored
- checkpoint written non-atomically and the learner cannot say what a kill mid-write does
- eval run only once, so churn cannot be noticed
- guard checks shape only and the learner does not know what it would miss
- self-made churn that is too easy to catch
- prediction written after the run

## Skip ("Start here if")

Ask these two, one at a time; each needs a file, command output or number, not a claim:

1. Show me a checkpointed run surviving kill -9 with zero duplicate ids.
2. Show me the guard and its test.
