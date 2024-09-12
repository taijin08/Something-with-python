def lang():
    return "python"

#同一个模块，既可以作为程序执行，也可以作为模块导入
#如果要作为程序执行，则__name__ == "__main__"；如果要作为模块引入，则pp2.__name__== "pp2"，即属性__name__的值是模块名称。

if __name__ == "__main__":
    print(lang())
#程序执行这一部分。
