def myfunction(a, b):
    c = a + b
    return c

x, y = input("input two int")
x, y = int(x), int(y)
print(x, y)
print(myfunction(x, y))

r = myfunction
print(r(10,39))

def fibs(n):
    """
    生成一个斐波那契数列
    """
    result = [0,1]
    for i in range(n-2):
        result.append(result[-2] + result[-1])
    return result

fibs.kk = 90

print(fibs.__doc__)
print(fibs.__name__)
print(fibs.__module__)
print(fibs.kk)
print(fibs(9))

def func(x, *arg): #用*arg收集值，得到元组类型的数据
    print(x)
    result = x
    print(arg)
    for i in arg:
        result += i
    return result

print(func(1,2,3,4,5,6,7,8,9,10)) #用**kargs收集值，得到字典类型的数据

def foo(**kargs):
    print(kargs)

foo(a=1,b=2,c=3)
