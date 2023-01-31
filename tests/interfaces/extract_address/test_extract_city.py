from unittest import TestCase

from interfaces.extract_address import ExtractAddress


class TestExtractCity(TestCase):
    def test_extract_city1(self) -> None:
        city_and_rest_address = ExtractAddress.extract_city("大田区北千束○-○-○")
        self.assertEqual(city_and_rest_address, ("大田区", "北千束○-○-○"))

    def test_extract_city2(self) -> None:
        city_and_rest_address = ExtractAddress.extract_city("廿日市市下平良○-○-○")
        self.assertEqual(city_and_rest_address, ("廿日市市", "下平良○-○-○"))

    def test_extract_city3(self) -> None:
        city_and_rest_address = ExtractAddress.extract_city("伊予市双海町○-○-○")
        self.assertEqual(city_and_rest_address, ("伊予市", "双海町○-○-○"))

    def test_extract_city4(self) -> None:
        city_and_rest_address = ExtractAddress.extract_city("野々市市三納1丁目1番地")
        self.assertEqual(city_and_rest_address, ("野々市市", "三納1丁目1番地"))

    def test_extract_city5(self) -> None:
        city_and_rest_address = ExtractAddress.extract_city("松山市市坪西町")
        self.assertEqual(city_and_rest_address, ("松山市", "市坪西町"))

    def test_extract_city6(self) -> None:
        city_and_rest_address = ExtractAddress.extract_city("町○○市××")
        self.assertEqual(city_and_rest_address, ("町○○市", "××"))

    def test_extract_city7(self) -> None:
        city_and_rest_address = ExtractAddress.extract_city("三区町××")
        self.assertEqual(city_and_rest_address, ("三区町", "××"))

    def test_extract_city8(self) -> None:
        city_and_rest_address = ExtractAddress.extract_city("千代田区××")
        self.assertEqual(city_and_rest_address, ("千代田区", "××"))
