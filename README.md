# Python学习项目

## 1. 起步
> Python 3.7.0 版本
1. Linux环境：
    * 编辑器：Geany
    * 运行展示：Terminal
    * 感觉：Linux系统环境比较合适编程，但是由于在虚拟机情况下性能并不是太好（不过并不妨碍学习）。另一方面，编辑器功能的局限性对于新手来说是个好事，
    并不妨碍学习的同时还能提前接触到各种错误。
2. Windows环境：
    * 编辑器：PyCharm Professional版本
    * 运行展示：IDE内置虚拟终端
    * 感觉：IDE功能强大，操作感觉上比较便捷，但是并不利于新手刚学习Python（太过强大的提示功能和自动补全功能导致有些错误被扼杀在了摇篮里）

## 2. 变量和数据类型
> 变量命名使用小写，下划线分割单词。（下划线命名风格）
1. Python中并不声明变量类型，直接变量名称就可以了。
2. 使用 `str()` 、 `int()` 、 `float()` 之类的方法来强制转换类型，防止出错。
3. 注释使用 `#` 标记

## 3. 列表
1. 在Python中列表使用 `[]` 来表示， 并用 `,` 号分割其中数据。
2. 增删改查列表内容：
    1. 增加：
        1. 末尾添加： `list_name.append(item)` 。
        2. 指定位置添加： `list_name.insert(index, item)` 。
    2. 删除：
        1. 指定位置删除： `del list_name[index]` 。
        2. 删除并弹出元素： `item_name = list_name.pop()` 或者 `item_name = list_name.pop(index)` 。
        3. 删除指定值： `list_name.remove(item)`
    3. 更改：
        1. 更改指定位置元素： `list_name[index] = item` 。
    4. 访问其中元素：
        1. 访问指定位置的元素： `list_name[index]` 。
        2. 访问最后一个元素： `list_name[-1]` 。           
3. 组织列表
    1. 使用 `sort()` 对列表永久排序。
    2. 使用 `sorted()` 对列表临时排序。
    3. 反转列表 `reverse()` 。
    4. 确定列表长度 `len(list_name)` 。
4. 使用 `range(start, end)` 创建数字列表
5. 简单统计计算
    1. `sum(list_name)` 求列表和。
    2. `max(list_name)` 求最大值。
    3. `min(list_name)` 求最小值。
6. 列表切片
    1. 知道起始位置和终止位置： `list_name[start:end]`
    2. 从起始位置到指定位置： `list_name[:end]`
    3. 从指定位置到末尾： `list_name[start:]`
    4. 获取最后一个元素： `list_name[-3:]` 获取最后三个元素
    5. 复制列表： `copy_list = list[:]`
7. 元组
    1. 在Python中使用 `()` 来表示元组， 元组就是不可变的列表， 如： `cell_name = (200, 50)` 。

## 4. `for` 循环
1. 一般用法：
    ```
    items = []
    for item in items:
        print(item)
    ```
2. 带指定次数的循环：
    ```
    # 循环四次， 输出 1， 2， 3， 4
    for value in range(1, 5):
        print(value)
    ```
3. 列表解析：
    ```
    # 生成一个1-10的平方列表
    squares = [value**2 for value in range(1, 11)]
    ```
