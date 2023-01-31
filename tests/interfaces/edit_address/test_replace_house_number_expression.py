from unittest import TestCase

from interfaces.edit_address import EditAddress


class TestReplaceHouseNumberExpression(TestCase):
    def test_replace_house_number_expression1(self) -> None:
        return_value = EditAddress.replace_house_number_expression("愛媛県松番市一番町3丁目3-6")
        self.assertEqual(return_value, "愛媛県松/ban市一/ban町3/tyoume3-6")

    def test_replace_house_number_expression2(self) -> None:
        return_value = EditAddress.replace_house_number_expression("番地番番番地号の号丁目")
        self.assertEqual(return_value, "/banti/ban/ban/banti/gou/no/gou/tyoume")
