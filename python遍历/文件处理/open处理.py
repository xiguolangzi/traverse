######## 1. open
#mode: tr 文本读取（默认文本读），br 二进制读取(图片、视频等)
#使用open 是一个stream 流对象，f 接收
f = open("a.txt",mode="tr")
#读取10个字节,返回
context = f.read(10)
print(context)
f.close()


######## 2.with
#with 缩进 不需要close,超过缩进 自动不在用f
with open("a.txt") as f:
    context = f.read()
    print(context)

######## 3.写文件(覆盖之前的文件)
with open("b.txt",mode="w") as f:
    f.write("完美世界")

####### 4.写文件(追加)
#a = append 追加
with open("b.txt",mode="a") as f:
    f.write("斗罗大陆")

####### 5.创建临时文件tempfile-TemporaryFile


####### 6.临时文件夹
