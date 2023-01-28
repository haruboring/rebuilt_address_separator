from interfaces.separated_address import SeparatedAddress
from utils.preprocess.operate import preprocess


def separate_address(original_address: str, zipcode: str) -> SeparatedAddress:
    print(original_address)
    # TODO: 郵便番号zipcodeを用いて、補完を行いたい。

    # 分割しやすい形にするための前処理
    preprocessed_address: str = preprocess(original_address)
    print(preprocessed_address)

    # 分割する
    separated_address: SeparatedAddress = SeparatedAddress(preprocessed_address)

    return separated_address


if __name__ == "__main__":
    separate_address("東京都大田市北千束一丁目56ー14　こだまルーミング一丁目302号室", "")
