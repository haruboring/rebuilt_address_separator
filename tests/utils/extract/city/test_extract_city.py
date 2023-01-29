from unittest import TestCase

from src.utils.extract.city.extract_city import extract_city


class TestExtractCity(TestCase):
    def test_extract_city1(self) -> None:
        city = extract_city("大田区北千束○-○-○")
        self.assertEqual(city, "大田区")

    def test_extract_city2(self) -> None:
        city = extract_city("廿日市市下平良○-○-○")
        self.assertEqual(city, "廿日市市")

    def test_extract_city3(self) -> None:
        city = extract_city("伊予市双海町○-○-○")
        self.assertEqual(city, "伊予市")
