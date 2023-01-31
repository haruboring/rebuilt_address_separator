from unittest import TestCase

from interfaces.edit_original_address import EditOriginalAddress


class TestReverseHouseNumberExpression(TestCase):
    def test_reverse_house_number_expression1(self) -> None:
        return_value = EditOriginalAddress.reverse_house_number_expression("302/gou室")
        self.assertEqual(return_value, "302号室")

    def test_reverse_house_number_expression2(self) -> None:
        return_value = EditOriginalAddress.reverse_house_number_expression("松山一/ban町校")
        self.assertEqual(return_value, "松山一番町校")
