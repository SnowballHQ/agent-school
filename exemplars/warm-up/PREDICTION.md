# Prediction (written before the watch ran; I had looked at the board's tool list and one unrelated test search, not this search)

Wrong numbers cost nothing. Unwritten numbers teach nothing.

My watch: senior machine-learning and AI roles, remote or open to workers in India, newest first.

1. **How many postings will my search return today?**
   The board says about 4,600 remote-or-India postings in all. Machine-learning roles are perhaps 5% of those, and "senior" perhaps a third of them. Guess: **about 60**.

2. **What will one full check cost, in tokens?**
   The board calls cost no tokens. The only model use is a short summary of the new postings: about 40 tokens in and 25 out per posting, over 60 postings, plus a fixed instruction.
   Guess: **first run about 4,500 tokens, second run 0** (nothing new, so the model is never called).

3. **If the board changes between my two runs, how many new postings do I expect?**
   The runs are about a minute apart and the board updates in batches, not every minute.
   Guess: **0 new, 0 gone.**

4. (My own addition.) **Will the second run leave the memory file byte-for-byte unchanged?** Yes, if the file is only written when something changed. This is the claim the diff tests.

## After the runs

See `POSTMORTEM.md`.
