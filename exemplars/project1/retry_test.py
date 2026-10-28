"""Retry-path test, offline. Feeds extract.py one deliberately malformed answer (format 'mostly in person',
not in the enum) followed by a good one, from replay/retry-test.jsonl (hand-written fixture, not a model call).
Prints the lines saved in RETRY_TEST.txt."""
import json
import sys

sys.argv = [sys.argv[0], "--replay", "replay/retry-test.jsonl"]
import extract  # noqa: E402

extract.log_usage = lambda *a: None   # the test must not add rows to usage.jsonl
text = open("postings/cfp-01.txt", encoding="utf-8").read()
answer, tokens, attempts = extract.extract_one("cfp-01.txt", text)
print("attempts: %d" % attempts)
print("result: %s" % ("recorded failure" if "failed" in answer else "valid"))
