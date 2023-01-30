import re

from utils.preprocess.edit.reverse_house_number_expression import reverse_house_number_expression


def extract_room_number(address: str) -> str:
    return reverse_house_number_expression(address)
