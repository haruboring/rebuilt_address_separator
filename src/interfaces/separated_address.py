from interfaces.utils.check_type import check_type
from interfaces.extract_address import ExtractAddress

class SeparatedAddress:
    def __init__(self, preprocessed_address: str, original_address: str):
        rest_address: str = preprocessed_address

        self.original_address: str = original_address

        prefecture, rest_address = ExtractAddress.extract_prefecture(rest_address)
        self.prefecture: str = check_type(prefecture, str)

        city, rest_address = ExtractAddress.extract_city(rest_address)
        self.city: str = check_type(city, str)

        town, rest_address = ExtractAddress.extract_town(rest_address)
        self.town: str = check_type(town, str)

        house_number, rest_address = ExtractAddress.extract_house_number(rest_address)
        self.house_number: str = check_type(house_number, str)

        building_name, rest_address = ExtractAddress.extract_building_name(rest_address)
        self.building_name: str = check_type(building_name, str)

        room_number = ExtractAddress.extract_room_number(rest_address)
        self.room_number: str = check_type(room_number, str)

    def __str__(self):
        return (
            "original_address = " + self.original_address + "\n"
            "prefecture = " + self.prefecture + "\n"
            "city = " + self.city + "\n"
            "town = " + self.town + "\n"
            "house_number = " + self.house_number + "\n"
            "building_name = " + self.building_name + "\n"
            "room_number = " + self.room_number + "\n"
        )
