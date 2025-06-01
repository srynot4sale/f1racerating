# F1 Race Ratings

Python script to display recent race ratings, to see if it's worth watching the full race or just the highlights.

Big thanks to https://www.racefans.net for collecting this info.

Generated with Claude Code.

## Example output

```
F1 Race Rating Extractor
========================================
Downloading index page: https://www.racefans.net/category/regular-features/rate-the-race/
Found 20 race rating posts
Processing latest 3 races:
  - https://www.racefans.net/2025/05/25/rate-the-race-2025-monaco-grand-prix/
  - https://www.racefans.net/2025/05/18/rate-the-race-2025-emilia-romagna-grand-prix/
  - https://www.racefans.net/2025/05/04/rate-the-race-2025-miami-grand-prix/

Downloading individual race pages...

Processing: https://www.racefans.net/2025/05/25/rate-the-race-2025-monaco-grand-prix/
  Race: 2025 Monaco Grand Prix
  Rating: 3.87
  Median: 3.0
  Votes: 198

Processing: https://www.racefans.net/2025/05/18/rate-the-race-2025-emilia-romagna-grand-prix/
  Race: 2025 Emilia Romagna Grand Prix
  Rating: 6.98
  Median: 7.0
  Votes: 170

Processing: https://www.racefans.net/2025/05/04/rate-the-race-2025-miami-grand-prix/
  Race: 2025 Miami Grand Prix
  Rating: 6.98
  Median: 7.0
  Votes: 170
```

## How to use

Make sure you have `uv` installed, and it'll handle all the setup for you.

```
uv run main.py
```
