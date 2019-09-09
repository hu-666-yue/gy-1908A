# 方法定义
def jia_fa ():
    a = 1
    b = 2
    print(a+b)

# 方法调用
jia_fa()

# 无参数有返回值
def jia_fa ():
    a = 1
    b = 2
    return(a+b)

c = jia_fa()
print(c)

# 有参数有返回值
def jia_fa (a,b):
    return (a + b)

c = jia_fa(1,2)
print(c)

C  = jia_fa(2,3)
print(c)

def aa(a, b =2):
    return(a+b)

def zzz(*args,**kwargs):
    print(args)
    print(kwargs)

if __name__ =='__main__':
    程序的入口
    print()

