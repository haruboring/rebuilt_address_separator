import re

from utils.preprocess.edit.reverse_house_number_expression import reverse_house_number_expression


def extract_building_name(address: str) -> str:
    building_name_and_rest_address: list[str] = re.split("[0-9]+", address, 1)
    building_name: str = building_name_and_rest_address[0]
    return reverse_house_number_expression(building_name)
