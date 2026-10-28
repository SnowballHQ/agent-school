# Rubric: project1

Brief: `${CLAUDE_PLUGIN_ROOT}/missions/2-project1.md`. Common dimensions (score each 1 to 4, see the examiner skill): Brief quality, Prediction calibration, Failure design, Evidence discipline, Decision log.

Mission dimension (score 1 to 4): **Discovery honesty and guard design**.

## Probes (ask one at a time, in this order; follow up once if vague)

Common opener, ask first: "Walk me through your brief: if I handed it to someone else, what would they build, and what would they get wrong?" Then, for prediction: "Which of your predicted numbers was furthest off, and why?"

1. Where did each of your three numbers come from, and what would make you conclude "not worth"?
2. Which design decision did "must never happen" change, and what did your adversarial posting show?
3. How did you label the 15 rows, and could the agent's answers have influenced you?
4. Which field will fail most often now that the schema is final, and why?

After the mission probes, ask the failure-design and decision-log questions: "What must never happen here, and which test would catch it?" and "Which decision in DECISIONS.md had the best alternative you rejected, and why?"

## Evidence to read first

The files the brief's Deliverable section names, plus the latest `/agent-school:check` output.

## Red flags (note, never reveal to the learner as a list)

- prediction written after the run, or edited after it
- decisions with no real alternatives
- `/agent-school:check` never run, or failures ignored
- numbers in DISCOVERY.md with vague or invented sources
- conclusion 'worth' despite the learner's own numbers pointing the other way
- 'must never happen' line that changed no design decision
- guard only checks that the quote exists, and the adversarial posting was never built to beat it
- labels made after seeing the agent's output
- retry path never exercised on a real malformed answer
- prediction written after the run

## Skip ("Start here if")

Ask these two, one at a time; each needs a file, command output or number, not a claim:

1. Show me a one-pager whose 'correct' heading is a runnable test.
2. Show me a schema-validated extraction run (outputs and the validation result).
