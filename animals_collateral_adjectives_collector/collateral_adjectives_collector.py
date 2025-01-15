import logging
from typing import List, Dict
from .collateral_adjectives_fetcher import fetch_animal_table_body
from .collateral_adjectives_table_parser import get_column_indices, parse_animal, parse_collateral_adjective
from .models import Animal

logger = logging.getLogger(__name__)


def collect_collateral_adjectives():
    """Main function to collect and display collateral adjectives and animals."""
    logger.info("Collecting collateral adjectives.")
    tbody = fetch_animal_table_body()

    headers = tbody.find_all("th") # Find all <th> tags in the table
    animal_idx, adj_idx = get_column_indices(headers) # Get the indices of the required columns
    rows = tbody.find_all("tr")[1:]  # Skip the first row (header row) and get all <tr> tags (rows)

    adj_map = populate_collateral_map(rows, animal_idx, adj_idx) # Populate the collateral adjective map
    return adj_map


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
