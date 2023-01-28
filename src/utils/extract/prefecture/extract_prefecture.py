from data.prefecture_names import PREFECTURE_NAMES


def extract_prefecture(address: str) -> tuple[str, str]:

    for prefecture in PREFECTURE_NAMES:
        if prefecture in address:
            return (prefecture, address.replace(prefecture, ""))

    # 県名が存在しない
    return ("", address)
