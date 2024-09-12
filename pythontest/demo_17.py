import sys
import pprint
pprint.pprint(sys.path)
#在Python 中，所有可引用的模块都被加入到了sys.path 里面。

sys.path.append("D:\PangProjects\pythontest\pp1.py")
#将自己编辑的模块纳入sys路径，以便可以import
import pp1
from pp1 import * #导入此模块所有有权限访问的内容

print(public_variable) #公有的才有权限访问
public_teacher()
print(pp1._private_variable) #私有对象可以这样访问


#一个包由多个模块组成，即多个.py 文件,在该目录中放一个__init__.py 文件。
# __init__.py 是一个空文件，将它放在某个目录中，就可以将该目录中的其他.py文件作为模块被引用。
#导入一个包中的模块：
import package1.pp2 as p
print(p.lang())

print(dir(pp1))
#可以通过help浏览模块的文档和源码等


