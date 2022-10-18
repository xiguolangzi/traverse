import datetime
import os

# 1.获取当前路径
print("当前文件路径：",os.getcwd())

# 2.切换路径
os.chdir("D:\python\pythonProject\excel001")
print("当前文件路径：",os.getcwd())

# 3.遍历当前路径下的所有“文件+文件夹”
dir_list = os.listdir()
print("当前路径下有哪些文件夹：",dir_list)

# 4.判断 是 文件夹 还是 文件
for d in dir_list:
    print(d,os.path.isdir(d),os.path.isfile(d))
    #输出结果： 文件名 + true/false + true/false
                       #是否为文件夹    #是否为文件

# 5.扫描，scandir("默认当前路径")
dir_list2 = os.scandir()
#输出结果是一个迭代器
print(dir_list2)
#需要通过遍历输出
for file in dir_list2:
    # 进一步输出名字，判断是不是文件夹
    print(file,file.name,file.is_dir())
    #查看文件信息（文件格式、文件大小、创建时间 等）
    print(file.stat())
    #获取其中的文件大小
    print(file.stat().st_size)
    #获取文件时间戳
    times = file.stat().st_ctime
    print(times)
    #时间戳转时间
    print(datetime.datetime.fromtimestamp(times))

# 6.统计编辑文件的数量
file_list3 = []
dir_list3 = []

for file in os.scandir():
    if file.is_dir():
        dir_list3.append(file.name)
    else:
        file_list3.append(file.name)
print("文件夹的数量是：{}".format(len(dir_list3)))
print("文件的数量是：{}".format(len(file_list3)))

# 7.名字过滤
demo_list = []
for name in  file_list3:
    #lower() 将 name 转成小写字母(排除包含大写字母)
    if "demo" in name.lower():
        demo_list.append(name)

print("*******************")
# 8.遍历所有文件、包括所有子目录下的文件
for dirpath,dirnames,files in os.walk("./"):
    print(dirpath,dirnames,files)
    #dirpath 路径
    #dirnames 所有 文件夹名 的列表
    #files 所有 文件名 的列表

# 9.glob 遍历
import glob
t_list = glob.glob("d*")
#当前路径下 d开头 的 文件
print(t_list)
#glob.glob("**")    获取当前目录的 文件 和 文件夹
#glob.glob("**/")   获取当前目录的 文件夹
#glob.glob("**",recursive=True)    获取 当前+所有子目录 的 文件 和 文件夹
#glob.glob("**/",recursive=True)   获取 当前+所有子目录 的 文件夹
#glob.glob("**/*.zip",recursive=True)   获取 当前+所有子目录 的 .zip 文件