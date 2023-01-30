import re

from utils.edit.convert_to_half_width_digit import convert_Chinese_numeral_to_half_width_digit


def replace_house_number_expression(address: str) -> str:
    address = address.replace("丁目", "/tyoume")
    address = address.replace("番地", "/banti")
    address = address.replace("番", "/ban")
    address = address.replace("号", "/gou")
    formatted_address: str = address.replace("の", "/no")

    match = re.search("[〇-九]+/tyoume", address)
    if match is not None:
        matched_string: str = match.group()
        formatted_string = convert_Chinese_numeral_to_half_width_digit(matched_string)
        formatted_address = formatted_address.replace(matched_string, formatted_string, 1)

    return formatted_address
