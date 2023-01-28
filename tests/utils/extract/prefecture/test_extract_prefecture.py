from unittest import TestCase

from src.utils.extract.prefecture.extract_prefecture import extract_prefecture


class TestFillSpace(TestCase):
    def test_extract_prefecture(self) -> None:
        prefecture, extra_address = extract_prefecture("東京都大田区")
        self.assertEqual(prefecture, "東京都")
        self.assertEqual(extra_address, "大田区")
