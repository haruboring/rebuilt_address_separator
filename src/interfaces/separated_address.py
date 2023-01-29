from interfaces.utils.check_type import check_type
from utils.extract.city.extract_city import extract_city
from utils.extract.prefecture.extract_prefecture import extract_prefecture


class SeparatedAddress:
    def __init__(self, address: str):
        self.prefecture: str = check_type(extract_prefecture(address), str)
        city = extract_city(address.replace(self.prefecture, "", 1))
        self.city: str = check_type(city, str)
        self.town: str = check_type("", str)
        self.house_number: str = check_type("", str)
        self.building_name: str = check_type("", str)
        self.room_number: str = check_type("", str)
