from unittest import TestCase

from utils.extract.extract_town import extract_town


class TestExtractTown(TestCase):
    def test_extract_town1(self) -> None:
        town_and_rest_address = extract_town("北千束1-1-1〇〇ビルディング321")
        self.assertEqual(town_and_rest_address, ("北千束", "1-1-1〇〇ビルディング321"))

    def test_extract_town2(self) -> None:
        town_and_rest_address = extract_town("一/ban町1")
        self.assertEqual(town_and_rest_address, ("一番町", "1"))
