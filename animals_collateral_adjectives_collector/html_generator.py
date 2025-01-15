from jinja2 import Environment, FileSystemLoader, TemplateNotFound
from pathlib import Path
from typing import List, Dict
from .models import Animal
import logging

logger = logging.getLogger(__name__)
TEMPLATE_NAME = "results-template.html"

def render_animal_table(data: Dict[str, List[Animal]], output_file: str):
    """
    Renders the collateral adjectives and animals into an HTML table using Jinja2.
    Args:
        data: Dictionary where keys are collateral adjectives and values are lists of Animal objects.
        output_file: Path to save the rendered HTML file.
    """
    if not data or not isinstance(data, Dict):
        logger.error("Invalid or empty data provided for rendering.")
        raise ValueError("Data must be a non-empty dictionary.")

    try:
        logger.info("Loading Jinja2 template.")
        template_dir = Path(__file__).parent / "templates"
        env = Environment(loader=FileSystemLoader(template_dir))
        template = env.get_template(TEMPLATE_NAME)

        logger.info("Rendering HTML.")
        rendered_html = template.render(data=data)

        logger.info(f"Saving rendered HTML to file: {output_file}.")
        output_path = Path(output_file)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(rendered_html, encoding="utf-8")

    except TemplateNotFound:
        logger.error(f"Template {TEMPLATE_NAME} not found in {template_dir}.")
        raise
    except Exception as e:
        logger.error(f"An error occurred during rendering or saving: {e}")
        raise