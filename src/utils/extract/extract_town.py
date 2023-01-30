import re

from utils.preprocess.edit.reverse_house_number_expression import \
    reverse_house_number_expression


def extract_town(address: str) -> tuple[str, str]:
    if re.search("[0-9]+", address) is not None:
        town_and_rest_address: list[str] = re.split("[0-9]+", address, 1)
        town: str = town_and_rest_address[0]
        return reverse_house_number_expression(town), address.replace(town, "", 1)

    else:
        return address, ""
