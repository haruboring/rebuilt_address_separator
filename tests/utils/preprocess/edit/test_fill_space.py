from unittest import TestCase

from src.utils.preprocess.edit.fill_space import fill_space


class TestFillSpace(TestCase):
    def test_fill_space(self) -> None:
        return_value = fill_space("あ い　う  え　　お")
        self.assertEqual(return_value, "あいうえお")
