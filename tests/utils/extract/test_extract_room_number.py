from unittest import TestCase

from utils.extract.extract_room_number import extract_room_number


class TestExtractRoomNumber(TestCase):
    def test_extract_room_number1(self) -> None:
        room_number = extract_room_number("321/gou室")
        self.assertEqual(room_number, "321号室")
