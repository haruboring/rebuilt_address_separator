import re

from data.prefecture_names import PREFECTURE_NAMES
from data.special_city_names import SPECIAL_CITY_NAMES
from data.ward_names_of_tokyo import WARD_NAMES_OF_TOKYO
from interfaces.edit_address import EditAddress


class ExtractAddress:
    @staticmethod
    def extract_prefecture(address: str) -> tuple[str, str]:

        for prefecture in PREFECTURE_NAMES:
            if re.match(prefecture, address) is not None:
                return prefecture, address.replace(prefecture, "", 1)

        # 県名が存在しない
        return "", address

    @staticmethod
    def extract_city(address: str) -> tuple[str, str]:
        # 区で市区町村を区切るのは、東京23区のみ
        for ward_name in WARD_NAMES_OF_TOKYO:
            if re.match(ward_name, address) is not None:
                return ward_name, address.replace(ward_name, "", 1)

        # 分割ミスが発生する地名
        for special_city_name in SPECIAL_CITY_NAMES:
            if re.match(special_city_name, address) is not None:
                return special_city_name, address.replace(special_city_name, "", 1)

        # 市・町・村で分割する
        for special_pattern in ["市", "町", "村"]:
            match = re.search(".+?" + special_pattern, address)
            if match is not None:
                return EditAddress.reverse_house_number_expression(match.group()), address.replace(match.group(), "", 1)

        # 市名が存在しない
        return "", address

    @staticmethod
    def extract_town(address: str) -> tuple[str, str]:
        if re.search("[0-9]+", address) is not None:
            town_and_rest_address: list[str] = re.split("[0-9]+", address, 1)
            town: str = town_and_rest_address[0]
            return EditAddress.reverse_house_number_expression(town), address.replace(town, "", 1)

        else:
            return address, ""

    @staticmethod
    def extract_house_number(address: str) -> tuple[str, str]:
        match = re.match("[0-9〇一二三四五六七八九/tyoume/banti/ban/gou/no-]+", address)
        if match is not None:
            house_number: str = match.group()
            house_number = EditAddress.convert_house_number_expression_to_hyphen(house_number)
            house_number = EditAddress.convert_Chinese_numeral_to_half_width_digit(house_number)
            # 1-2-3-のようになっている場合がある
            if house_number[len(house_number) - 1] == "-":
                house_number = house_number[:-1]
            return house_number, address.replace(match.group(), "", 1)

        return "", address

    @staticmethod
    def extract_building_name(address: str) -> tuple[str, str]:
        building_name_and_rest_address: list[str] = re.split("[0-9]+", address, 1)
        building_name: str = building_name_and_rest_address[0]
        return EditAddress.reverse_house_number_expression(building_name), address.replace(building_name, "", 1)

    @staticmethod
    def extract_room_number(address: str) -> str:
        return EditAddress.reverse_house_number_expression(address)
