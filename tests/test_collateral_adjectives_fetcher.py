import unittest
from unittest.mock import patch, MagicMock
from animals_collateral_adjectives_collector.collateral_adjectives_fetcher import fetch_animal_table_body


class TestFetcher(unittest.TestCase):
    @patch("requests.get")
    def test_fetch_animal_table_body(self, mock_get):
        # Mock HTML content with a table
        mock_html = """
            <html>
                <body>
                    <table class="wikitable sortable sticky-header">
                        <tbody>
                            <tr><th>Animal</th><th>Collateral adjective</th></tr>
                            <tr><td>Lion</td><td>Lupine</td></tr>
                        </tbody>
                    </table>
                </body>
            </html>
            """

        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.content = mock_html.encode("utf-8")
        mock_get.return_value = mock_response

        tbody = fetch_animal_table_body()

        self.assertIsNotNone(tbody, "Table body should not be None")
        self.assertEqual(len(tbody.find_all("tr")), 2, "Table body should contain two rows (header + one data row)")
        self.assertIn("Lion", tbody.text, "The table body should contain the animal 'Lion'")
        self.assertIn("Lupine", tbody.text, "The table body should contain the adjective 'Lupine'")

