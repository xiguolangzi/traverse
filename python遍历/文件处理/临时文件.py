## 创建 文件夹 的库
from tempfile import TemporaryDirectory
## 创建 文件 的库
from tempfile import TemporaryFile

# 1.创建临时文件夹
with TemporaryDirectory() as temp_dir:
    print("文件夹已经创建",temp_dir)
    #C:\Users\hubia\AppData\Local\Temp\tmpe2gidvfe  自动创建的路径，名称随机

# 2.创建临时文件
# mode 默认"w+b"读写二进制
with TemporaryFile(mode="w+") as temp_file:
    temp_file.write("我是搬运工")
    temp_file.seek(0) #将光标移动到0的位置
    data = temp_file.read()
    print(data)

# 3.临时文件可以设置关闭后清除或不清楚