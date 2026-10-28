"""Job-posting extraction: three model calls per posting (majority vote), two fields out.

Reads every .md/.txt/.json file in $HARNESS_INPUT_DIR, asks a model for
remote_type and seniority, and writes one JSON line per file to $HARNESS_OUTPUT.
Standard library only. Calls the OpenAI-compatible chat endpoint using the
env vars the harness injects (OPENAI_BASE_URL, OPENAI_API_KEY).
"""
import hashlib
import json
import os
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

REMOTE_TYPES = ["remote", "hybrid", "onsite"]
SENIORITIES = ["intern", "junior", "mid", "senior", "lead", "staff", "exec"]

PROMPT = """You label job postings. Read the posting and answer with ONLY a JSON object:
{"remote_type": "...", "seniority": "..."}

remote_type must be one of: remote, hybrid, onsite.
- remote: work can be done from home / anywhere / remote-first.
- hybrid: some days in an office and some days away.
- onsite: the person must be at a workplace. If the posting never says, pick onsite.

seniority must be one of: intern, junior, mid, senior, lead, staff, exec.
- intern: internships, student or trainee roles.
- junior: entry level, associate, early-career, 0-2 years.
- mid: a normal individual contributor with no seniority word, about 2-5 years.
- senior: the word Senior, or about 5+ years of experience.
- lead: team lead, manager, head of a team or function.
- staff: Staff, Principal, or Distinguished individual contributor.
- exec: Director, VP, C-level.
Use the job title first, then the years of experience asked for.

Posting:
"""

VOTES = 3
CACHE_DIR = Path(os.environ.get("P2_CACHE", "/tmp/p2_exemplar_cache"))


def call_model(text, model, base, key):
    """One non-streaming chat call. Returns (reply_text, usage_dict)."""
    body = {"model": model, "temperature": 0, "seed": 7,
            "messages": [{"role": "user", "content": PROMPT + text[:12000]}]}
    for attempt in range(4):
        req = urllib.request.Request(
            base.rstrip("/") + "/chat/completions",
            data=json.dumps(body).encode(),
            headers={"Content-Type": "application/json", "Authorization": "Bearer " + key})
        try:
            with urllib.request.urlopen(req, timeout=120) as r:
                data = json.load(r)
            return data["choices"][0]["message"]["content"], data.get("usage", {})
        except urllib.error.HTTPError as e:
            detail = e.read().decode(errors="replace")
            if e.code == 400 and "temperature" in detail and "temperature" in body:
                del body["temperature"]          # some models only allow their default
                continue
            if e.code == 400 and "seed" in detail and "seed" in body:
                del body["seed"]
                continue
            if e.code in (429, 500, 502, 503):
                time.sleep(2 ** attempt)
                continue
            raise
    raise RuntimeError("model call failed after retries")


def clean(reply):
    """Turn the model's reply into two valid labels (empty string if unusable)."""
    try:
        s = reply[reply.index("{"): reply.rindex("}") + 1]
        obj = json.loads(s)
    except ValueError:
        obj = {}
    rt = str(obj.get("remote_type", "")).strip().lower()
    se = str(obj.get("seniority", "")).strip().lower()
    return (rt if rt in REMOTE_TYPES else "", se if se in SENIORITIES else "")


def majority(values):
    values = [v for v in values if v]
    if not values:
        return ""
    return sorted(set(values), key=lambda v: (-values.count(v), v))[0]


def label(text, model, base, key, trace):
    """Cached by content hash so a second run returns the same answer."""
    h = hashlib.sha256((model + PROMPT + text).encode()).hexdigest()
    cache = CACHE_DIR / (h + ".json")
    if cache.is_file():
        return json.loads(cache.read_text()), True
    # Ask VOTES times and keep the most common answer per field. Ties go to the
    # label that sorts first, so the choice never depends on call order.
    answers = []
    for _ in range(VOTES):
        reply, usage = call_model(text, model, base, key)
        answers.append(clean(reply))
        trace.append({"raw_reply": reply, "usage": usage})
    result = {"remote_type": majority([a[0] for a in answers]),
              "seniority": majority([a[1] for a in answers])}
    try:
        CACHE_DIR.mkdir(parents=True, exist_ok=True)
        cache.write_text(json.dumps(result))
    except OSError:
        pass
    return result, False


def main():
    in_dir = Path(os.environ["HARNESS_INPUT_DIR"])
    out_path = Path(os.environ["HARNESS_OUTPUT"])
    base = os.environ.get("OPENAI_BASE_URL", "https://api.openai.com/v1")
    key = os.environ["OPENAI_API_KEY"]
    model = os.environ.get("OPENAI_LUNA_MODEL") or os.environ.get("P2_MODEL", "")
    trace_path = os.environ.get("P2_TRACE")
    files = sorted(p for p in in_dir.iterdir() if p.suffix in (".md", ".txt", ".json"))
    lines, trace_lines = [], []
    for p in files:
        trace = []
        res, cached = label(p.read_text(errors="replace"), model, base, key, trace)
        lines.append(json.dumps({"id": p.stem, **res}, sort_keys=True))
        trace_lines.append(json.dumps({"id": p.stem, "cached": cached, "calls": trace}, sort_keys=True))
    out_path.write_text("\n".join(lines) + "\n")
    if trace_path:
        Path(trace_path).write_text("\n".join(trace_lines) + "\n")
    print(f"wrote {len(lines)} lines", file=sys.stderr)


if __name__ == "__main__":
    main()
