from interfaces.edit_original_address import EditOriginalAddress


def preprocess(original_address: str):
    preprocessing_address: str = EditOriginalAddress.fill_space(original_address)

    preprocessing_address = EditOriginalAddress.convert_full_width_digit_to_half_width_digit(preprocessing_address)

    preprocessing_address = EditOriginalAddress.convert_macron_to_hyphen(preprocessing_address)

    preprocessed_address: str = EditOriginalAddress.replace_house_number_expression(preprocessing_address)

    return preprocessed_address
