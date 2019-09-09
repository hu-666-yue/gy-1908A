X = [1,2,3,4,5,6,7,8,9]

#新增数据
#在列表最后新增单个数据
X.append(0)
print(X)

#在列表的某个位置新增单个数据
X.insert(1,10)
print(X)

#在列表最后新增多个数据
z = [1,2,3]
X.extend(z)

#删除数据
print(X.pop())
print(X)
print(X.pop(-2))
print(X)

#根据内容删除数据
X.remove(2)
print(1)

#修改列表中的数据

'''
列表中元素可被更改，元祖中的元素不能被修改

'''


