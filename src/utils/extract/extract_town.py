import re


def extract_town(address: str) -> str:
    town_and_rest_address: list[str] = re.split("[0-9]+", address, 1)
    town: str = town_and_rest_address[0]
    return town
