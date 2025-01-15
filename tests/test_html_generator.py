import unittest
from pathlib import Path
from animals_collateral_adjectives_collector import render_animal_table
from animals_collateral_adjectives_collector.models import Animal

class TestHtmlGenerator(unittest.TestCase):
    def test_render_animal_table_real_template(self):
        # Mock data to render
        mock_data = {
            "canine": [Animal(name="Dog", data_url="/wiki/Dog", image_local_path="tmp/Dog.jpg")],
            "feline": [Animal(name="Cat", data_url="/wiki/Cat", image_local_path="tmp/Cat.jpg")],
        }

        tmp_dir = Path("test-tmp")
        tmp_dir.mkdir(exist_ok=True) # Create the tmp directory if it doesn't exist

        output_file = tmp_dir / "test_output.html"

        # Check that the template file exists
        template_dir = Path(__file__).parent.parent / "animals_collateral_adjectives_collector/templates"
        template_file = template_dir / "results-template.html"
        self.assertTrue(template_file.exists(), "Template file does not exist.")

        # Render the data into an HTML table and save it to a file.
        render_animal_table(mock_data, str(output_file))

        # Assert that the output file was created
        self.assertTrue(output_file.exists(), "Output HTML file was not created.")

        # Get the content of the output file
        rendered_content = output_file.read_text(encoding="utf-8")

        # Assert that the rendered content contains the expected data
        self.assertIn("canine", rendered_content)
        self.assertIn("Dog", rendered_content)
        self.assertIn("feline", rendered_content)
        self.assertIn("Cat", rendered_content)

        # Clean up the test output file
        output_file.unlink()
        tmp_dir.rmdir()
