#!/usr/bin/python3

from json import dump, load


"""基本的なシリアル化モジュールを追加する"""


def シリアライズしてファイルに保存(data, filename):
    """シリアライズ"""
    with open(filename, 'w', encoding="UTF-8") as ファイル新:
        dump(data, ファイル新)


def load_and_deserialize(filename):
    """読み込みとデシリアライズ"""
    with open(filename, 'r', encoding="utf-8") as ファイル新:
        return load(ファイル新)
