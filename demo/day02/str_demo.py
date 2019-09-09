


#截取
a ='123456789'
print(a[0:5])
print(a[5:])
print(a[:5])
print(a[:-3])

#字符串倒叙
print(a[::-1])

#取出字符串中的字符
print(a[2])

#重复字符串
print(a * 3)


#字符串切片
d = '你,我,他'
print(d.split(','))

#去空格
e = '    你我他     '
print(e.strip())
print(e.strip())
print(e.replace(' ',''))

#替换
f = 'aabbccddee'   '123123'
print (f.replave(''))




g ='guoyasoft'
print(g.find("ya"))



u  = 'GET https://www.fiddler2.com/UpdateCheck.aspx?isBeta=False HTTP/1.1'
if __name__ =='__main__':
    print('请求方法：',r.split(' ')[0])
        a = r.split(':')[0]
    print('协议名称：',a.split(' ')[1])
    print('url:',r.split('/')[2])
        b = r.split('/')[3]
    print('请求路径:',b.split('?')[0])
        c = r.split('?')[1]
    print('请求内容:',c.split(' ')[0])
    print('协议版本:',r.split(' ')[2])



