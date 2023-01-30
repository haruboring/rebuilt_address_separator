def convert_full_width_digit_to_half_width_digit(string: str) -> str:
    """
    args: address_data: str (example: 東京都港区元麻布1-６-9)
    return: formatted_address_data: str (example: 東京都港区元麻布1-6-9)
    """

    MAPPING_DICTIONARY: dict[str, str] = {
        "１": "1",
        "２": "2",
        "３": "3",
        "４": "4",
        "５": "5",
        "６": "6",
        "７": "7",
        "８": "8",
        "９": "9",
        "０": "0",
    }

    formatted_string: str = ""

    for character in string:
        if character in MAPPING_DICTIONARY.keys():
            formatted_string += MAPPING_DICTIONARY[character]
        else:
            formatted_string += character

    return formatted_string


def convert_Chinese_numeral_to_half_width_digit(string: str) -> str:
    """
    args: address_data: str (example: 東京都港区元麻布1-六-9)
    return: formatted_address_data: str (example: 東京都港区元麻布1-6-9)
    """

    MAPPING_DICTIONARY: dict[str, str] = {
        "一": "1",
        "二": "2",
        "三": "3",
        "四": "4",
        "五": "5",
        "六": "6",
        "七": "7",
        "八": "8",
        "九": "9",
        "〇": "0",
    }

    formatted_string: str = ""

    for character in string:
        if character in MAPPING_DICTIONARY.keys():
            formatted_string += MAPPING_DICTIONARY[character]
        else:
            formatted_string += character

    return formatted_string
