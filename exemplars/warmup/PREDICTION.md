# Prediction (written before the watch ran; I had looked at the board's tool list and one unrelated test search, not this search)

Wrong numbers cost nothing. Unwritten numbers teach nothing.

## Predictions

My watch: senior machine-learning and AI roles, remote or open to workers in India, newest first.

1. **How many postings will my search return today?**
   The board says about 4,600 remote-or-India postings in all. Machine-learning roles are perhaps 5% of those, and "senior" perhaps a third of them. Guess: **about 60**.

2. **What will one full check cost, in tokens?**
   The board calls cost no tokens. The only model use is a short summary of the new postings: about 40 tokens in and 25 out per posting, over 60 postings, plus a fixed instruction.
   Guess: **first run about 4,500 tokens, second run 0** (nothing new, so the model is never called).

3. **If the board changes between my two runs, how many new postings do I expect?**
   The runs are about a minute apart and the board updates in batches, not every minute.
   Guess: **0 new, 0 gone.**

- My own addition, not numbered: **Will the second run leave the memory file byte-for-byte unchanged?** Yes, if the file is only written when something changed. This is the claim the diff tests.

## The gap
1. Postings: I said about 60, the board returned 100 (two pages of 50). I guessed the pool, not the thing the pool feeds.
2. Tokens: I said about 4,500 for the first check and 0 for the second. The first cost 2,048 (938 in, 1,110 out) in the final run, 2,938 in the first attempt (`usage.jsonl`); the second cost 0, and the model was never called.
3. Change between runs: I said 0 new, 0 gone, and that is what the runs about 15 seconds apart showed, which only proves "no change" is reported as no change. The contract's staged-change step does better: with one key deleted from a copy of the memory file the watcher reports exactly one `new:` line. The unnumbered claim, a byte-identical memory file after run 2, held: `diff-live-run.txt` is empty and the hashes match.

Full table and lessons: `POSTMORTEM.md`.
