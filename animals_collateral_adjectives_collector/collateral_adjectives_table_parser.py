import logging
from .models import Animal
from .constants import REQUIRED_TABLE_COLUMNS

logger = logging.getLogger(__name__)


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
