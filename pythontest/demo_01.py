print("Hello World")
print("\nHelloWorld")
print("This is a Python test")

stra = 'I love python'
print(stra.isalpha())

print(stra[0:3])
m = input("find a letter:\n")
print(m in stra)
print(stra.index(m))

c = stra.split(" ")
print(c)
cc = "*".join(c)
print(cc)

str1 = c[0]
str2 = c[1]
print(str1 + str2)

print('This string has {lenth} letters'.format(lenth=str(len(stra)))) #格式化字符串
print('This string has {0:^10} letters'.format(str(len(stra))))
