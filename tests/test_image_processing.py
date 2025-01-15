import unittest
from unittest.mock import patch, MagicMock
from animals_collateral_adjectives_collector.image_processing import process_images


class TestImageProcessing(unittest.TestCase):
    @patch("animals_collateral_adjectives_collector.image_processing.requests.get")
    def test_process_images_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.iter_content = MagicMock(return_value=[b"fake_image_data"])
        mock_get.return_value = mock_response

        image_url = "https://example.com/image.jpg"
        animal_name = "Test Animal"
        result = process_images(image_url, animal_name)

        expected_filename = "Test_Animal.jpg"
        self.assertEqual(result, expected_filename, "The filename should match the expected format.")

    @patch("animals_collateral_adjectives_collector.image_processing.requests.get")
    def test_process_images_failure(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        image_url = "https://example.com/image.jpg"
        animal_name = "Test Animal"
        result = process_images(image_url, animal_name)

        self.assertIsNone(result, "The function should return None for a failed download.")