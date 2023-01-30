def fill_space(address: str) -> str:
    address = address.replace(" ", "")
    address = address.replace("　", "")
    formatted_address: str = address.replace("　", "")

    return formatted_address
