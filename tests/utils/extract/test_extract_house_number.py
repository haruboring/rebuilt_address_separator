from unittest import TestCase

from utils.extract.extract_house_number import extract_house_number


class TestExtractHouseNumber(TestCase):
    def test_extract_house_number1(self) -> None:
        house_number = extract_house_number("1/tyoume二-3山田ハウス")
        self.assertEqual(house_number, "1-2-3")
