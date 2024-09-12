print(hasattr(list, '__iter__')) #判断一个类型的对象是否是迭代器

lst = [1,2,3,4]
print(iter(lst))

class MyRange:
    def __init__(self, n):
        self.i = 1
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.i <= self.n:
            i = self.i
            self.i += 1
            return i
        else: raise StopIteration()

#自己编写迭代器对象，即编写类，其中实现__iter__()和__next__()方法。
# 当没有元素时，则引发StopIteration 异常。

x = MyRange(7)
m1 = [i+3 for i in x]
print(m1)
for item in m1: print(item, end=" ")

print("\n","-"*20)
m2 = (i+3 for i in x)
for item in m2:print(item)
print(m2)

print("\n","-"*20)
m3 = (i for i in range(9))
print(m3)
for item in m3 : print(item, end=" ")

print("\n","-"*20)

#定义生成器
def g():
    yield 0
    yield 1
    yield 2

print(g)
ge = g()
print(type(ge))
print(ge.__next__())
print(ge.__next__())
print(ge.__next__())
#含有yield关键词的函数是一个生成器对象，这个生成器对象也是迭代器。
#把含有yield语句的函数称作生成器。生成器是一种用普通函数语法定义的迭代器。
#yield语句的作用，就是在调用的时候返回相应的值。
ge2 = g()
for i in ge2:
    print(i)

def y_yield(n):
    print("You taked me.")
    while n > 0:
        print("before yield")
        yield n
        n -= 1
        print("after yield")

yy = y_yield(3) #没有执行函数体内语句
print(yy.__next__()) #遇到yield，返回值，并暂停
print(yy.__next__()) #从上次暂停位置继续执行
print(yy.__next__()) #从上次暂停位置继续执行

#一般的函数，都是止于return；作为生成器的函数，由于有了yield，则会遇到它挂起。

def fibs(max):
    """
    斐波那契数列的生成器
    """
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1

f = fibs(10)
for i in f:
    print(i, end=',')