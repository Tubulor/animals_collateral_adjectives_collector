import unittest
from bs4 import BeautifulSoup
from animals_collateral_adjectives_collector.collateral_adjectives_table_parser import parse_collateral_adjective, parse_animal, get_column_indices

class TestTableParser(unittest.TestCase):
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
