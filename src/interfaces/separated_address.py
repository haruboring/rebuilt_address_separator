from interfaces.utils.check_type import check_type


class SeparatedAddress:
    def __init__(self, original_address):
        self.prefecture: str = check_type("", str)
        self.city: str = check_type("", str)
        self.town: str = check_type("", str)
        self.house_number: str = check_type("", str)
        self.building_name: str = check_type("", str)
        self.room_number: str = check_type("", str)
