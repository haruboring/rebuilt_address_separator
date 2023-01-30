from unittest import TestCase

from src.utils.edit.convert_to_half_width_digit import convert_Chinese_numeral_to_half_width_digit, convert_full_width_digit_to_half_width_digit


class TestConvertChineseNumeralToHalfWidthDigit(TestCase):
    def test_convert_Chinese_numeral_to_half_width_digit1(self) -> None:
        return_value = convert_Chinese_numeral_to_half_width_digit("一二三四五")
        self.assertEqual(return_value, "12345")

    def test_convert_Chinese_numeral_to_half_width_digit2(self) -> None:
        return_value = convert_Chinese_numeral_to_half_width_digit("一に曰わく、和を以て貴しとなし、さからうことなきを宗とせよ。")
        self.assertEqual(return_value, "1に曰わく、和を以て貴しとなし、さからうことなきを宗とせよ。")


class TestConvertFullWidthDigitToHalfWidthDigit(TestCase):
    def test_convert_full_width_digit_to_half_width_digit1(self) -> None:
        return_value = convert_full_width_digit_to_half_width_digit("２００１年生まれ")
        self.assertEqual(return_value, "2001年生まれ")

    def test_convert_full_width_digit_to_half_width_digit2(self) -> None:
        return_value = convert_full_width_digit_to_half_width_digit("お酒は２０歳になってから")
        self.assertEqual(return_value, "お酒は20歳になってから")
