#!/usr/bin/python3
"""このスクリプトは、Python 3で実行されることを想定しています。"""


class Student:
    """学生を表すクラスです。"""

    def __init__(self, first_name, last_name, age):
        """
        Studentオブジェクトを初期化します。

        Args:
            first_name (str): 学生の名字。
            last_name (str): 学生の苗字。
            age (int): 学生の年齢。
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        学生オブジェクトをJSONライクな辞書に変換します。

        Returns:
            dict: 学生の属性を含む辞書。
        """
        return self.__dict__
