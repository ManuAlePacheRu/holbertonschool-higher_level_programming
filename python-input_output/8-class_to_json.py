#!/usr/bin/python3
"""クラスのオブジェクトを辞書に変換します。"""


def class_to_json(obj):
    """
    クラスのオブジェクトを辞書に変換します。

    Parameters:
        obj: オブジェクト
            変換するオブジェクト

    Returns:
        dict: オブジェクトの属性を含む辞書
    """
    return obj.__dict__
