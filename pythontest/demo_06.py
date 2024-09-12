#并行迭代
a = "qiwsir"
b = "aasjjh"
zip(a, b) #如果参数是字典，那么只返回键的元组
result = list(zip(a, b))
print(result)
print(list(zip(*result))) #将元素一一对应地结为元组，序列长度不同就按最短的来
print(list(zip(a))) #只有一个参数是序列对象时的情况

a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]
d = []
for x, y in zip(a, b):
    d.append(x + y)
print(d)

week = ['monday', 'sunday', 'friday']
for (i,day) in enumerate(week):
    print(day + " is " + str(i))
print(list(enumerate(week))) #同时获得列表中的索引和元素

raw = "Do you love Canglaoshi? Canglaoshi is a good teacher."
raw_lst = raw.split()
for i, string in enumerate(raw_lst):
    if "Canglaoshi" in string:
        raw_lst[i] = "PHP"
print(" ".join(raw_lst))

squares = [x**2 for x in range(1, 10)] #列表解析
print(squares)

import random
number = random.randint(1,100)
guess = 0
while True:
    num_input = input("please input one integer that is in 1 to 100:")
    guess += 1
    if not num_input.isdigit():
        print("error")
        continue
    elif int(num_input) < 0 or int(num_input) >= 100:
        print("out of range")
        continue
    else:
        if int(num_input) == number:
            print("well done!")
            print("this number is {0}".format(number) + ", {0} guesses in total".format(guess))
            break
        elif int(num_input) > number:
            print("bigger")
            continue
        elif int(num_input) < number:
            print("smaller")
            continue

count = 0
while count < 5:
    print(count, "is less than 5")
    count += 1
else:
    print(count, "is not less than 5")

from math import sqrt
for n in range(99, 81, -1):
    root = sqrt(n)
    if root == int(root):
        print(n)
        break
else:
    print("none.")