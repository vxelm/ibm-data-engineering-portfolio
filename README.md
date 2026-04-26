# IBM Data Engineering Portfolio

A collection of exercises and projects built throughout the **IBM Data Engineering Professional Certificate** (Coursera). Each folder is a self-contained module covering a specific skill area.

## Projects

### 1. [`demographics_etl_pipeline/`](./demographics_etl_pipeline)

> **Course:** Python Project for Data Engineering

A complete ETL pipeline that consolidates person records from multiple file formats (CSV, JSON, XML), converts measurement units, and writes the result to a structured CSV file.

**Key concepts:** multi-format extraction, unit transformation, timestamped logging, modular project structure.

**Stack:** Python · pandas · xml.etree · glob

---

### 2. [`web_scraping_and_etl_pipeline/`](./web_scraping_and_etl_pipeline)

> **Course:** Python Project for Data Engineering

Two standalone scripts:

- **ETL pipeline** — same extraction/transform/load pattern as the demographics project, applied to person data across CSV, JSON, and XML sources.
- **Web scraper** — pulls the *100 Most Highly-Ranked Films* list from a Web Archive snapshot, keeps the top 50, and persists the data to both CSV and a SQLite database.

**Key concepts:** web scraping with BeautifulSoup, SQLite persistence, multi-source ETL, execution logging.

**Stack:** Python · pandas · requests · BeautifulSoup · sqlite3

---

### 3. [`programming_concepts/Concurrency/`](./programming_concepts/Concurrency)

> **Course:** Python for Data Science, AI & Development

Jupyter notebooks exploring Python concurrency with `ThreadPoolExecutor`:

| Notebook | Topic |
|---|---|
| `1. Basic Example.ipynb` | How `as_completed()` enables tasks to report results as they finish vs. waiting in submission order |
| `2. Errors Handling.ipynb` | Handling per-task exceptions (DNS errors, timeouts) without blocking the remaining futures |

**Key concepts:** `ThreadPoolExecutor`, `as_completed`, non-blocking error handling, I/O-bound concurrency.

**Stack:** Python · concurrent.futures · requests

---

## Repository structure

```
ibm-data-engineering-portfolio/
├── demographics_etl_pipeline/
│   ├── src/                  # ETL logic and path settings
│   ├── data/
│   │   ├── raw/              # Input files (CSV, JSON, XML)
│   │   └── processed/        # Output: transformed_data.csv
│   └── logs/                 # Execution log
├── web_scraping_and_etl_pipeline/
│   ├── scripts/              # ETL pipeline and web scraper
│   ├── data/                 # Source files and pipeline output
│   ├── databases/            # SQLite database
│   └── logs/                 # Execution log
└── programming_concepts/
    └── Concurrency/          # Jupyter notebooks
```

## Certificate

[IBM Data Engineering Professional Certificate](https://www.coursera.org/professional-certificates/ibm-data-engineer) — Coursera
