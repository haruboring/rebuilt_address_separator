from unittest import TestCase

from interfaces.extract_address import ExtractAddress


class TestExtractRoomNumber(TestCase):
    def test_extract_room_number1(self) -> None:
        room_number = ExtractAddress.extract_room_number("321/gou室")
        self.assertEqual(room_number, "321号室")

    def test_extract_room_number2(self) -> None:
        room_number = ExtractAddress.extract_room_number("321")
        self.assertEqual(room_number, "321")

    def test_extract_room_number3(self) -> None:
        room_number = ExtractAddress.extract_room_number("")
        self.assertEqual(room_number, "")
