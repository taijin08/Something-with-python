f = open("filetest01.txt") #打开一个txt文件，赋予一个对象，默认为只读的方式，即“r”
print(type(f))
print(dir(f)) #方法中有__iter__意味着是可以迭代的对象类型

for line in f:
    print(line) #现在的指针已经到了文件的末尾

nf = open("filetest02.txt", "w+") # w 意味着可以写入信息，如果文件存在则将覆写之前的内容
                                  # w+ 可以消除文件内容然后以读写方式打开文件
long = nf.write("This is a new file")
print(long)
nf.close()

nf = open("filetest02.txt", "a+") #a+ 即追加模式，文件指针移到最后
long = nf.write("\n Aha I like programming.") #返回文件指针所在的位置
print(long) 
nf.close()

nf = open("filetest02.txt", "r+") #r+ 即读写模式
l1 = nf.read()
print(l1)
nf.close()

with open("mdfile_01.md","w+") as mdf: #使用with语句，便不需要close()来保存
    mdf.write("I am a Pythoner.")
with open("mdfile_01.md") as mdf:
    print(mdf.read())

import os
file_stat = os.stat("mdfile_01.md")
print(file_stat) #显示这个文件的属性

import time
print(time.localtime(file_stat.st_ctime))

kk = open("mdfile_01.md")
print(kk.read(5)) #从指针所在位置向后读size个数据，如果size为负数或者none则读到文件末尾
print(kk.read()) #这些读到的数据返回为一整个字符串
kk.close()

kk2 = open("filetest01.txt")
while kk2.readline():
    print(kk2.readline())
kk2.close()

with open("filetest02.txt") as txf:
    print(txf.readlines())

import fileinput
mdf2 = fileinput.input("mdfile_02.md") #使用fileinput读取很大的文件
for line in mdf2:
    print(line)
print(dir(fileinput))

mdf2 = open("mdfile_02.md", "rb") #用rb模式才能使用seek的whence参数，不是b模式的仅支持从文件头偏移
print(mdf2.readline(), mdf2.tell())
mdf2.seek(5,1) #seek(offset, whence)调整指针位置 whence默认为0表示从文件开头计算偏移量，1为从当前位置，2为从文件末尾
print(mdf2.readline(), mdf2.tell())

#迭代
lst = "www.sjtu.edu.cn".split(".")
lst_iter = iter(lst) #返回一个迭代器对象
flag = True
while flag:
    kk = lst_iter.__next__()
    print(kk)
    if not kk:
        break

#用for来实现迭代，就是自动调用__next__()