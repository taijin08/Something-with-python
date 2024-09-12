print(4 > 3 and 4 < 2) #与
print(4 < 2 and 4 > 3) #短路，可以减少计算量
print(4 < 2 or 4 > 3) #或
print( not(4 < 3) ) #非

import math
from re import A
print(math.pow(3,2))

from math import pow
print(pow(3,2))

from math import pow as pingfang #导入函数并赋予新名字
print(pingfang(3, 2))

from math import * #直接将所有math中的函数都导入
print(sqrt(9))

x, y, z = 1, 2, 3
print(x, y, z)

a = 2
b = 9
a,b = b,a
print(a, b) #变量对调

m = n = "kk"
print(m is n) #链式赋值，两个变量指向一个对象

num = int(input("input a number:\n"))
# 条件语句
if num >= 10:
    print("the number is {0}".format(num))
elif num == 2:
    print("num = 2")
else:
    print("error") 

x = int(input("input x:\n"))
y = int(input("input y:\n"))
a = "kk" if x > y else "nn" #三元操作符
print(a)

str1 = "www.isjtu.edu.cn"
for item in str1: #for循环的对象一定是可迭代的
    print(item) 
slt = str1.split(".")
for item in slt:
    print(item, end="-*-")
print("\n")
for idex in range(len(slt)):
    print(slt[idex])

d1 = {'website': 'www.itdiffer.com', 'lang': 'python', 'author': 'laoqi'}
for k in d1.items():
    print(k)

R1 = range(0,9,2) #range(start,stop, step)
print(R1, type(R1), list(R1))
R2 = range(0,-9,-1)
print(list(R2))

pythoner = ['I', 'am', 'a', 'pythoner', 'I', 'am', 'learning', 'it', 'with', 'qiwsir']
pyindex = range(len(pythoner)) #获得列表内每一个元素的索引
print(list(pyindex)) 


