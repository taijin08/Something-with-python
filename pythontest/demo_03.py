t = 123, 'abc', [1,2,'hello']
print(t)
print(type(t))

t2 = ('python', 1, t)
print(t2)

print(dir(tuple)) #元组不可以修改

print(t.__len__())
tt1 = (3)
print(type(tt1))
tt2 = (3,)
print(type(tt2))

tls = list(t) #元组与列表可以相互转换
print(tls)
tpl = tuple(tls)
print(tpl)

mydict = {} #字典
person = {"name":"hhh","site":"hhh.com","language":"python"} #键/值对
print(person)
person["name2"] = "qqq"
print(person) #字典是可变的对象

name = (["first", "Google"], ["second", "Yahoo"])
web = dict(name)
print(web) #用元组构造字典
website = {}.fromkeys(("third", "forth"), "facebook")
print(website) #键必须是不可变的数据类型，值可以变

print(person["name"]) #访问字典的值
person["name"] = "ttt"
print(person)
del person["name"]
print(person)

city_code = {"suzhou":"0512", "tangshan":"0315", "hangzhou":"0571"} #用字典完成格式化字符串
strr ="Suzhou is a beautiful city, its area code is {suzhou}".format(**city_code)
print(strr)

print(id(city_code))
cd = city_code.copy()
print(id(cd)) #用copy可以在内存中另辟一个空间，但列表对象仍是复制了引用，即所谓浅拷贝

import copy #导入copy模块，使用deepcopy可以完全地创造另一个空间
x = {"lang":["python","java"], "name":"qqq"}
z = copy.deepcopy(x)
print(id(x["lang"]))
print(id(z["lang"]))

z.clear() #无返回值，只是清空字典，并不删除
print(z)

print(x.get("lang")) #得到某个键的值，若无此键则返回None
print(x.setdefault("lang")) #得到某个键的值，若无此键则增加键，并添加一个None值
print(x.setdefault("kk", "nn"))  #若一并写出值，则增添这个键值对
print(x)

print(x.items())
print(x.keys())
print(x.values())

m = input("input a key")
n = x.pop(m,"key not in dict") #返回第一个参数的值并删除此键值对，若无此键则返回第二个参数
print(n)
print(x)
print(x.popitem()) #随机返回一个键值对并在字典里删除它

d1 = {"lang":"py"}
d2 = {(1,2,3):"44"}
d1.update(d2) #更新字典的内容
print(d1)
d1.update([('dd',"33")])
print(d1)
