from typing import Any


def check_type(data_to_be_assigned: Any, expected_type_name: type) -> Any:
    """
    type check: data_to_be_assignedがexpected_type_name型か判断し、
        Trueならばdata_to_be_assignedを、Falseならば、実行時エラーを起こさないために、空文字をreturnする。
        (このプログラムでは中身を全てstrとして処理しているため。)

    Parameters
    ----------
    data_to_be_assigned: Any, expected_type_name: type

    Returns
    -------
        Any (data_to_be_assigned or "")
    """
    try:
        if type(data_to_be_assigned) is expected_type_name:
            return data_to_be_assigned

        raise TypeError("クラスへの代入時に型エラーが生じています。")

    except TypeError as error_message:
        print(error_message)

        return ""


def check_list_type(list_data_to_be_assigned: list[Any], expected_list_type_name: type) -> list[Any]:
    """
    type list check: src/functions/check_type.pyを利用してlist型の各要素が期待している型かどうかを判断し、返す。

    Parameters
    ----------
        list_data_to_be_assigned: list[Any], expected_list_type_name: type

    Returns
    -------
        list[Any]
    """
    for value_of_list in list_data_to_be_assigned:
        check_type(value_of_list, expected_list_type_name)

    return list_data_to_be_assigned
