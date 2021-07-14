# 私有属性

class woman:
    def __init__(self,a,b):
        self.name=a
        self.age=b
    def show(self):
        print(self.name,"is",self.age)

a=woman("xm",18)
print(a.age)
a.show()


print()


class woman1:
    def __init__(self,a,b):
        self.name=a
        self.__age=b
    def show(self):
        print(self.name,"is",self.__age)

a=woman1("xm",18)
a.show()
print(a.__age)

#   __ 可使属性变为私有，不可在class外访问
