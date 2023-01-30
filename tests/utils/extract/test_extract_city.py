from unittest import TestCase

from utils.extract.extract_city import extract_city


class TestExtractCity(TestCase):
    def test_extract_city1(self) -> None:
        city_and_rest_address = extract_city("大田区北千束○-○-○")
        self.assertEqual(city_and_rest_address, ("大田区", "北千束○-○-○"))

    def test_extract_city2(self) -> None:
        city_and_rest_address = extract_city("廿日市市下平良○-○-○")
        self.assertEqual(city_and_rest_address, ("廿日市市", "下平良○-○-○"))

    def test_extract_city3(self) -> None:
        city_and_rest_address = extract_city("伊予市双海町○-○-○")
        self.assertEqual(city_and_rest_address, ("伊予市", "双海町○-○-○"))
