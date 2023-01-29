def reverse_house_number_expression(address: str) -> str:
    address = address.replace("/tyoume", "丁目")
    address = address.replace("/banti", "番地")
    address = address.replace("/ban", "番")
    address = address.replace("/gou", "号")
    formatted_address: str = address.replace("/no", "の")

    return formatted_address
