from interfaces.utils.check_type import check_type
from utils.extract.extract_building_name import extract_building_name
from utils.extract.extract_city import extract_city
from utils.extract.extract_house_number import extract_house_number
from utils.extract.extract_prefecture import extract_prefecture
from utils.extract.extract_room_number import extract_room_number
from utils.extract.extract_town import extract_town


class SeparatedAddress:
    def __init__(self, address: str):
        rest_address: str = address

        self.original_address: str = address

        prefecture, rest_address = extract_prefecture(address)
        self.prefecture: str = check_type(prefecture, str)

        city, rest_address = extract_city(rest_address)
        self.city: str = check_type(city, str)

        town, rest_address = extract_town(rest_address)
        self.town: str = check_type(town, str)

        house_number, rest_address = extract_house_number(rest_address)
        self.house_number: str = check_type(house_number, str)

        building_name, rest_address = extract_building_name(rest_address)
        self.building_name: str = check_type(building_name, str)

        room_number = extract_room_number(rest_address)
        self.room_number: str = check_type(room_number, str)

    def debug_print(self):
        print("original_address = " + self.original_address)
        print("prefecture = " + self.prefecture)
        print("city = " + self.city)
        print("town = " + self.town)
        print("house_number = " + self.house_number)
        print("building_name = " + self.building_name)
        print("room_number = " + self.room_number)
        print()
