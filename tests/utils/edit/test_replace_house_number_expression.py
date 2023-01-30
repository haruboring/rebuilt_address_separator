from unittest import TestCase

from src.utils.edit.replace_house_number_expression import replace_house_number_expression


class TestReplaceHouseNumberExpression(TestCase):
    def test_replace_house_number_expression(self) -> None:
        return_value = replace_house_number_expression("愛媛県松番市一番町3丁目3-6")
        self.assertEqual(return_value, "愛媛県松/ban市一/ban町3/tyoume3-6")
