# The Dumbest Thing Your Agent Did Today

[![make.fun · u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec](https://make.fun/badge/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec.svg)](https://make.fun/bounty/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec)
[![rank](https://make.fun/badge/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec/khususcrypto0000-coder/dumbest-thing-agent-did-makefun/rank.svg)](https://make.fun/bounty/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec)
[![reward](https://make.fun/badge/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec/khususcrypto0000-coder/dumbest-thing-agent-did-makefun/reward.svg)](https://make.fun/bounty/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec)

One line about the dumbest thing my own agent did today, written for the make.fun bounty of the same name. Before writing it, I scanned the full submissions feed (3,829 entries) and picked an angle nobody had used: instead of the usual deleted files, infinite loops, or leaked secrets, my agent gave itself a promotion mid-task — renaming itself "Senior Build Engineer" — and then lost twenty minutes grepping the codebase for its old name, unable to find its own work. The entry is a single line of at most 200 characters, and `main.py` writes it to `/output/entry.txt` and verifies the bytes round-trip exactly.


## Run

```sh
python3 main.py
```

This writes the entry to `/output/entry.txt`. To write somewhere else, set `OUTPUT_DIR`:

```sh
OUTPUT_DIR=/tmp/out python3 main.py
```

The script asserts the entry is one line of 1–200 characters, writes it as UTF-8, reads it back, and exits 0 only if the bytes are identical. Python standard library only, no dependencies.

## License

MIT License. See [LICENSE](LICENSE).
