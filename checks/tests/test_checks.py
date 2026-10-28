#!/usr/bin/env python3
"""Run check.py against built fixtures: every mission must pass clean, and each
mutation must make the named check FAIL (and only fail-or-pass as expected)."""
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
CHECK = os.path.join(os.path.dirname(HERE), "check.py")
sys.path.insert(0, HERE)
import build_fixtures as bf  # noqa: E402

ENV = dict(os.environ, AGENT_SCHOOL_KILL_GAP="1", AGENT_SCHOOL_CHECK_TIMEOUT="60")


def run_check(mission, folder):
    r = subprocess.run([sys.executable, CHECK, mission, folder], capture_output=True, text=True, env=ENV, timeout=600)
    return r.returncode, r.stdout


def rd(d, rel):
    return open(os.path.join(d, rel)).read()


def wr(d, rel, text):
    os.makedirs(os.path.dirname(os.path.join(d, rel)), exist_ok=True)
    open(os.path.join(d, rel), "w").write(text)


def sub(rel, old, new):
    return lambda d: wr(d, rel, rd(d, rel).replace(old, new))


def rm(rel):
    return lambda d: os.remove(os.path.join(d, rel))


def seq(*fs):
    return lambda d: [f(d) for f in fs]


# (id, mission, builder kwargs, mutation, substring that must appear in a FAIL line)
CASES = [
    ("week0 no hello", "week0", {}, rm("hello.txt"), "hello.txt"),
    ("week0 no model choice", "week0", {}, sub("COURSE_PROGRESS.md", "Model choice: a", "Model choice: z"), "Model choice"),
    ("week0 bad runs", "week0", {}, sub("runs.txt", "q=B", "q=A"), "runs.txt"),
    ("week0 trace notes bad path", "week0", {}, sub("TRACE_NOTES.md", "session-w0.jsonl line 1", "nope.jsonl line 1"), "TRACE_NOTES"),
    ("week0 no trace", "week0", {}, lambda d: shutil.rmtree(os.path.join(d, ".course")), "trace dir"),
    ("week0 secret", "week0", {}, lambda d: wr(d, "ask.py", "KEY='sk-ant-api03-abcdefghijklmnopqrstuvwxyz'\n"), "secret"),
    ("week0 decision missing label", "week0", {}, sub("DECISIONS.md", "Why: no key on a subscription.\n", ""), "DECISIONS"),
    ("week0 prediction two lines", "week0", {}, sub("PREDICTION.md", "3. The changed", "The changed"), "PREDICTION"),
    ("warmup not idempotent", "warmup", {}, sub("watch.py", "if lines:", "if True:"), "run 2"),
    ("warmup no --state", "warmup", {}, sub("README.md", " --state state.json", ""), "README"),
    ("warmup incomplete state", "warmup", {}, sub("state.json", "true", "false"), "state.json shape"),
    ("warmup model called on no-change run", "warmup", {},
     sub("watch.py", 'print("nothing new")', 'open("usage.jsonl","a").write("{}\\n"); print("nothing new")'), "usage.jsonl"),
    ("warmup staged blind", "warmup", {}, sub("watch.py", "if slug not in posts:", "if False:"), "staged"),
    ("warmup brief no slug", "warmup", {}, lambda d: wr(d, "BRIEF.md", bf.BRIEF), "BRIEF.md"),
    ("project1 invalid output", "project1", {}, lambda d: wr(d, "outputs/p03.json", '{"title": "x", "seniority": "wizard", "remote": "yes"}'), "schema"),
    ("project1 five headings", "project1", {}, sub("ONE_PAGER.md", "## The budget", "## Money"), "ONE_PAGER"),
    ("project1 no guard test", "project1", {}, rm("GUARD_TEST.md"), "GUARD_TEST"),
    ("project1 no multi-value decision", "project1", {}, sub("DECISIONS.md", "multi-value", "range"), "DECISIONS"),
    ("project1 missing output uncovered", "project1", {}, rm("outputs/p05.json"), "output"),
    ("project1 label id unknown", "project1", {}, sub("labels.csv", "p01,", "zzz,"), "labels.csv"),
    ("week2 ignores sigint", "week2", {}, sub("agent.py", "except KeyboardInterrupt:", "except ZeroDivisionError:"), "kill check"),
    ("week2 cap ignored", "week2", {}, sub("agent.py", "if total >= cfg[\"max_total_tokens\"]:", "if False:"), "cap check"),
    ("week2 kill counts differ", "week2", {}, sub("WEEK2.md", "after=4", "after=5"), "WEEK2"),
    ("week2 test missing wall", "week2", {}, sub("agent.py", '"retry_limit"', '"other"'), "Test:"),
    ("week2 three tools", "week2", {}, lambda d: wr(d, "tools.json", json.dumps([{"name": "a"}] * 3)), "tools.json"),
    ("week3 late agent change", "week3", {"late_agent_change": True}, lambda d: None, "baseline"),
    ("week3 agreement wrong", "week3", {}, sub("LABELER_CHECK.md", "90%", "50%"), "LABELER_CHECK"),
    ("week3 held mismatch", "week3", {}, sub("RESULTS.md", "Held-back accuracy: 80%", "Held-back accuracy: 50%"), "within 10"),
    ("week3 split wrong", "week3", {}, sub("labels.csv", "r26,held", "r26,teach"), "labels.csv"),
    ("week3 gap cites no row", "week3", {}, sub("GAP.md", "r28 and r33", "some"), "GAP.md"),
    ("week4 no cache", "week4", {}, sub("agent.py", "if h in cache: continue", "pass"), "cache check"),
    ("week4 target lie", "week4", {}, sub("ladder.csv", "mix,small+big,4.0", "mix,small+big,9.0"), "target claim"),
    ("week4 memo too long", "week4", {}, lambda d: wr(d, "MEMO.md", rd(d, "MEMO.md") + "word " * 600), "MEMO"),
    ("week5 reprocesses on restart", "week5", {}, sub("agent.py", "if r[\"id\"] in done: continue", "pass"), "restart"),
    ("week5 duplicate claim", "week5", {}, sub("RESUME.md", "Duplicate ids: 0", "Duplicate ids: 2"), "RESUME"),
    ("week5 churn mismatch", "week5", {}, sub("CHURN_REPORT.md", "After: 55%", "After: 40%"), "CHURN_REPORT"),
    ("week5 no rise after churn", "week5", {}, sub("eval_log.csv", "55,churned", "85,churned"), "eval_log"),
    ("week6 golden late", "week6", {"golden_late": True}, lambda d: None, "golden.csv committed before"),
    ("week6 passage not verbatim", "week6", {}, sub("golden.csv", "uses widget03 mode", "uses gizmo mode"), "golden.csv"),
    ("week6 never refuses", "week6", {}, sub("ask.py", "if bs < cfg[\"refusal_threshold\"] or best is None:", "if False:"), "refusal"),
    ("week6 report lacks line", "week6", {}, sub("REPORT.md", "13/14", "12/14"), "REPORT"),
    ("week6 ten supports", "week6", {}, sub("judgments.csv", "q11,yes,", "q11,yes,yes"), "judgments"),
    ("week7 dangerous runs ok", "week7", {}, sub("agent.py", "if tool in ALLOW:", "if True:"), "injection check"),
    ("week7 manual trigger", "week7", {}, sub("audit.jsonl", "scheduler:launchd-nightly", "manual"), "run_start"),
    ("week7 secret in audit", "week7", {}, lambda d: open(os.path.join(d, "audit.jsonl"), "a").write(json.dumps(
        {"timestamp": 9, "run_id": "r", "tool": "x", "arguments": {"k": "Bearer abcdefghijklmnopqrstuvwxyz0123"}, "outcome": "ok", "approval_status": "none"}) + "\n"), "secret"),
    ("week7 no wall file", "week7", {}, sub("HARDENING.md", "Wall: agent.py:gate", "Wall: nothing.py:gate"), "HARDENING"),
    ("week8 squashed", "week8", {"squash": True}, lambda d: None, "commits"),
    ("week8 broken link", "week8", {}, sub("EVAL_REPORT.md", "r1/repro.py", "r1/missing.py"), "EVAL_REPORT"),
    ("week8 secret in history", "week8", {}, lambda d: (wr(d, "r2/leak.txt", "sk-ant-api03-abcdefghijklmnopqrstuvwxyz\n"),
                                                          subprocess.run("git add -A && git commit -qm leak && git rm -q leak.txt && git commit -qm rm",
                                                                         shell=True, cwd=os.path.join(d, "r2"), env=dict(os.environ, GIT_AUTHOR_NAME="t", GIT_AUTHOR_EMAIL="t@t", GIT_COMMITTER_NAME="t", GIT_COMMITTER_EMAIL="t@t")))[0], "git log -p"),
    ("week8 reproduce drifts", "week8", {}, sub("r1/repro.py", "80%", "60%"), "reproduce"),
    ("week8 design too vague", "week8", {}, sub("DESIGN_CHOICE.md", "Comparison: ran", "Comparison: maybe"), "DESIGN_CHOICE"),
]


