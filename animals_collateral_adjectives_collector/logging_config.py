import logging
from pathlib import Path

def configure_logging():
    """Set up the logging configuration for the application."""
    log_file = Path("logs/app.log")
    log_file.parent.mkdir(exist_ok=True)

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        handlers=[
            logging.FileHandler(log_file, encoding="utf-8"), # file logging
            logging.StreamHandler() # console logging
        ]
    )
