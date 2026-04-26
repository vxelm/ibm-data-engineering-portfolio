# ETL Project

A Python ETL (Extract, Transform, Load) pipeline that consolidates data from multiple file formats, applies unit-conversion transformations, and persists the results. The project also includes a web scraping module that pulls film rankings from a public archive and stores them in SQLite.

## Project Structure

```
etl_proyect/
├── data/
│   ├── csv/              # Source CSV files + web scraping output
│   ├── json/             # Source JSON files
│   ├── xml/              # Source XML files
│   └── transformed_data.csv  # ETL pipeline output
├── databases/
│   └── Movies.db         # SQLite database (web scraping output)
├── logs/
│   └── log_file.txt      # ETL execution log
└── scripts/
    ├── etl_code.py       # Main ETL pipeline
    └── web_scraping.py   # Film rankings scraper
```

## Scripts

### `etl_code.py` — ETL Pipeline

Reads person data (name, height, weight) from all CSV, JSON, and XML files in the `data/` directory, transforms the units, and saves the result to `data/transformed_data.csv`.

**Phases:**

| Phase | Description |
|-------|-------------|
| Extract | Reads all `.csv`, `.json`, and `.xml` files under `data/` |
| Transform | Converts height from **inches → meters** and weight from **pounds → kilograms** |
| Load | Writes the transformed DataFrame to `data/transformed_data.csv` |

Each phase is timestamped in `logs/log_file.txt`.

**Source data schema:**

```
name (string), height (inches), weight (pounds)
```

**Output schema:**

```
name (string), height (meters, 2 decimal places), weight (kg, 2 decimal places)
```

### `web_scraping.py` — Film Rankings Scraper

Scrapes the *100 Most Highly-Ranked Films* list from a Web Archive snapshot and stores the top 50 entries.

**Output:**
- `data/csv/top_50_films.csv`
- `databases/Movies.db` → table `Top_50`

**Output schema:**

```
Average Rank (string), Film (string), Year (string)
```

## Requirements

```
pandas
requests
beautifulsoup4
```

Install dependencies:

```bash
pip install pandas requests beautifulsoup4
```

## Usage

Run the ETL pipeline from the `scripts/` directory:

```bash
cd scripts
python etl_code.py
```

Run the web scraper:

```bash
cd scripts
python web_scraping.py
```

> Both scripts use relative paths, so they must be executed from the `scripts/` directory.

## Logging

The ETL pipeline appends a timestamped entry to `logs/log_file.txt` at the start and end of each phase:

```
2025-Dec-16-17:44:58,ETL Job Started
2025-Dec-16-17:44:58,Extract phase Started
2025-Dec-16-17:44:58,Extract phase Ended
...
2025-Dec-16-17:44:58,ETL Job Ended
```
