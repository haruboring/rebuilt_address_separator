from unittest import TestCase

from interfaces.extract_address import ExtractAddress


class TestExtractBuildingName(TestCase):
    def test_extract_building_name1(self) -> None:
        building_name_and_rest_address = ExtractAddress.extract_building_name("山田ハウス321/gou室")
        self.assertEqual(building_name_and_rest_address, ("山田ハウス", "321/gou室"))

    def test_extract_building_name2(self) -> None:
        building_name_and_rest_address = ExtractAddress.extract_building_name("山田ハウス")
        self.assertEqual(building_name_and_rest_address, ("山田ハウス", ""))
