import requests, logging
from bs4 import BeautifulSoup
from .constants import WIKIPEDIA_ANIMAL_NAMES_URL, TABLE_ATTRIBUTES

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
