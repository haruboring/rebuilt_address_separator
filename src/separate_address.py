from interfaces.separated_address import SeparatedAddress
from utils.preprocess.operate import preprocess


def separate_address(original_address: str, zipcode: str) -> SeparatedAddress:
    # TODO: 郵便番号zipcodeを用いて、補完を行いたい。

    # 分割しやすい形にするための前処理
    preprocessed_address: str = preprocess(original_address)

    # 分割する
    separated_address: SeparatedAddress = SeparatedAddress(preprocessed_address)

    return separated_address
