import re

from data.special_city_names import SPECIAL_CITY_NAMES
from data.ward_names_of_tokyo import WARD_NAMES_OF_TOKYO


def extract_city(address: str) -> str:
    # 区で市区町村を区切るのは、東京23区のみ
    for ward_name in WARD_NAMES_OF_TOKYO:
        if re.match(ward_name, address) is not None:
            return ward_name

    # 分割ミスが発生する地名
    for special_city_name in SPECIAL_CITY_NAMES:
        if re.match(special_city_name, address) is not None:
            return special_city_name
    # 市・町・村で分割する
    for special_pattern in ["市", "町", "村"]:
        match = re.search(".+" + special_pattern, address)
        if match is not None:
            return match.group()

    # 市名が存在しない
    return ""
