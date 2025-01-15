import requests
import logging
from bs4 import BeautifulSoup
from typing import List, Dict
from .models import Animal

WIKIPEDIA_ANIMAL_NAMES_URL = "https://en.wikipedia.org/wiki/List_of_animal_names"
TABLE_ATTRIBUTES = {"class": "wikitable sortable sticky-header"}
REQUIRED_TABLE_COLUMNS = ["Animal", "Collateral adjective"]
logger = logging.getLogger(__name__)

def fetch_animal_table_body():
    """
    Fetches the table body with the specific attribute from the Wikipedia animal names page.
    Returns the table body containing the animal data.
    """
    logger.info("Fetching animal table body.")
    response = requests.get(WIKIPEDIA_ANIMAL_NAMES_URL)
    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find("table", TABLE_ATTRIBUTES)
    if not table:
        logger.error("Could not find animal table.")
        raise ValueError("Could not find animal table.")
    return table.find("tbody")


def get_column_indices(headers):
    """
    Maps table header text to column indices.
    Returns the indices of the required columns.
    """
    logger.info("Getting column indices.")
    header_map = {header.text.strip(): idx for idx, header in enumerate(headers)}
    try:
        return [header_map[col] for col in REQUIRED_TABLE_COLUMNS] # Creates a list of indices for the required columns
    except KeyError:
        logger.error(f"Missing required columns in table: {REQUIRED_TABLE_COLUMNS}")
        raise ValueError(f"Missing required columns in table: {REQUIRED_TABLE_COLUMNS}")


def parse_animal(cells, animal_idx):
    """
    Parses animal data from a table row.
    Get the name from title attribute of the first <a> tag in the cell.
    get the data URL from the href attribute of the first <a> tag in the cell.
    Returns an Animal object with the name and data URL.
    """
    logger.info("Parsing animal data.")
    cell = cells[animal_idx]
    link_tag = cell.find("a")  # Find the first <a> tag in the cell
    if link_tag:
        name = link_tag["title"] # Extract the title attribute
        link = link_tag["href"]  # Extract the href link
        logger.info(f"Found animal: {name}")
        return Animal(name=name, data_url=link)
    else:
        raise ValueError(f"Missing <a> tag for animal in cell: {cell}")


def parse_collateral_adjective(cell):
    """
    Parses collateral adjectives from a <td> tag.
    Removes <br> tags, ignores all other nested tags, and extracts only plain text.
    Return a list of adjectives.
    """
    logger.info("Parsing collateral adjectives.")
    # Remove all unwanted tags except <br>
    for unwanted in cell.find_all(recursive=True):  # Finds all nested tags
        if unwanted.name != "br":  # Keep <br> tags, remove everything else
            unwanted.decompose()

    # Replace <br> tags with newline characters
    for br in cell.find_all("br"):
        br.replace_with("\n")

    # Extract plain text from the cleaned cell
    content = cell.get_text()

    # Split the content by newline characters and remove empty strings
    adjectives = [adj.strip() for adj in content.split("\n") if adj.strip()]
    logger.info(f"Found adjectives: {adjectives}")
    return adjectives


def populate_collateral_map(rows, animal_idx, adj_idx):
    """
    Populates the collateral adjective map with animal data.
    Returns a dictionary mapping each adjective to a list of animals.
    """
    logger.info("Populating collateral adjective map.")
    adj_map: Dict[str, List[Animal]] = {}
    for row in rows:
        cells = row.find_all("td") # Find all <td> tags in the row (cells)
        if not cells:
            continue

        # Parse collateral adjectives and animals
        collaterals_adjectives = parse_collateral_adjective(cells[adj_idx])
        animal = parse_animal(cells, animal_idx)

        # Assign the animal to each collateral adjective
        for adj in collaterals_adjectives:
            adj_map.setdefault(adj, []).append(animal)
        logger.info(f"Added animal {animal.name} to adjectives: {collaterals_adjectives}")
    return adj_map


def collect_collateral_adjectives():
    """Main function to collect and display collateral adjectives and animals."""
    logger.info("Collecting collateral adjectives.")
    tbody = fetch_animal_table_body()

    headers = tbody.find_all("th") # Find all <th> tags in the table
    animal_idx, adj_idx = get_column_indices(headers) # Get the indices of the required columns
    rows = tbody.find_all("tr")[1:]  # Skip the first row (header row) and get all <tr> tags (rows)

    adj_map = populate_collateral_map(rows, animal_idx, adj_idx) # Populate the collateral adjective map
    return adj_map
