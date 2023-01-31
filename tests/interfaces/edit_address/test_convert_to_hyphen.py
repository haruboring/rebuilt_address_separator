from unittest import TestCase

from interfaces.edit_address import EditAddress


class TestConvertMacronToHyphen(TestCase):
    def test_convert_macron_to_hyphen1(self) -> None:
        return_value = EditAddress.convert_macron_to_hyphen("1ー1")
        self.assertEqual(return_value, "1-1")

    def test_convert_macron_to_hyphen2(self) -> None:
        return_value = EditAddress.convert_macron_to_hyphen("1ー1ー1-1")
        self.assertEqual(return_value, "1-1-1-1")


class TestConvertHouseNumberExpressionToHyphen(TestCase):
    def test_convert_house_number_expression_to_hyphen1(self) -> None:
        return_value = EditAddress.convert_house_number_expression_to_hyphen("1/tyoume5/banti3/gou")
        self.assertEqual(return_value, "1-5-3-")

    def test_convert_house_number_expression_to_hyphen2(self) -> None:
        return_value = EditAddress.convert_house_number_expression_to_hyphen("5-321/ban")
        self.assertEqual(return_value, "5-321-")
