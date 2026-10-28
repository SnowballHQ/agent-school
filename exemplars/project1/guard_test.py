"""Guard test, offline. Takes the adversarial posting (a real quote, a wrong answer) and the model's saved reply for it
from trace/session-p1.jsonl, applies extract.py's guard, and compares with the hand label (deadline = null)."""
import json
import sys

sys.argv = [sys.argv[0], "--replay", "none"]
import extract  # noqa: E402

posting = "adversarial/cfp-16-two-deadlines.txt"
text = open(posting, encoding="utf-8").read()
rows = [json.loads(l) for l in open("trace/session-p1.jsonl")]
asked = [r for r in rows if r["role"] == "user"]
replies = [r for r in rows if r["role"] == "assistant"]
reply = json.loads(replies[[i for i, r in enumerate(asked) if r["text"].startswith("[cfp-16.txt]")][0]]["text"])
kept, dropped = extract.apply_guard(reply, text)
print("posting: " + posting)
print("model answer: %s  quote: %r" % (reply["submission_deadline"], reply["deadline_quote"]))
print("quote appears in posting: %s" % (not dropped))
print("guard output: %s   hand label: null" % kept["submission_deadline"])
print("result: %s" % ("caught" if kept["submission_deadline"] is None else "missed"))
