def add(x):
    x += 3
    return x

numbers = range(10)
print(list(numbers))
new_numbers = []
for i in numbers:
    new_numbers.append(add(i))
print(new_numbers)

new_numbers = [i+3 for i in numbers]
print(new_numbers)

lam = lambda x:x+3 #引入参数，运行公式，返回计算后的值
n2 = []
for i in numbers:
    n2.append(lam(i))
print(n2)

g = lambda x,y:x**y
n = 4
print([g(n,i) for i in range(n)])

print(list(map(add, numbers))) #对可迭代对象的每个元素依次应用func的方法

lst1 = [1, 2, 3, 4, 5]
lst2 = [6, 7, 8, 9, 0]
lst3 = [7, 8, 9, 2, 1]
print(list(map(lambda x,y,z:x+y+z, lst1,lst2,lst3)))

from functools import reduce
print(reduce(lambda x,y:x+y, [1,2,3,4,5])) 
#Apply a function of two arguments cumulatively to the items of a sequence, from left
# to right, so as to reduce the sequence to a single value.

numbers = range(-5,5)
filst = list(filter(lambda x:x>0, numbers))
print(filst) #过滤掉不是TRUE的元素

m = [[1,2],[3,4],[5,6]]
print(list(zip(*m))) #用zip函数实现矩阵的转置




