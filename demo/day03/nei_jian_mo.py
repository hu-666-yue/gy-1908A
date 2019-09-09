# python 提供的内置模块
#直接import 导入使用
#第三方模块
'''
a = 1
print('sss')
    作用，输入到控制台
    参数，要打印的对象，and 修改结尾符号
b = '11111'
    作用，查看字符串，
len (b)
range(1,2)
int(b)
str()
list(()
dict()
tuple（）
    作用，把变量从其他类型转换为元组类型
    参数，要转换的变量
'''

#作用，打开一个文件
# 参数1，文件路径，
# 参数2r 读文件先清空文件内容，然后在写入 a可写
f = open('D:\\softwareData\\python\\gy-1908\\day03\\test','r',encoding ='utf-8'
)
print(f. readlines())
#关闭文件
f.close()


# import os
dirs  = os. lisedir('../day03')
print(dirs)