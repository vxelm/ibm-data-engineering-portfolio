# ETL Pipeline — Python Data Engineering Project

Final project for the **Python Project for Data Engineering Certificate** (Coursera). Implements a complete ETL (Extract, Transform, Load) pipeline in Python that consolidates person data from multiple file formats, applies unit conversions, and persists the results to CSV.

## What it does

1. **Extract** — reads all CSV, JSON, and XML files from `data/raw/`
2. **Transform** — converts height from inches to meters and weight from pounds to kilograms
3. **Load** — writes the cleaned dataset to `data/processed/transformed_data.csv`
4. **Log** — appends a timestamped entry for each phase to `logs/log_file.txt`

## Project structure

```
project/
├── src/
│   ├── etl.py          # ETL logic (extract, transform, load, log)
│   └── settings.py     # Path configuration
├── data/
│   ├── raw/            # Input files (CSV, JSON, XML)
│   └── processed/      # Output: transformed_data.csv
└── logs/
    └── log_file.txt    # Execution log
```

## Input data schema

Each source file contains person records with three fields:

| Field  | Unit (raw)  | Unit (output) |
|--------|-------------|---------------|
| name   | —           | —             |
| height | inches      | meters        |
| weight | pounds      | kilograms     |

## Requirements

- Python 3.10+
- pandas
- Standard library: `glob`, `xml.etree.ElementTree`, `datetime`

Install dependencies:

```bash
pip install pandas
```

## Usage

Run from the `src/` directory:

```bash
cd src
python etl.py
```

The script will print the transformed DataFrame to stdout and append progress entries to the log file.

## Conversions applied

- Height: `inches × 0.0254` → meters (rounded to 2 decimal places)
- Weight: `pounds × 0.45359237` → kilograms (rounded to 2 decimal places)
