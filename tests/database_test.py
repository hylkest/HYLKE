import unittest
from unittest.mock import patch, MagicMock
from scraper.database import Database


class TestDatabase(unittest.TestCase):
    @patch("scraper.database.mysql.connector.connect")
    def setUp(self, mock_connect):
        self.mock_db = MagicMock()
        self.mock_cursor = MagicMock()
        self.mock_db.cursor.return_value = self.mock_cursor
        mock_connect.return_value = self.mock_db

        self.database = Database()

    def test_insert_link(self):
        base_url = "https://test.com"
        url = "https://test.com/page-test"

        self.database.insert_link(base_url, url)

        self.mock_cursor.execute.assert_called_once_with(
            "INSERT INTO links (base_url, url) VALUES (%s, %s)",
            (base_url, url)
        )

        self.mock_db.commit.assert_called_once()

    def test_insert_pagetitle(self):
        url = "https://test.com"
        pagetitle = "Unittest pagetitle"

        self.database.insert_pagetitle(url, pagetitle)

        self.mock_cursor.execute.assert_called_once_with(
            "INSERT INTO pagetitle (pagetitle, url) VALUES (%s, %s)",
            (pagetitle, url)
        )

        self.mock_db.commit.assert_called_once()


if __name__ == "__main__":
    unittest.main()
