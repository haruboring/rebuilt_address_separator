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

    def test_separate_address2(self) -> None:
        separated_address: SeparatedAddress = separate_address("愛媛県松番市一番町3丁目3ー6", "")
        self.assertEqual(separated_address.original_address, "愛媛県松番市一番町3丁目3ー6")
        self.assertEqual(separated_address.prefecture, "愛媛県")
        self.assertEqual(separated_address.city, "松番市")
        self.assertEqual(separated_address.town, "一番町")
        self.assertEqual(separated_address.house_number, "3-3-6")
        self.assertEqual(separated_address.building_name, "")
        self.assertEqual(separated_address.room_number, "")

    def test_separate_address3(self) -> None:
        separated_address: SeparatedAddress = separate_address("東京都港区南青山7-1-7. C-Cube南青山ビル 6F", "")
        self.assertEqual(separated_address.original_address, "東京都港区南青山7-1-7. C-Cube南青山ビル 6F")
        self.assertEqual(separated_address.prefecture, "東京都")
        self.assertEqual(separated_address.city, "港区")
        self.assertEqual(separated_address.town, "南青山")
        self.assertEqual(separated_address.house_number, "7-1-7")
        self.assertEqual(separated_address.building_name, ".C-Cube南青山ビル")
        self.assertEqual(separated_address.room_number, "6F")

    def test_separate_address4(self) -> None:
        separated_address: SeparatedAddress = separate_address("東京都大田区西六郷4-30-7音金六郷マンション1-C号", "")
        self.assertEqual(separated_address.original_address, "東京都大田区西六郷4-30-7音金六郷マンション1-C号")
        self.assertEqual(separated_address.prefecture, "東京都")
        self.assertEqual(separated_address.city, "大田区")
        self.assertEqual(separated_address.town, "西六郷")
        self.assertEqual(separated_address.house_number, "4-30-7")
        self.assertEqual(separated_address.building_name, "音金六郷マンション")
        self.assertEqual(separated_address.room_number, "1-C号")
