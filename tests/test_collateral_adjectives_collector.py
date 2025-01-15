import unittest
from bs4 import BeautifulSoup
from animals_collateral_adjectives_collector.collateral_adjectives_collector import collect_collateral_adjectives, populate_collateral_map


class TestCollector(unittest.TestCase):
    def test_populate_collateral_map(self):
        html = """
        <tr>
            <td><a href="/wiki/Dog" title="Dog">Dog</a></td>
            <td>canine</td>
        </tr>
        <tr>
            <td><a href="/wiki/Cat" title="Cat">Cat</a></td>
            <td>feline<br>feline2</td>
        </tr>
        """
        soup = BeautifulSoup(html, "html.parser")
        rows = soup.find_all("tr")

        result = populate_collateral_map(rows, 0, 1)
        self.assertEqual(len(result), 3)
        self.assertIn("canine", result)
        self.assertEqual(result["canine"][0].name, "Dog")
        self.assertEqual(result["feline"][0].name, "Cat")
        self.assertEqual(result["feline2"][0].name, "Cat")
