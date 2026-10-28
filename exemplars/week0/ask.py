"""Week 0: send one question to a model, print the reply and the token counts.

Usage:  python3 ask.py "your question"

Needs three environment variables (no key ever goes in this file):
  LLM_API_KEY    your secret key
  LLM_BASE_URL   the service address, e.g. https://example.com/v1
  LLM_MODEL      the model name your provider gave you

Every call is also written to .course/trace/ so you can read it afterwards.
"""
import json
import os
import sys
import time
import urllib.request
from datetime import datetime, timezone

question = sys.argv[1]
key = os.environ["LLM_API_KEY"]
base = os.environ["LLM_BASE_URL"].rstrip("/")
model = os.environ["LLM_MODEL"]


def now():
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def append(path, row):
    os.makedirs(".course/trace", exist_ok=True)
    with open(path, "a", encoding="utf-8") as f:
        f.write(json.dumps(row, ensure_ascii=False) + "\n")


# 1. The request: a web address, a few headers, and a JSON body.
body = {
    "model": model,
    "messages": [{"role": "user", "content": question}],
    "max_completion_tokens": 400,  # a ceiling on the reply, so a mistake cannot get expensive
}
request = urllib.request.Request(
    base + "/chat/completions",
    data=json.dumps(body).encode(),
    headers={"Authorization": "Bearer " + key, "Content-Type": "application/json"},
)

# 2. Send it, and time it.
append(".course/trace/events.jsonl", {"ts": now(), "event": "tool", "tool_name": "Bash",
                              "input": {"command": "python3 ask.py " + json.dumps(question)}})
started = time.time()
with urllib.request.urlopen(request, timeout=60) as response:
    status = response.status
    reply = json.loads(response.read())
seconds = round(time.time() - started, 2)

# 3. Read the reply: the text, and the token counts.
text = reply["choices"][0]["message"]["content"]
usage = reply["usage"]

print(text)
print("--- tokens in: %d, out: %d, total: %d, seconds: %s" % (
    usage["prompt_tokens"], usage["completion_tokens"], usage["total_tokens"], seconds))

# 4. Save what happened. The secret key is never written down.
shown_headers = {"Authorization": "Bearer [REDACTED]", "Content-Type": "application/json"}
append(".course/trace/raw-calls.jsonl", {
    "ts": now(), "seconds": seconds,
    "request": {"method": "POST", "url": base + "/chat/completions",
                "headers": shown_headers, "body": body},
    "response": {"status": status, "body": reply},
})
append(".course/trace/session-week0.jsonl", {"ts": now(), "role": "user", "text": question, "model": None, "usage": None})
append(".course/trace/session-week0.jsonl", {
    "ts": now(), "role": "assistant", "text": text, "model": reply.get("model"),
    "usage": {"input_tokens": usage["prompt_tokens"], "output_tokens": usage["completion_tokens"],
              "cache_creation_input_tokens": 0, "cache_read_input_tokens": 0},
})
