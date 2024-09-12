def  gcd(a,b): #最大公约数
    if not a > b:
        a, b = b, a
    while b != 0:
        remain = a % b
        a, b = b, remain
    return a

def lcm(a, b): #最小公倍数
    return (a * b) / gcd(a, b)

print(gcd(8,20))
print(lcm(8,20))

class Fraction:
    def __init__(self, number, denom=1): #前后双下划綫无需我们显式地调用
        self.number = number
        self.denom = denom
    
    def __str__(self):
        return str(self.number)+'/'+str(self.denom)
    #__str__()是一个特殊方法。实现这个方法的目的就是能够得到打印的内容。

    __repr__ = __str__
    #__repr__ = __str__的含义是在类被调用，即向变量提供__str__()里的内容。
    
    def __add__(self, other):
        lcm_num = lcm(self.denom, other.denom)
        number_sum = (lcm_num / self.denom * self.number) + (lcm_num / other.denom * other.number)
        return Fraction(number_sum, lcm_num)
    #__add__()，是实现相加的特殊方法。

f = Fraction(2,3)
print(f)
n = Fraction(1,2)
s = f + n
print(f, "+", n, "=", s)




