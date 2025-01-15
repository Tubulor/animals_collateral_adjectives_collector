import requests
import os
from bs4 import BeautifulSoup
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
import logging

logger = logging.getLogger(__name__)

WIKIPEDIA_BASE_URL = "https://en.wikipedia.org"
PROJECT_ROOT = Path(__file__).resolve().parents[1]
TMP_DIR = PROJECT_ROOT / "tmp"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}


def fetch_animal_images(collapsed_adj_map, max_workers=os.cpu_count() * 2):
    """
    Fetches and saves animal images using threads.
    Return the updated collapsed_adj_map with the local image paths.
    """
    logger.info("Fetching animal images.")
    TMP_DIR.mkdir(parents=True, exist_ok=True) # Create the tmp directory if it doesn't exist
    # Create a list of tasks to process
    tasks = [
        (animal, WIKIPEDIA_BASE_URL + animal.data_url)
        for animals in collapsed_adj_map.values()
        for animal in animals
    ]

    # Process the tasks using threads
    with ThreadPoolExecutor(max_workers) as executor:
        logger.info(f"Processing {len(tasks)} tasks using {max_workers} threads.")
        # Submit the tasks to the executor and map the future objects to the animals for better access later
        future_to_animal = {executor.submit(process_task, task): task[0] for task in tasks}
        # iterate over the future objects and waits until at least one is completed and then process the loop
        # if no future object is completed, it will wait - loop paused (blocks) until one is completed
        for future in as_completed(future_to_animal):
            animal = future_to_animal[future]
            try:
                animal.image_local_path = future.result() # get the result of the corresponding task (future)
            except Exception as e:
                logger.error(f"Error processing task: {e}")

    return collapsed_adj_map


def process_task(task):
    """
    Processes a single task: fetches og:image URL and saves the image.
    Returns the local image path or None if the image could not be saved.
    """
    logger.info(f"Processing task: {task}")
    animal, url = task
    image_url = fetch_og_image(url)
    return save_image(image_url, animal.name) if image_url else None


def fetch_og_image(url):
    """
    Fetches the 'og:image' URL from a Wikipedia page.
    Returns the image URL or None if not found.
    """
    logger.info(f"Fetching og:image from {url}")
    try:
        # the headers are used to mimic a browser request to avoid being blocked
        response = requests.get(url, headers=HEADERS)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            meta = soup.find("meta", property="og:image") # Find the first meta tag with the property 'og:image'
            return meta["content"] if meta else None # Extract the content attribute from the meta tag which contains the image url
    except Exception as e:
        logger.error(f"Error fetching og:image from {url}: {e}")
    return None


def save_image(image_url, animal_name):
    """
    Downloads and saves the image locally as a .jpg file.
    Returns the local image path or None if the image could not be saved.
    """
    logger.info(f"Saving image for {animal_name}")
    try:
        filename = f"{animal_name.replace(' ', '_')}.jpg" # Replace spaces with underscores in the filename
        file_path = TMP_DIR / filename # Create the full path to the file
        response = requests.get(image_url, stream=True, headers=HEADERS)
        if response.status_code == 200:
            with open(file_path, "wb") as file:
                for chunk in response.iter_content(1024):
                    file.write(chunk)
            return str(file_path)
        else:
            logger.error(f"Failed to download image: {image_url} (Status: {response.status_code})")
    except Exception as e:
        logger.error(f"Error saving image {animal_name}: {e}")
    return None