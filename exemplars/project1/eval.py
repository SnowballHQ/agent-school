"""Score outputs/ against labels/sample.json. Prints per-field accuracy and the confident-wrong deadline count.
Passes (exit 0) only if cell accuracy >= 90% AND confident-wrong deadlines == 0."""
import json
import re
import sys

FIELDS = ["is_cfp", "conference_name", "submission_deadline", "event_start_date",
          "format", "audience_level", "travel_support"]


def norm(s):
    return re.sub(r"[^a-z0-9]", "", s.lower())


def same(field, got, want):
    if field == "conference_name" and got and want:       # tolerant: one name contains the other
        return norm(want) in norm(got) or norm(got) in norm(want)
    return got == want


labels = json.load(open("labels/sample.json"))
right = {f: 0 for f in FIELDS}
confident_wrong, missing, wrong_cells = [], [], []
for row in labels:
    try:
        out = json.load(open("outputs/" + row["file"].replace(".txt", ".json")))
    except FileNotFoundError:
        missing.append(row["file"])
        continue
    for f in FIELDS:
        if same(f, out.get(f), row[f]):
            right[f] += 1
        else:
            wrong_cells.append((row["file"], f, out.get(f), row[f]))
    if out.get("submission_deadline") and out["submission_deadline"] != row["submission_deadline"]:
        confident_wrong.append((row["file"], out["submission_deadline"], row["submission_deadline"]))

n = len(labels)
cells = n * len(FIELDS)
total_right = sum(right.values())
print("rows labelled: %d   rows with no output (failed): %d" % (n, len(missing)))
for f in FIELDS:
    print("  %-20s %2d/%d  %3.0f%%" % (f, right[f], n, 100.0 * right[f] / n))
print("cell accuracy: %d/%d = %.1f%%" % (total_right, cells, 100.0 * total_right / cells))
print("confident-wrong deadlines: %d" % len(confident_wrong))
for c in confident_wrong:
    print("   %s gave %s, label says %s" % c)
print("wrong cells:")
for c in wrong_cells:
    print("   %s  %-18s got %r, want %r" % c)
ok = total_right / cells >= 0.9 and not confident_wrong
print("PASS" if ok else "FAIL")
sys.exit(0 if ok else 1)
