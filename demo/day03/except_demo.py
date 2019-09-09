
 def div(a,b):
     try:
         C = a/b
     except ZeroDivisionError:
         print('除数不能为0')
         return

     return  C
print(div(19,0))




def operate_file():
    try:
        # open("test.txt",'w')
        g = open ('test.txt','w')
        g.read()
        g.close()
        g.write('sssss')
    except  FileNotFoundError:
        print('文件不存在')
    except ValueError:
        print('文件已关闭')












