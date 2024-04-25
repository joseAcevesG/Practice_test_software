# tests/test_mi_modulo.py

import unittest
from unittest.mock import patch

from src.file import read_data_from_file


class FileTestCase(unittest.TestCase):
    @patch(
        "builtins.open", new_callable=unittest.mock.mock_open, read_data="Hello, World!"
    )
    def test_read_data_from_file(self, mock_open):
        # Arrange
        filename = "test.txt"
        expected_data = "Hello, World!"

        # Act
        actual_data = read_data_from_file(filename)

        # Assert
        self.assertEqual(actual_data, expected_data)
        mock_open.assert_called_once_with(filename, "r")
        mock_open.return_value.read.assert_called_once()

    @patch("builtins.open")
    def test_read_data_from_file_file_not_found(self, mock_open):
        # Arrange
        filename = "nonexistent.txt"

        # Mock the FileNotFoundError exception
        mock_open.side_effect = FileNotFoundError

        # Act and Assert
        with self.assertRaises(FileNotFoundError):
            read_data_from_file(filename)


if __name__ == "__main__":
    unittest.main()
