from pathlib import Path

WIKIPEDIA_BASE_URL = "https://en.wikipedia.org"
WIKIPEDIA_ANIMAL_NAMES_URL = "https://en.wikipedia.org/wiki/List_of_animal_names"
TABLE_ATTRIBUTES = {"class": "wikitable sortable sticky-header"}
REQUIRED_TABLE_COLUMNS = ["Animal", "Collateral adjective"]

PROJECT_ROOT = Path(__file__).resolve().parents[1]
TMP_DIR = PROJECT_ROOT / "tmp"

# User-Agent header to mimic a web browser
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

TEMPLATE_NAME = "results-template.html"
