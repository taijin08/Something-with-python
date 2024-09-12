print(list(reversed("abcd"))) #反转字符串，返回列表

lst = ["py","c",22]
print(lst*3)

la = [1, 2, 3]
lb = [4, "hello"]
la.extend(lb) #扩容，但无返回值
print(la)
la.extend("abcd")
print(la)

x = la.count("4") #统计列表中相同元素的个数
print(x)
x = la.count(4)
print(x)

lc = ["www","sjtu","edu","cn"]
print('.'.join(lc)) #用''里面的东西连接几个字符串

la.insert(0, "python") #在index位置添加新元素
print(la[0])
print(la[0:])

kk = input("pop a word: \n") 
if kk in lc:
    idex = lc.index(kk)
    aa = lc.pop(idex) #pop返回并删除列表中某索引处的元素
    print(lc)
    print(aa)
else:
    print("not in list")

b = reversed(lc)
b = list(b)
print(b)
print(b.reverse()) #list.reverse不返回值
print(b)


numlst = [6, 1, 5, 3, 7]
xxx = numlst
numlst.sort() #sort也不返回值
print(numlst)
print(xxx) #可见是在原处修改的
strlst = ['w','sjtu','edu','cn']
strlst.sort(key= len, reverse= True) #按关键字排序，顺序或倒序
print(strlst)

mat = [[1,2,3], [4,5,6],[7,8,9]] #多维列表（矩阵）
print(mat[0][1])
