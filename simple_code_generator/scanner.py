"""
  Created by Xiaozhong on 2018/11/7.
  Copyright (c) 2018/11/7 Xiaozhong. All rights reserved.
"""

from pathlib import Path

current_dir = Path()
models = []

# 填充字段字典
fill_objs = []


def load_models(dir_name):
    for pro_dir in dir_name.iterdir():
        if pro_dir.is_file() and pro_dir.match("*/model/*.java"):
            models.append(str(pro_dir))
            package_name = get_package_name(models[0])
            fill_objs.append({
                'package_name': package_name,
                'model_name': pro_dir.stem,
                'dao_name': pro_dir.stem + 'Dao',
                'component_name': pro_dir.stem.lower() + 'Dao',
                'lower_case_model_name': pro_dir.stem.lower(),
                'level': 'dao'
            })
        elif pro_dir.is_dir():
            load_models(pro_dir)


def get_package_name(file_name):
    with open(file_name, encoding="utf-8") as file_obj:
        while True:
            content = file_obj.readline()
            if content.startswith("package"):
                split_contents = content.split(" ")
                if ".model" in split_contents[1]:
                    package_name = (split_contents[1])[:split_contents[1].find(".model")]
                    return package_name


load_models(current_dir)
print(models)
print(fill_objs)