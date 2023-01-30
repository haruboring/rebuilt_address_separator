import re

from utils.preprocess.edit.reverse_house_number_expression import reverse_house_number_expression
from utils.preprocess.edit.convert_to_hyphen import convert_house_number_expression_to_hyphen
from utils.preprocess.edit.convert_to_half_width_digit import convert_Chinese_numeral_to_half_width_digit

def extract_house_number(address: str) -> str:
    match = re.match("[0-9〇一二三四五六七八九/tyoume/banti/ban/gou/no-]+", address)
    if match is not None:
        house_number: str = match.group()
        house_number = convert_house_number_expression_to_hyphen(house_number)
        house_number = convert_Chinese_numeral_to_half_width_digit(house_number)
        return house_number

    return ""
