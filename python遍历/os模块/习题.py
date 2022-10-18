'''
综合习题：
    1.遍历指定路径下所有.zip文件（包括子目录）；
    2.找出 文件大于50MB，最后修改时间超过30天的文件

'''
import datetime
import glob
import os
#D:\python\pythonProject\excel001
path = input("输入一个路径：")
#切换路径
os.chdir(path)
#遍历 当前目录+所有子目录 下 .zip 文件
files = glob.glob("**/*.zip",recursive=True)

for path_file in files:
    #获取文件大小
    file_sizes = os.stat(path_file).st_size
    #将字节转换成MB
    file_sizes_MB = file_sizes / 1024 / 1024
    #获取文件修改时间戳
    file_modify = datetime.datetime.fromtimestamp(os.stat(path_file).st_mtime)
    #将时间戳转成天
    days = (datetime.datetime.now()-file_modify).days
    if (file_sizes_MB < 50) and (days < 30):
        print(f"压缩包的名称：{path_file},文件大小{file_sizes_MB}MB,修改时间：{days}天前")