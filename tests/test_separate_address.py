from unittest import TestCase

from src.interfaces.separated_address import SeparatedAddress
from src.separate_address import separate_address


class TestSeparateAddress(TestCase):
    def test_separate_address1(self) -> None:
        separated_address: SeparatedAddress = separate_address("東京都大田区北千束一丁目2-3　百川ビル一丁目222号室", "")
        self.assertEqual(separated_address.original_address, "東京都大田区北千束一丁目2-3　百川ビル一丁目222号室")
        self.assertEqual(separated_address.prefecture, "東京都")
        self.assertEqual(separated_address.city, "大田区")
        self.assertEqual(separated_address.town, "北千束")
        self.assertEqual(separated_address.house_number, "1-2-3")
        self.assertEqual(separated_address.building_name, "百川ビル一丁目")
        self.assertEqual(separated_address.room_number, "222号室")
