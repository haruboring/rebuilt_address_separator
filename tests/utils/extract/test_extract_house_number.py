from unittest import TestCase

from interfaces.extract_address import ExtractAddress


class TestExtractHouseNumber(TestCase):
    def test_extract_house_number1(self) -> None:
        house_number_and_rest_address = ExtractAddress.extract_house_number("1/tyoume二-3山田ハウス")
        self.assertEqual(house_number_and_rest_address, ("1-2-3", "山田ハウス"))

    def test_extract_house_number2(self) -> None:
        house_number_and_rest_address = ExtractAddress.extract_house_number("1-3-1/gou")
        self.assertEqual(house_number_and_rest_address, ("1-3-1", ""))

    def test_extract_house_number3(self) -> None:
        house_number_and_rest_address = ExtractAddress.extract_house_number("1/no3/no2")
        self.assertEqual(house_number_and_rest_address, ("1-3-2", ""))
