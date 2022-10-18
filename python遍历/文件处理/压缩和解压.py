import os
import zipfile

dir_list = os.listdir() #遍历当前路径
print(dir_list)

#mode默认"r"读，
# 1.压缩文件
'''
with zipfile.ZipFile("压缩文件名.zip","w") as zipobj:
    for file in dir_list:
        if file.endswith(".txt"):  #判断以.py结尾的文件
            zipobj.write(file)
# 2.读压缩文件
with zipfile.ZipFile("压缩文件名.zip","r") as zipobj:
    print(zipobj.namelist())  #namelist()获取压缩文件内部文件名的列表
'''

# 3.解压缩文件
with zipfile.ZipFile("压缩文件名.zip","r") as zipobj:
    # 将单个文件"a.txt" 解压 出来
    zipobj.extract("a.txt","./")
    # 将所有文件解压到指定文件
    zipobj.extractall("files/")
