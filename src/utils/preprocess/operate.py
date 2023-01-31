from interfaces.edit_address import EditAddress


def preprocess(original_address: str):
    preprocessing_address: str = EditAddress.fill_space(original_address)

    preprocessing_address = EditAddress.convert_full_width_digit_to_half_width_digit(preprocessing_address)

    preprocessing_address = EditAddress.convert_macron_to_hyphen(preprocessing_address)

    preprocessed_address: str = EditAddress.replace_house_number_expression(preprocessing_address)

    return preprocessed_address
