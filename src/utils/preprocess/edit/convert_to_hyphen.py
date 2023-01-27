import re


def convert_to_hyphen(address: str) -> str:
    formatted_address: str = address

    # 1ー43のような形は一つ目が番地と考えられるのでsearchでいい
    match = re.search("([0-9]+ー)+[0-9]+", address)
    if match is not None:
        matched_string: str = match.group()
        formatted_string: str = matched_string.replace("ー", "-")
        formatted_address = address.replace(matched_string, formatted_string, 1)

    return formatted_address
