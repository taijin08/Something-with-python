while 1:
    print("this is a division program.")
    c = input("input 'c' continue, otherwise logout:")
    if c == 'c':
        a = input("first number:")
        b = input("second number:")
        try:
            print(float(a)/float(b))
            print("*************************")
        except ZeroDivisionError:
            print("The second number can't be zero!")
            print()
        except ValueError as e:
            print(e) #使用默认的异常提示
            print("*************************")
    else:
        break

#如果没有异常发生，except 子句在try 语句执行之后被忽略；
# 如果try 子句中有异常，则该部分的其他语句被忽略，直接跳到except 部分，
# 执行其后面指定的异常类型及其子句。
#如果except后无异常参数，不论try部分发生什么异常，都会执行except
# try 后面可以接多个except 对应多种异常类型

while 1:
    try:
        x = input("the first number:")
        y = input("the second number:")
        r = float(x)/float(y)
        print(r)
    except Exception as e:
        print(e)
        print("try again.")
    else:
        break
#如果执行了try，则except 被忽略，但是else被执行。
#这样一来可以一直输入直到正确为止

try:
    x = input("the first number:")
    y = input("the second number:")
    r = float(x)/float(y)
    print(r)
except Exception as e:
    print(e)
else:
    print("else")
finally:
    print("finally")
    del x, y, r

assert 1==1 #断言：如果后面的不为真则抛出异常
assert 1==0

