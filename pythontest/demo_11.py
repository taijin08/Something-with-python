from msilib.schema import Class


class Person:
    """
    This is a sample class
    """
    def __init__(self, name, age): #__init__用双下划线开头结尾的，构造函数
        self.name = name #建立实例的一个属性
        self.age = age #__init__没有return语句
    def get_name(self): #类的方法必须第一个参数是self，即实例对象本身，不需要显式地传递值
        return self.name
    def get_age(self, age):
        d = {}
        d[self.name] = age
        return d
    kk = "human" #创建类的属性

GF = Person("gf", 19)
print(GF.name)
print(GF.age)
print(GF.get_name())
print(GF.get_age(22))

print(GF.kk)

del Person.kk #可以删除、增添和修改类的属性
Person.kk = "Animal"
print(GF.kk)
GF.mm = 90 #实例属性可以随意更改，但最好不要随便更改类属性
print(GF.__dict__) #实例属性不影响类属性，但如果是可变对象如列表，则修改实例属性也将修改类属性
print(Person.__dict__) #类属性影响实例属性

class Foo:
    def bar(self):
        print("This is a normal method of class")
f = Foo()
f.bar()
Foo.bar(f) #实例也可以显式地传给方法

print(Foo.bar) #通过类得到方法对象，为非绑定方法
print(f.bar) #通过实例得到方法对象，为绑定方法，通常实例调用的方法都是绑定方法

#有__get__(),__set__()和__delete__()方法的对象称之为描述器
print(Foo.__dict__["bar"].__get__(None,Foo)) #在self位置赋None，表示没有给定的实例，这说明是非绑定方法

print("-"*20)

class Foo2:
    lang = "Java"
    def __init__(self):
        self.lang = "python"

def get_class_attr(cls):
    return cls.lang
#这种函数太特异了，和类耦合太严重，应该避免这样写

print("Foo2.lang:", Foo2.lang)
r = get_class_attr(Foo2)
print("get class attribute:", r)
f = Foo2()
print("instance attribute:", f.lang)

print("-"*20)

class Foo3:
    lang = "Java"
    def __init__(self):
        self.lang = "python"
    @classmethod
    def get_class_attr(cls):
        return cls.lang
#这里使用@classmethod装饰器，其装饰的方法的参数中，第一个无需是self
#将一个函数转变成类的方法，在类里面定义，将类本身作为引用对象传入此方法：类方法
#用@classmethod装饰的方法，其参数引用的对象是类对象

print("Foo3.lang:", Foo3.lang)
r = Foo3.get_class_attr()
print("get class attribute:", r)
f = Foo3()
print("instance attribute:", f.lang)
print("instance get_class_attr:", f.get_class_attr())

print("-"*20)

import random
def select(n):
    a = random.randint(1, 100)
    return a - n > 0

class Foo4:
    def __init__(self, name):
        self.name = name
    def get_name(self, age):
        if select(age):
            return self.name
        else:
            return "the name is secret."

f = Foo4("luolaoshi")
name = f.get_name(22)
print(select(22))
print(name)

print("-"*20)

import random
class Foo5:
    def __init__(self, name):
        self.name = name
    def get_name(self, age):
        if self.select(age):
            return self.name
        else:
            return "the name is secret."
    @staticmethod
    def select(n):
        a = random.randint(1, 100)
        return a - n > 0
#尽管select(n)位于类的命名空间之内，但它却是一个独立的方法：静态方法
# 跟类没有关系，仅仅是为了免除前面所说的维护上的困难，写在类的作用域内的普通函数
#前面加上@staticmethod 装饰器，这个函数位于类的里面，但它不以self 为第一个参数。
# 当使用它的时候，可以通过实例调用，比如self.select(n)；也可以通过类调用这个方法，比如Foo.select(n)。

f = Foo5("luolaoshi")
name = f.get_name(22)
print(f.select(22))
print(name)