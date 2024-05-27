#!/usr/bin/python3
"""JSON ファイルからオブジェクトを読み込む"""
import json


def load_from_json_file(filename):
    """
    JSON ファイルからオブジェクトを読み込む。

    Args:
        filename (str): 読み込むファイルの名前。

    Returns:
        object: JSON ファイルから読み込んだオブジェクト。

    Raises:
        FileNotFoundError: 指定されたファイルが見つからない場合。
        JSONDecodeError: JSON ファイルの形式が無効な場合。
    """
    with open(filename, 'r', encoding="utf-8") as file_create_obj:
        return json.load(file_create_obj)
