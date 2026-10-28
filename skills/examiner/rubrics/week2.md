# Rubric: week2

Brief: `${CLAUDE_PLUGIN_ROOT}/missions/3-week2.md`. Common dimensions (score each 1 to 4, see the examiner skill): Brief quality, Prediction calibration, Failure design, Evidence discipline, Decision log.

Mission dimension (score 1 to 4): **Walls, budget and trust in fifteen labels**.

## Probes (ask one at a time, in this order; follow up once if vague)

Common opener, ask first: "Walk me through your brief: if I handed it to someone else, what would they build, and what would they get wrong?" Then, for prediction: "Which of your predicted numbers was furthest off, and why?"

1. Which wall fired most often, and did that match your prediction?
2. What stops the loop if the model never calls `submit_record`?
3. How far can you trust fifteen labels, and how did you choose your error estimate?
4. What did you decide the model must not decide?

After the mission probes, ask the failure-design and decision-log questions: "What must never happen here, and which test would catch it?" and "Which decision in DECISIONS.md had the best alternative you rejected, and why?"

## Evidence to read first

The files the brief's Deliverable section names, plus the latest `/agent-school:check` output.

## Red flags (note, never reveal to the learner as a list)

- prediction written after the run, or edited after it
- decisions with no real alternatives
- `/agent-school:check` never run, or failures ignored
- budget cap enforced only in the prompt, not in code
- no answer to what stops the loop when submit_record is never called
- kill check skipped or counts typed by hand rather than measured
- error estimate with no reasoning
- labels made after seeing output, or reused when the schema changed
- prediction written after the run

## Skip ("Start here if")

Ask these two, one at a time; each needs a file, command output or number, not a claim:

1. Show me a tool-calling loop with hard budget caps in code (the config and the line that enforces it).
2. Show me the trace of a row through that loop.
