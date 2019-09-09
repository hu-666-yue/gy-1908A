#字典
'''
key:value

key唯一
key必须不可变，数字，字符串，元组，列表（不可以），字典（不可以）

'''
# 增
#初次创建
d = {}
d1 = {'name':'小明同学','sex':'女'}
d1['age'] = 18
print (d1)

# 删
# 删除key
print(d1.pop('age'))
print(d1)
del d1 ['sex']
print(d1)

# 清空
d1.clear()
d1 = {}

# 改
d1['name'] = '小红同学'
print(d1)

# 查
print(d1['name'])

# 获取字典长度
print(len(d1))

# 成员判断，只能用key判断
print ('name' in d1)

# 字典拼接
d2 = {1:'234',2 : '346'}
d3 = {2:'567',4: '5789'}
d2.update(d3)

# 在某个字典末尾加上另一个字典
# 生成一个新的字典
c = dict(d2,**d3)
print(c)
print('2345')

