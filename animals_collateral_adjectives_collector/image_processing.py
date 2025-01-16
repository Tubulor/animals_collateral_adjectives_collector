import requests, logging
from .constants import TMP_DIR, HEADERS

logger = logging.getLogger(__name__)


def process_images(image_url, animal_name):
    """
    Downloads and saves the image locally as a .jpg file.
    Returns the local image path or None if the image could not be saved.
    """
    logger.info(f"Saving image for {animal_name}")
    try:
        filename = f"{animal_name.replace(' ', '_')}.jpg"
        file_path = TMP_DIR / filename # Create the full path to the file
        response = requests.get(image_url, stream=True, headers=HEADERS)
        if response.status_code == 200:
            with open(file_path, "wb") as file:
                for chunk in response.iter_content(1024):
                    file.write(chunk)
            return str(filename)
        else:
            logger.error(f"Failed to download image: {image_url} (Status: {response.status_code})")
    except Exception as e:
        logger.error(f"Error saving image {animal_name}: {e}")
    return None
