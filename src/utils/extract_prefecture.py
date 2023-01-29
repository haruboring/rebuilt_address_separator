import re

from data.prefecture_names import PREFECTURE_NAMES


def extract_prefecture(address: str) -> str:

    for prefecture in PREFECTURE_NAMES:
        if re.match(prefecture, address) is not None:
            return prefecture

    # 県名が存在しない
    return ""
