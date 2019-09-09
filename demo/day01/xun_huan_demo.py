# for 循环
'''
for i in range(10):
    代码块
'''
#打印出100以内的奇数
for i in range (1,100,2):
    print (i)


for i in range (1,100):
    if(i%2 ==1):
         print(i)

#终止循环 break
for i in range (100):
    if (i == 5):
        break
    print(i)
#跳过本次循环 continue
for i in range(100):
    if (i%5 == 0):
        continue
    print(i)

#求出1+2+3.。。+100的和
def qiu_he():
    a = 0
    for i in range (1,101):
        a += i;
    print (a)

# 求出100！ 1*2*3..*100
def chengji():
    s = 1
    for i in range(1,101):
        s *= i
    print(s)


#求出九九乘法表（循环嵌套）
def jiu_jiu():
    for i in range(1, 10):
        for j in range(1, i + 1):
            print(j, "X", i, '=', i * j, "\t", end='', )
        print()

 #冒泡排序
def maopao():
    a = [90,43,2,63,6,3,4]
    for i in range(len(a)-1,0,-1):
        for j in range(i):
            if(a[j] > a[j+1]):
                a[j],a[j+1] = a[j+1],a[j]
    print(a)



#while
'''
i = 0
while:循环体
i=i+1
'''
for i in range (1,101,1):
    print(i)
i =1
while(i< 101):
    print(i)
    i = i + 1










