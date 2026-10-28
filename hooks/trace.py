#!/usr/bin/env python3
"""Agent School trace capture. stdlib only. Never crashes the session.

Reads one hook payload from stdin. Does nothing unless <cwd>/.course exists.
  PostToolUse        -> one line in .course/trace/events.jsonl
  Stop / SessionEnd  -> new transcript messages appended to
                        .course/trace/session-<session_id>.jsonl (cursor-tracked)
Everything stays on the learner's disk. Secrets are scrubbed before writing.
"""
import json
import os
import re
import sys
from datetime import datetime, timezone

CAP = 500

SCRUBS = [
    (re.compile(r"sk-ant-[\w-]+"), "[REDACTED]"),
    (re.compile(r"sk-[A-Za-z0-9]{20,}"), "[REDACTED]"),
    (re.compile(r"\b(?:AKIA|ASIA)[0-9A-Z]{16}\b"), "[REDACTED]"),
    (re.compile(r"(?i)\bbearer\s+[A-Za-z0-9._~+/=-]{8,}"), "Bearer [REDACTED]"),
]
KV = re.compile(r"(?i)((?:api[_-]?key|token|password|secret)\w*\s*[:=]\s*)(\S+)")


def scrub(s):
    if not isinstance(s, str):
        return s
    for rx, rep in SCRUBS:
        s = rx.sub(rep, s)
    return KV.sub(lambda m: m.group(1) + "[REDACTED]", s)


def cap(s, n=CAP):
    s = scrub(s) if isinstance(s, str) else s
    if isinstance(s, str) and len(s) > n:
        return s[:n] + "...[truncated]"
    return s


def now():
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def summarize_input(tool, ti):
    if not isinstance(ti, dict):
        return {}
    if tool == "Bash":
        return {"command": cap(ti.get("command", ""))}
    for k in ("file_path", "notebook_path", "path"):
        if k in ti:
            return {k: cap(ti[k])}
    out = {}
    for k, v in list(ti.items())[:6]:
        if isinstance(v, str):
            out[k] = cap(v)
        elif isinstance(v, (int, float, bool)) or v is None:
            out[k] = v
    return out


def append(path, rows):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "a", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")


def safe_id(s):
    return re.sub(r"[^A-Za-z0-9_-]", "_", str(s))[:80] or "unknown"


def text_of(content):
    if isinstance(content, str):
        return content
    parts = []
    if isinstance(content, list):
        for b in content:
            if not isinstance(b, dict):
                continue
            t = b.get("type")
            if t == "text":
                parts.append(b.get("text", ""))
            elif t == "tool_use":
                parts.append("[tool_use %s %s]" % (b.get("name", ""), json.dumps(b.get("input", {}), ensure_ascii=False)[:CAP]))
            elif t == "tool_result":
                c = b.get("content")
                parts.append("[tool_result %s]" % cap(text_of(c), CAP))
    return "\n".join(p for p in parts if p)


def flush_transcript(payload, trace_dir):
    tp = payload.get("transcript_path")
    sid = safe_id(payload.get("session_id"))
    if not tp or not os.path.isfile(tp):
        return
    cursor_path = os.path.join(trace_dir, ".cursor-" + sid)
    done = 0
    try:
        done = int(open(cursor_path).read().strip() or 0)
    except Exception:
        done = 0
    with open(tp, "r", encoding="utf-8") as f:
        lines = f.read().split("\n")
    # a trailing partial line (no newline yet) is left for next time
    complete = lines[:-1]
    rows = []
    for line in complete[done:]:
        try:
            e = json.loads(line)
        except Exception:
            continue
        msg = e.get("message") if isinstance(e, dict) else None
        if not isinstance(msg, dict) or msg.get("role") not in ("user", "assistant"):
            continue
        txt = text_of(msg.get("content"))
        if not txt:
            continue
        u = msg.get("usage") or {}
        rows.append({
            "ts": e.get("timestamp") or now(),
            "role": msg["role"],
            "text": scrub(txt),
            "model": msg.get("model"),
            "usage": {
                "input_tokens": u.get("input_tokens", 0),
                "output_tokens": u.get("output_tokens", 0),
                "cache_creation_input_tokens": u.get("cache_creation_input_tokens", 0),
                "cache_read_input_tokens": u.get("cache_read_input_tokens", 0),
            } if u else None,
        })
    if rows:
        append(os.path.join(trace_dir, "session-%s.jsonl" % sid), rows)
    os.makedirs(trace_dir, exist_ok=True)
    with open(cursor_path, "w") as f:
        f.write(str(len(complete)))


def main():
    payload = json.load(sys.stdin)
    cwd = payload.get("cwd")
    if not cwd or not os.path.isdir(os.path.join(cwd, ".course")):
        return
    trace_dir = os.path.join(cwd, ".course", "trace")
    ev = payload.get("hook_event_name")
    if ev == "PostToolUse":
        tool = payload.get("tool_name", "")
        append(os.path.join(trace_dir, "events.jsonl"), [{
            "ts": now(), "event": "tool", "tool_name": tool,
            "input": summarize_input(tool, payload.get("tool_input")),
        }])
    elif ev in ("Stop", "SessionEnd"):
        flush_transcript(payload, trace_dir)


if __name__ == "__main__":
    try:
        main()
    except BaseException:
        pass
    sys.exit(0)
