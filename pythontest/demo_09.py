from asyncio import wrap_future
from re import A


def fib(n):
    """
    递归生成一个斐波那契数列
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2) 

print(fib.__doc__)
n = int(input("input a int"))
lst = []
for i in range(n):
    lst.append(fib(i))
print(lst)

def bar():
    print("I am in bar()")
def foo(func): #函数作为对象可以当函数的参数
    func()

foo(bar)

def lst2str(func, seq):
    return [func(i) for i in seq]
numseq = [111,3.14,2.91]

print(lst2str(str, numseq))

#函数嵌套，里面还可以定义函数
def foo1():
    def foobar():
        print("李雨衡")
    foobar()
    print("忒der")

foo1()

def foo2():
    a = 1
    def bar():
        nonlocal a
        a = a + 1
        print("bar()a=", a)
    bar()
    print("foo2()a=", a)
foo2()

def foo3(fun):
    def wrap():
        print("start")
        fun()
        print("end")
        print(fun.__name__)
    return wrap

f = foo3(bar)
f()
# 装饰器：foo3()是装饰器函数，使用@foo3来装饰bar2()函数
# 装饰器本身就是一个函数，将被装饰的类或函数当做参数传递给装饰器函数
@foo3
def bar2():
    print("I am in bar2()")
bar2()


def foo4():
    a = 3
    def bar():
        return a
    return bar
f2 = foo4()
print(f2()) #在函数外面使用了函数里面的变量
#a 相对于 bar() 是自由变量，但在bar()中应用了这个自由变量
# bar()就是一个闭包：嵌套函数，并引用其所在函数环境的自由变量

#使用闭包来创建多个实例，更加简便
def parabola(a, b, c):
    def para(x):
        return a*x**2 + b*x + c
    return para
p = parabola(2, 3, 4)
print(p(5))