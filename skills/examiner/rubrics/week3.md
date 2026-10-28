# Rubric: week3

Brief: `${CLAUDE_PLUGIN_ROOT}/missions/4-week3.md`. Common dimensions (score each 1 to 4, see the examiner skill): Brief quality, Prediction calibration, Failure design, Evidence discipline, Decision log.

Mission dimension (score 1 to 4): **Eval trustworthiness**.

## Probes (ask one at a time, in this order; follow up once if vague)

Common opener, ask first: "Walk me through your brief: if I handed it to someone else, what would they build, and what would they get wrong?" Then, for prediction: "Which of your predicted numbers was furthest off, and why?"

1. Did you ever see agent output before labelling a row? How would I know?
2. Your self-agreement is P%. What does that say about the ceiling of your eval?
3. Why is your held-back number different from your teaching number?
4. With fifteen held-back rows, how large a change counts as real?
5. Which rows would you relabel first?

After the mission probes, ask the failure-design and decision-log questions: "What must never happen here, and which test would catch it?" and "Which decision in DECISIONS.md had the best alternative you rejected, and why?"

## Evidence to read first

The files the brief's Deliverable section names, plus the latest `/agent-school:check` output.

## Red flags (note, never reveal to the learner as a list)

- prediction written after the run, or edited after it
- decisions with no real alternatives
- `/agent-school:check` never run, or failures ignored
- labels made after seeing agent output, with no way to show otherwise
- self-agreement low but the learner treats the eval as exact
- eval.py committed after prompt changes (baseline not real)
- held-back set used to tune the prompt
- a gap explanation that cites no row ids
- claims a change is real from one or two rows

## Skip ("Start here if")

Ask these two, one at a time; each needs a file, command output or number, not a claim:

1. Show me a labelled set split into teaching and held-back rows, and the eval script.
2. Show me the git log proving the eval was committed before your last prompt change.
