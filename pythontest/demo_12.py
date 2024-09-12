#继承
class P:
    def __init__(self):
        print("Crazy Thursday V me 50")
    name = "KFC"
    def Yaofan(self, num):
        self.bargan = num
        print("Fuge V {0}".format(num))

class C(P): #P是父类，C是子类，单继承，就是只从一个父类里继承
    m = 90
    def __init__(self, kk): #父类对应不分的重写，继承没有重写的部分
        self.kk = kk
        print("Crazy Thursday")

c = C(99)
print(C.__base__)
print(C.__dict__, c.__dict__)
#当实例刚刚建立时，__dict__是空的，只有建立实例属性之后，它才包括其内容。
#实例的__dict__和类的__dict__是有所区别的，即实例属性和类属性不同。
c.Yaofan(100) #可以调用父类的函数
print(c.bargan, c.name)

class K(C):
    def __init__(self, kk):
        C.__init__(self, kk)
        self.realkk = kk
    def get_kk(self):
        return self.realkk

k = K(88) # 使父类中被覆盖的方法再次在子类中实现
print(k.get_kk())

class K2(C):
    def __init__(self, kk):
        super(K2, self).__init__(kk) #这样不需要在里面提及父类的名字
        self.realkk = kk
    def get_kk(self):
        return self.realkk

k2 = K2(90)
print(k2.get_kk())


class F:
    def __init__(self, name):
        self.hhname = name
        print(self.hhname + "V me 50")

class KFC(F,P): #继承属性和方法是按照顺序先后继承的，如果之前的有了，就不继承后面同样的
    pass

kfc = KFC("Chicken")
print(kfc.name, kfc.hhname)

#私有化：即在准备私有化的属性名字前面加上双下划线
class H:
    def __pp(self): #这样的属性不能在类之外调用
        print("which language?")
    def PP(self):
        self.__pp()
    __name = "__name"
    
    @property
    def pp(self):
        return self.__name

h = H()
h.PP()
print(h.pp) #使用@property装饰器来调用私有属性

print(isinstance(h, KFC)) #判断一个对象是否是一个类的实例
print(isinstance(h,H))