from unittest import TestCase

from utils.extract.extract_building_name import extract_building_name


class TestExtractBuildingName(TestCase):
    def test_extract_building_name1(self) -> None:
        building_name = extract_building_name("山田ハウス321/gou室")
        self.assertEqual(building_name, "山田ハウス")

    def test_extract_building_name2(self) -> None:
        building_name = extract_building_name("山田ハウス")
        self.assertEqual(building_name, "山田ハウス")
