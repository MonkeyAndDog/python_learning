"""
  Created by Xiaozhong on 2018/11/4.
  Copyright (c) 2018/11/4 Xiaozhong. All rights reserved.
"""

from pathlib import Path
import re


def generator(dir_input):
    """扫描指定目录下的*.java文件，并在当前目录下生成*_temp.java"""

    if dir_input.match("*/service"):
        return
    current_dir = dir_input
    count = 0
    for pro_dir in current_dir.iterdir():
        if pro_dir.match("template.java"):
            return
        if pro_dir.is_file() and pro_dir.match("*.java") and not pro_dir.match("*_temp.java"):
            s = str(dir_input) + "\\" + str(pro_dir.stem) + "_temp.java"
            wr_file = open(s, mode="w", encoding="utf-8")
            if wr_file.writable():
                wr_file.write("/**\n * 自动生成的代码\n */")
            count = count + 1
        elif pro_dir.is_dir():
            generator(pro_dir)
    if dir_input.is_dir():
        if count == 0:
            print(str(dir_input) + "没有生成任何代码")
        else:
            print(str(dir_input) + "生成了" + str(count) + "个代码文件")


# 当前目录下操作
c_dir = Path()

# 读取模板文件
template_file = open("template.java")
fill_obj = {
    'package_name': 'com.tccloud.webserver',
    'model_name': 'User',
    'dao_name': 'UserDao',
    'component_name': 'userDao',
    'lower_case_model_name': 'user'
}
result_content = ""
while True:
    read_content = template_file.readline()
    if not read_content:
        break
    if read_content.endswith("{\n"):
        result_content += read_content[0:-2].format(**fill_obj)
        result_content += "{\n"
        continue
    if read_content.endswith("}\n"):
        result_content += read_content
        continue
    else:
        result_content += read_content.format(**fill_obj)

wr_code = open("template_generate.java", mode="w", encoding="utf-8")
wr_code.write(result_content)
