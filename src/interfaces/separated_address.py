from interfaces.utils.check_type import check_type
from utils.extract.extract_city import extract_city
from utils.extract.extract_town import extract_town
from utils.extract_prefecture import extract_prefecture


class SeparatedAddress:
    def __init__(self, address: str):
        rest_address: str = address

        self.prefecture: str = check_type(extract_prefecture(address), str)
        rest_address = rest_address.replace(self.prefecture, "", 1)

        self.city: str = check_type(extract_city(rest_address), str)
        rest_address = rest_address.replace(self.city, "", 1)

        self.town: str = check_type(extract_town(rest_address), str)
        rest_address = rest_address.replace(self.town, "", 1)

        self.house_number: str = check_type("", str)
        rest_address = rest_address.replace(self.house_number, "", 1)

        self.building_name: str = check_type("", str)
        rest_address = rest_address.replace(self.building_name, "", 1)

        self.room_number: str = check_type("", str)
        rest_address = rest_address.replace(self.room_number, "", 1)

        if rest_address != "":
            print("Error出す")
