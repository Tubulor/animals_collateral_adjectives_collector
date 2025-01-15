# Animals Collateral Adjectives Collector

This project collects **collateral adjectives** and their associated animals from the [Wikipedia List of Animal Names](https://en.wikipedia.org/wiki/List_of_animal_names). It fetches images for each animal, organizes the data into a structured format, and renders an HTML table.

---

## Features

- Scrapes collateral adjectives and associated animals from Wikipedia.
- Fetches animal images from Wikipedia.
- Generates an HTML file featuring a well-organized table that showcases collateral adjectives alongside their associated animals, complete with animal images.
- Saves all downloaded images in the `tmp/` directory for local access.

---

## Prerequisites

Ensure you have the following installed:

- **Python** (3.12+)
- **Poetry** for dependency management

---

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-repo-name/animals-collateral-adjectives-collector.git
   cd animals-collateral-adjectives-collector```

2.	Install dependencies using Poetry:

  ```poetry install```

---

## Usage

To run the application, execute the following command:
```poetry run animals_collateral_adjectives_collector```

---

## Running Tests

To run the test suite, execute:
```poetry run pytest```

---

## Logging

Logs for the application are saved in the logs/ directory:
	•	File: logs/application.log
This file contains detailed information about the scraping, image downloading, and rendering processes.
