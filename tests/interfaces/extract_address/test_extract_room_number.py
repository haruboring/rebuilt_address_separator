from unittest import TestCase

from interfaces.extract_address import ExtractAddress


class TestExtractRoomNumber(TestCase):
    def test_extract_room_number1(self) -> None:
        room_number = ExtractAddress.extract_room_number("321/gou室")
        self.assertEqual(room_number, "321号室")
