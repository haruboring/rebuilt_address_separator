from unittest import TestCase

from interfaces.edit_address import EditAddress


class TestFillSpace(TestCase):
    def test_fill_space(self) -> None:
        return_value = EditAddress.fill_space("あ い　う  え　　お")
        self.assertEqual(return_value, "あいうえお")
