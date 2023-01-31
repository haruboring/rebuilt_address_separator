from unittest import TestCase

from interfaces.edit_original_address import EditOriginalAddress


class TestFillSpace(TestCase):
    def test_fill_space(self) -> None:
        return_value = EditOriginalAddress.fill_space("あ い　う  え　　お")
        self.assertEqual(return_value, "あいうえお")
