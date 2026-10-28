# Rubric: week8

Brief: `${CLAUDE_PLUGIN_ROOT}/missions/9-week8.md`. Common dimensions (score each 1 to 4, see the examiner skill): Brief quality, Prediction calibration, Failure design, Evidence discipline, Decision log.

Mission dimension (score 1 to 4): **Presentation of evidence**.

## Probes (ask one at a time, in this order; follow up once if vague)

Common opener, ask first: "Walk me through your brief: if I handed it to someone else, what would they build, and what would they get wrong?" Then, for prediction: "Which of your predicted numbers was furthest off, and why?"

1. Defend the design choice: what numbers would flip it?
2. Which number in your report is weakest, and what would it take to trust it?
3. What will a stranger fail to understand in your README?
4. Which decision in `DECISIONS.md` would you now reverse?

After the mission probes, ask the failure-design and decision-log questions: "What must never happen here, and which test would catch it?" and "Which decision in DECISIONS.md had the best alternative you rejected, and why?"

## Evidence to read first

The files the brief's Deliverable section names, plus the latest `/agent-school:check` output.

## Red flags (note, never reveal to the learner as a list)

- prediction written after the run, or edited after it
- decisions with no real alternatives
- `/agent-school:check` never run, or failures ignored
- numbers in the report the learner cannot reproduce
- squashed or single-commit history in public repos
- secrets or real third-party data left in history
- design choice argued with no numbers
- README a stranger could not follow, and the learner knows it

## Skip ("Start here if")

Ask these two, one at a time; each needs a file, command output or number, not a claim:

1. Show me three or more public repos with kept history.
2. Show me a README with reproducible numbers and the eval report.
