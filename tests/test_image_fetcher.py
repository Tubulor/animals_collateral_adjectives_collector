import unittest
from unittest.mock import patch, MagicMock
from animals_collateral_adjectives_collector.image_fetcher import fetch_og_image


class TestImageFetcher(unittest.TestCase):
    @patch("requests.get")
    def test_fetch_og_image_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.content = b'<html><meta content="https://upload.wikimedia.org/image.jpg" property="og:image"/></html>'
        mock_get.return_value = mock_response

        url = "https://upload.wikimedia.org"
        result = fetch_og_image(url)

        self.assertEqual(result, "https://upload.wikimedia.org/image.jpg")

    @patch("requests.get")
    def test_fetch_og_image_no_meta_tag(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.content = b"<html></html>"
        mock_get.return_value = mock_response

        url = "https://upload.wikimedia.org"
        result = fetch_og_image(url)

        self.assertIsNone(result)

    @patch("requests.get")
    def test_fetch_og_image_request_fail(self, mock_get):
        mock_get.side_effect = Exception("Request failed")

        url = "https://upload.wikimedia.org"
        result = fetch_og_image(url)

        self.assertIsNone(result)