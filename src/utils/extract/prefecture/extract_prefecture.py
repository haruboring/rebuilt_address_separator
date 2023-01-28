from data.prefecture_names import PREFECTURE_NAMES


def extract_prefecture(address: str) -> tuple[str, str]:

    # 愛媛県伊予市.... 愛媛県民ホールなどで不適切に分割されてしまうので、先頭からのre.matchで一致不一致を見分ける
    for prefecture in PREFECTURE_NAMES:
        if prefecture in address:
            return (prefecture, address.replace(prefecture, ""))

    # 県名が存在しない
    return ("", address)
