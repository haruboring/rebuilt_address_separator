from utils.preprocess.edit.convert_to_half_width_digit import convert_full_width_digit_to_half_width_digit
from utils.preprocess.edit.convert_to_hyphen import convert_to_hyphen
from utils.preprocess.edit.fill_space import fill_space
from utils.preprocess.edit.replace_house_number_expression import replace_house_number_expression


def preprocess(original_address: str):
    preprocessing_address: str = fill_space(original_address)

    preprocessing_address = convert_full_width_digit_to_half_width_digit(preprocessing_address)

    preprocessing_address = convert_to_hyphen(preprocessing_address)

    preprocessed_address: str = replace_house_number_expression(preprocessing_address)

    return preprocessed_address
