from unittest import TestCase

from utils.extract.extract_prefecture import extract_prefecture


class TestFillSpace(TestCase):
    def test_extract_prefecture1(self) -> None:
        prefecture_and_rest_address = extract_prefecture("東京都大田区")
        self.assertEqual(prefecture_and_rest_address, ("東京都", "大田区"))

    def test_extract_prefecture2(self) -> None:
        prefecture_and_rest_address = extract_prefecture("愛媛県松山市〇〇町東京都民会館愛媛県支部")
        self.assertEqual(prefecture_and_rest_address, ("愛媛県", "松山市〇〇町東京都民会館愛媛県支部"))
