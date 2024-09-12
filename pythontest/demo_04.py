s1 = set("www.sjtu.edu.cn")
print(s1) #创建集合，并只保留不重复的元素
#集合并不是序列，里面的元素必须是不可变的，但这个集合是可变的

s2 = set()
print(type(s2)) #创建一个空集合
sw = {}
print(type(sw)) #这样创建的是字典

s1.add('qiwsir')
print(s1)
s1.update("goo")
s1.update([2,3])
print(s1)

print(s1.pop()) #随机删除集合内一个元素，并返回其值
print(s1)
s1.remove("j") #能删除集合内指定的元素，若不含则报错
print(s1)
s1.discard('.') #能删除集合内指定的元素，若不含则不改变
print(s1)

f_set = frozenset("qiwsir") #创建不可修改的集合
s2.update({'w','s','t','u'})

#集合运算
print(s1 == s2)
print(s1 < s2)
print(s2.issubset(s1))
s3 = s1 | s2
print(s3)
s4 = s1 & s2
print(s4)
s5 = s1 - s2
s6 = s1.difference(s2)
print(s5);print(s6)
s7 = s1.symmetric_difference(s2)
print(s7)
