"""Score a pipeline output file against the dev labels.

Usage: python3 eval.py runs/run1.jsonl [labels.json]
Metrics mirror the grader: precision and recall are averaged over label values
(macro), accuracy is the plain share correct, coverage is the share of postings
that got any answer.
"""
import json
import sys
from pathlib import Path

DEFAULT_LABELS = Path(__file__).resolve().parents[3] / "harness/datasets/p2/dev/labels.json"
FIELDS = ["remote_type", "seniority"]


def norm(v):
    return "" if v is None else str(v).strip().lower()


def score(outputs, labels, fields):
    result = {}
    for f in fields:
        gold = {i: norm(l[f]) for i, l in labels.items() if f in l}
        pred = {i: norm(outputs.get(i, {}).get(f)) for i in gold}
        correct = sum(1 for i in gold if pred[i] and pred[i] == gold[i])
        precs, recs = [], []
        for v in {p for p in pred.values() if p}:
            said = [i for i in gold if pred[i] == v]
            precs.append(sum(1 for i in said if gold[i] == v) / len(said))
        for v in set(gold.values()):
            real = [i for i in gold if gold[i] == v]
            recs.append(sum(1 for i in real if pred[i] == v) / len(real))
        result[f] = {"precision": round(sum(precs) / len(precs), 4) if precs else 0.0,
                     "recall": round(sum(recs) / len(recs), 4) if recs else 0.0,
                     "accuracy": round(correct / len(gold), 4) if gold else 0.0,
                     "n": len(gold)}
    return result


def main():
    out_file = Path(sys.argv[1])
    labels = json.loads(Path(sys.argv[2] if len(sys.argv) > 2 else DEFAULT_LABELS).read_text())
    outputs = {}
    for line in out_file.read_text().splitlines():
        if line.strip():
            rec = json.loads(line)
            outputs[str(rec["id"])] = rec
    scores = score(outputs, labels, FIELDS)
    cov = sum(1 for i in labels if i in outputs) / len(labels)
    print(f"coverage {cov:.2f}")
    for f, s in scores.items():
        print(f"{f:12s} precision {s['precision']:.2f}  recall {s['recall']:.2f}  accuracy {s['accuracy']:.2f}  n={s['n']}")
    print("\nmisses (id: field gold -> predicted):")
    for i, l in sorted(labels.items()):
        for f in FIELDS:
            if norm(outputs.get(i, {}).get(f)) != norm(l[f]):
                print(f"  {i}: {f} {norm(l[f])} -> {norm(outputs.get(i, {}).get(f)) or '(empty)'}")


if __name__ == "__main__":
    main()
