"""
方式1：
导入格式：   import 包名.模块名
            包名就是文件夹名    模块名就是文件名字
使用格式：   包名.模块名.工具   (类名、函数、变量)
"""
import _fox.ppap

print(_fox.ppap._add(1, 2))
"""
方式2：
导入格式：   from 包名.模块名 import 所需的工具
使用格式：   工具   (类名、函数、变量)
"""
from _fox.ppap import _sub

print(_sub(233, 100))
