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

    def test_separate_address5(self) -> None:
        separated_address: SeparatedAddress = separate_address("玉野市後閑1-13　カイテラス1-102号", "")
        self.assertEqual(separated_address.original_address, "玉野市後閑1-13　カイテラス1-102号")
        self.assertEqual(separated_address.prefecture, "")
        self.assertEqual(separated_address.city, "玉野市")
        self.assertEqual(separated_address.town, "後閑")
        self.assertEqual(separated_address.house_number, "1-13")
        self.assertEqual(separated_address.building_name, "カイテラス")
        self.assertEqual(separated_address.room_number, "1-102号")

    def test_separate_address6(self) -> None:
        separated_address: SeparatedAddress = separate_address("長崎県佐世保市小佐々町黒石356-14　ベイサイドタウン7-6", "")
        self.assertEqual(separated_address.original_address, "長崎県佐世保市小佐々町黒石356-14　ベイサイドタウン7-6")
        self.assertEqual(separated_address.prefecture, "長崎県")
        self.assertEqual(separated_address.city, "佐世保市")
        self.assertEqual(separated_address.town, "小佐々町黒石")
        self.assertEqual(separated_address.house_number, "356-14")
        self.assertEqual(separated_address.building_name, "ベイサイドタウン")
        self.assertEqual(separated_address.room_number, "7-6")

    def test_separate_address7(self) -> None:
        separated_address: SeparatedAddress = separate_address("玉野市長尾1588-26", "")
        self.assertEqual(separated_address.original_address, "玉野市長尾1588-26")
        self.assertEqual(separated_address.prefecture, "")
        self.assertEqual(separated_address.city, "玉野市")
        self.assertEqual(separated_address.town, "長尾")
        self.assertEqual(separated_address.house_number, "1588-26")
        self.assertEqual(separated_address.building_name, "")
        self.assertEqual(separated_address.room_number, "")

    def test_separate_address8(self) -> None:
        separated_address: SeparatedAddress = separate_address("竜南110", "")
        self.assertEqual(separated_address.original_address, "竜南110")
        self.assertEqual(separated_address.prefecture, "")
        self.assertEqual(separated_address.city, "")
        self.assertEqual(separated_address.town, "竜南")
        self.assertEqual(separated_address.house_number, "110")
        self.assertEqual(separated_address.building_name, "")
        self.assertEqual(separated_address.room_number, "")

    def test_separate_address9(self) -> None:
        separated_address: SeparatedAddress = separate_address("島原市萩原２丁目5192-2荻原ＡＰ104", "")
        self.assertEqual(separated_address.original_address, "島原市萩原２丁目5192-2荻原ＡＰ104")
        self.assertEqual(separated_address.prefecture, "")
        self.assertEqual(separated_address.city, "島原市")
        self.assertEqual(separated_address.town, "萩原")
        self.assertEqual(separated_address.house_number, "2-5192-2")
        self.assertEqual(separated_address.building_name, "荻原ＡＰ")
        self.assertEqual(separated_address.room_number, "104")

    def test_separate_address10(self) -> None:
        separated_address: SeparatedAddress = separate_address("長崎県長崎市川口町7-12アーバス川口町407", "")
        self.assertEqual(separated_address.original_address, "長崎県長崎市川口町7-12アーバス川口町407")
        self.assertEqual(separated_address.prefecture, "長崎県")
        self.assertEqual(separated_address.city, "長崎市")
        self.assertEqual(separated_address.town, "川口町")
        self.assertEqual(separated_address.house_number, "7-12")
        self.assertEqual(separated_address.building_name, "アーバス川口町")
        self.assertEqual(separated_address.room_number, "407")
