from . import collect_collateral_adjectives, fetch_animal_images, render_animal_table, configure_logging

HTML_OUTPUT_PATH = "tmp/animal_table.html"

def main():
    """
    Main function to:
    - Collect collateral adjectives and their associated animals.
    - Fetch and save images for each animal.
    - Renders the data into an HTML table using a Jinja2 template and saves it to a file
    """
    configure_logging() # Configure logging
    collapsed_adj_map = collect_collateral_adjectives()
    fetch_animal_images(collapsed_adj_map)
    render_animal_table(collapsed_adj_map, HTML_OUTPUT_PATH)


if __name__ == "__main__":
    main()