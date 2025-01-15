import unittest
from bs4 import BeautifulSoup
from animals_collateral_adjectives_collector.data_collector import (
    parse_collateral_adjective,
    parse_animal,
    get_column_indices,
    populate_collateral_map,
)

class TestDataCollector(unittest.TestCase):
    def test_parse_collateral_adjective(self):
        html = "<td>asteroid<br>galaxy<sup>[111]</sup></td>"
        soup = BeautifulSoup(html, "html.parser")
        cell = soup.find("td")

        result = parse_collateral_adjective(cell)
        self.assertEqual(result, ["asteroid", "galaxy"])

    def test_parse_animal(self):
        html = '<td><a href="/wiki/Dog" title="Dog">Dog</a></td>'
        soup = BeautifulSoup(html, "html.parser")
        cell = soup.find("td")
        animal = parse_animal([cell], 0)

        self.assertEqual(animal.name, "Dog")
        self.assertEqual(animal.data_url, "/wiki/Dog")

    def test_get_column_indices(self):
        html = """
        <tr>
            <th>Animal</th>
            <th>Extra column</th>
            <th>Collateral adjective</th>
        </tr>
        """
        soup = BeautifulSoup(html, "html.parser")
        headers = soup.find_all("th")
        animal_idx, adj_idx = get_column_indices(headers)

        self.assertEqual(animal_idx, 0)
        self.assertEqual(adj_idx, 2)

    def test_populate_collateral_map(self):
        # Test with two animals, one of the animals has two adjectives
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
        self.assertIn("canine", result)
        self.assertEqual(result["canine"][0].name, "Dog")
        self.assertEqual(result["feline"][0].name, "Cat")
        self.assertEqual(result["feline2"][0].name, "Cat")
