from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
LOGGING_DIR = DATA_DIR / "logs"

DATA_DIR.mkdir(parents=True, exist_ok=True)
LOGGING_DIR.mkdir(parents=True, exist_ok=True)
