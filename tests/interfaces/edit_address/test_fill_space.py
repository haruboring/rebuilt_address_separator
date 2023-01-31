from unittest import TestCase

from interfaces.edit_address import EditAddress


class TestFillSpace(TestCase):
    def test_fill_space1(self) -> None:
        return_value = EditAddress.fill_space("あ い　う  え　　お")
        self.assertEqual(return_value, "あいうえお")

    def test_fill_space2(self) -> None:
        return_value = EditAddress.fill_space("   ")
        self.assertEqual(return_value, "")
