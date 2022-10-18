'''
综合应用：
    1.找到执行目录下所有距离上次修改时间超过1个月的md文件
    2.将所有文件重命名，在原来文件名开头加上最后修改日期
    3.创建一个锌的文件夹：长期未使用
    4.将所有文件移到 长期未使用 文件夹
    5.对 长期未使用 的文件夹 进行压缩处理，并在名字上加上今天的日期

'''

import os
import shutil
import zipfile
from datetime import datetime

path = input("输入一个路径：")
#1.切换路径
os.chdir(path)

file_list = []

#3.os.walk 遍历当前路径
for dirpath,dirname,files in os.walk("./"):
    print(dirpath,dirname,files)