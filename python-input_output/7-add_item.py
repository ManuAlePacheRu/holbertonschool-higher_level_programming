#!/usr/bin/python3
"""すべての引数をPythonリストに書き込んでファイルに保存します"""

import os
import json
from sys import argv

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
argvs = argv[1:]
arg_list = []

# 引数をリストに追加
for i in (argvs):
    arg_list.append(i)

if os.path.isfile(filename):
    # ファイルが存在する場合は、その内容を読み込んで追加
    arg_listy = load_from_json_file(filename)
    for newelem in (arg_list):
        arg_listy.append(newelem)
    save_to_json_file(arg_listy, filename)
else:
    # ファイルが存在しない場合は、新しいリストを保存
    save_to_json_file(arg_list, filename)
