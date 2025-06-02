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
  - https://www.racefans.net/2025/06/01/rate-the-race-2025-spanish-grand-prix/
  - https://www.racefans.net/2025/05/25/rate-the-race-2025-monaco-grand-prix/
  - https://www.racefans.net/2025/05/18/rate-the-race-2025-emilia-romagna-grand-prix/

Downloading individual race pages...

Processing: https://www.racefans.net/2025/06/01/rate-the-race-2025-spanish-grand-prix/
  Race: 2025 Spanish Grand Prix
  Rating: 7.15
  Median: 7.0
  Votes: 122

Processing: https://www.racefans.net/2025/05/25/rate-the-race-2025-monaco-grand-prix/
  Race: 2025 Monaco Grand Prix
  Rating: 3.85
  Median: 3.0
  Votes: 199

Processing: https://www.racefans.net/2025/05/18/rate-the-race-2025-emilia-romagna-grand-prix/
  Race: 2025 Emilia Romagna Grand Prix
  Rating: 6.98
  Median: 7.0
  Votes: 170
```

## How to use

Make sure you have `uv` installed, and it'll handle all the setup for you.

```
uv run main.py
```
