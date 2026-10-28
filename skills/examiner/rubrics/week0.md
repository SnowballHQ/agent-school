# Rubric: week0

Brief: `${CLAUDE_PLUGIN_ROOT}/missions/0-week0.md`. Common dimensions (score each 1 to 4, see the examiner skill): Brief quality, Prediction calibration, Failure design, Evidence discipline, Decision log.

Mission dimension (score 1 to 4): **Setup and trace reading**.

## Probes (ask one at a time, in this order; follow up once if vague)

Common opener, ask first: "Walk me through your brief: if I handed it to someone else, what would they build, and what would they get wrong?" Then, for prediction: "Which of your predicted numbers was furthest off, and why?"

1. Which option did you choose, and what would make you switch?
2. Why did your "must never happen" line say what it says, and how did you check it?
3. Show me where in the trace the stop reason is. What would a different value mean?
4. Why did your prediction differ from the measured token count?

After the mission probes, ask the failure-design and decision-log questions: "What must never happen here, and which test would catch it?" and "Which decision in DECISIONS.md had the best alternative you rejected, and why?"

## Evidence to read first

The files the brief's Deliverable section names, plus the latest `/agent-school:check` output.

## Red flags (note, never reveal to the learner as a list)

- prediction written after the run, or edited after it
- decisions with no real alternatives
- `/agent-school:check` never run, or failures ignored
- prediction written after the runs (check file order or the learner's own admission)
- model choice recorded but no reason given, or chosen only because it was the default
- 'must never happen' line is generic and was never checked (e.g. the key-in-file scan was not run)
- trace notes copied from the agent without the learner opening the trace
- check skipped or never run

## Skip ("Start here if")

Ask these two, one at a time; each needs a file, command output or number, not a claim:

1. Show me a script that calls a model and prints token counts.
2. Show me the log or trace of one of its runs.
