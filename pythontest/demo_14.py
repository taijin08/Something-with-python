class SP:
    name = "zx\sx"

a = SP()
a.age = 28
print(a.__dict__)

class Spring:
    __slots__ = ("tree", "flower")
    #特殊属性__slots__，不能通过实例修改此属性的值。

print(dir(Spring))
t = Spring()
print(t.__slots__)
f = Spring()
print(f.__slots__)
#类属性已经赋值了，那么通过任何一个实例属性都能得到同样的值。

Spring.flower = "huahua"
print(f.flower)
print(id(f.__slots__) == id(Spring.__slots__)) #用于节省内存
#对实例属性来讲，类的静态数据是只读的，不能修改。只有通过类属性才能修改。
f.tree = "shushu"
print(Spring.tree)
#但尚未赋值的属性，能通过实例赋值。但实例属性的值并不能修改类属性的值。


class A:
    def __getattr__(self, name):
        print("using getattr")
        #如果name被访问，但同时它不存在，那么此方法被调用。
    def __setattr__(self, name, value):
        print("using setattr")
        self.__dict__[name] = value
        #如果要给name 赋值，就调用这个方法


a1 = A()
a1.x
a1.x = 8
print(a1.x)