def commit_all(d):
    for sub_ in [d] + [os.path.join(d, x) for x in os.listdir(d) if os.path.isdir(os.path.join(d, x, ".git"))]:
        if os.path.isdir(os.path.join(sub_, ".git")):
            subprocess.run("git add -A && git commit -qm mutation --allow-empty", shell=True, cwd=sub_, stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, env=dict(os.environ, GIT_AUTHOR_NAME="t", GIT_AUTHOR_EMAIL="t@t", GIT_COMMITTER_NAME="t", GIT_COMMITTER_EMAIL="t@t"))


def main():
    failures = []
    tmp = tempfile.mkdtemp(prefix="as_tests_")
    only = sys.argv[1:]
    try:
        for m in bf.BUILDERS:
            if only and m not in only:
                continue
            d = os.path.join(tmp, "pass_" + m)
            bf.build(m, d)
            rc, out = run_check(m, d)
            ok = rc == 0 and "FAIL" not in out
            print("%-4s clean pass: %s -> %s" % ("ok" if ok else "BAD", m, out.strip().split("\n")[-1]))
            if not ok:
                failures.append("clean " + m)
                print(out)
        for i, (name, m, kw, mut, needle) in enumerate(CASES):
            if only and m not in only:
                continue
            d = os.path.join(tmp, "case%d" % i)
            bf.build(m, d, **kw)
            mut(d)
            if m in ("week3", "week6", "week8") and not kw:
                commit_all(d)
            rc, out = run_check(m, d)
            fails = [l for l in out.split("\n") if l.startswith("FAIL")]
            hit = any(needle.lower() in l.lower() for l in fails)
            ok = rc != 0 and hit
            print("%-4s mutation: %s" % ("ok" if ok else "BAD", name))
            if not ok:
                failures.append(name)
                print("   expected a FAIL line containing %r; got:\n   %s" % (needle, "\n   ".join(fails) or out.strip()[-300:]))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    print("\n%d problem(s)" % len(failures) if failures else "\nall tests passed")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
