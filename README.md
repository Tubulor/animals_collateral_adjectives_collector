# 🐾 Animals Collateral Adjectives Collector

**Animals Collateral Adjectives Collector** is a tool that extracts **collateral adjectives** and their associated animals from the [Wikipedia List of Animal Names](https://en.wikipedia.org/wiki/List_of_animal_names). It fetches images for each animal, organizes the data into a structured format, and generates an HTML table to display the results beautifully.

---

## ✨ Features

- **Scraping:** Collects collateral adjectives and their associated animals from Wikipedia.
- **Image Fetching:** Downloads images for each animal directly from Wikipedia.
- **HTML File Generation:**

  Creates an HTML file containing:
  - Collateral adjectives.
  - Corresponding animals.
  - Animal images.
- **Local Image Storage:** Saves all downloaded images in the `tmp/` directory for easy access.

---

## 🛠️ Prerequisites

Make sure you have the following installed on your system:

- **Python** (version 3.12 or higher)
- **Poetry** (for dependency and environment management)

---

## 🚀 Installation

Follow these steps to set up the project:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-repo-name/animals-collateral-adjectives-collector.git
   cd animals-collateral-adjectives-collector
   
2. **Install dependencies with Poetry:**

    ```bash
    poetry install

---

## 📖 Usage

To run the application and generate the HTML file:

1. Execute the following command:

   ```bash
   poetry run animals_collateral_adjectives_collector

2. The script will:
   - Scrape the collateral adjectives and associated animals.
   - Fetch images from Wikipedia.
   - Generate an HTML file displaying the results.

3. Check the project directory for:
   - The generated HTML file in the `tmp/` directory.
   - Images saved in the `tmp/` directory.


---

## 🧪 Running Tests

1. To ensure everything is working correctly, run the test suite

   ```bash
   poetry run pytest

---

## 📂 Logging

Logs for the application are stored in the `logs/` directory:

- **File:** `logs/application.log`

This file contains detailed information about:
- Scraping operations.
- Image downloads.
- HTML rendering process.

---

## 🐳 Docker Instructions

You can containerize and run **Animals Collateral Adjectives Collector** using Docker. Follow these steps to build and run the application in a Docker container.

---

### 🔨 Build the Docker Image

1. Make sure Docker is installed and running on your machine.
2. Navigate to the project directory.
3. Build the Docker image using the following command:

   ```bash
   docker build -t animals-coll-adj-collector .

### 🚀 Run the Docker Container

- Once the image is built, you can run the application inside a container:

  ```bash
  docker run -it animals-coll-adj-collector
  
### 📂 Outputs in Docker

- **Generated HTML File**: The generated HTML file will be available inside the container. To copy it to your local machine, you can use the following command:

   ```bash
   docker cp <container_id>:/app/output.html ./output.html
  
 - Replace <container_id> with the ID of the running container, which you can find using:
   
   ```bash
   docker ps

---

## 🖼️ Output

- **HTML File:** Displays a well-structured table of collateral adjectives, associated animals, and their images.
- **Images:** All fetched animal images are saved locally in the `tmp/` directory.

---

## 📋 Example

Below is an example of what the generated HTML table might look like:

| Collateral Adjective | Animal   | Image                  |
|-----------------------|----------|------------------------|
| Lupine               | Wolf     | <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/68/Eurasian_wolf_2.jpg/440px-Eurasian_wolf_2.jpg" alt="Wolf Image" width="100"/> |
| Galline              | Chicken  | <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/84/Male_and_female_chicken_sitting_together.jpg/440px-Male_and_female_chicken_sitting_together.jpg" alt="Chicken Image" width="100"/> |
| Gastropodian         | Snail    | <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/cc/Snail.jpg/440px-Snail.jpg" alt="Snail Image" width="100"/> |

---

## 📬 Contact

If you encounter any issues or have suggestions, feel free to reach out or open an issue on the repository.
