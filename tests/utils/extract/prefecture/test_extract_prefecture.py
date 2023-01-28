from unittest import TestCase

from src.utils.extract.prefecture.extract_prefecture import extract_prefecture


class TestFillSpace(TestCase):
    def test_extract_prefecture1(self) -> None:
        prefecture, extra_address = extract_prefecture("東京都大田区")
        self.assertEqual(prefecture, "東京都")
        self.assertEqual(extra_address, "大田区")

    def test_extract_prefecture2(self) -> None:
        prefecture, extra_address = extract_prefecture("愛媛県松山市〇〇町東京都民会館愛媛県支部")
        self.assertEqual(prefecture, "愛媛県")
        self.assertEqual(extra_address, "松山市〇〇町東京都民会館愛媛県支部")
