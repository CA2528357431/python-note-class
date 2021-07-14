# 私有方法

class woman:
    def __init__(self,a,b):
        self.name=a
        self.age=b
    def show(self):
        print(self.name,"is",self.age)
    def __show1(self):
        print(self.name,"is",self.age)

a=woman("xm",18)

a.show()
a.__show1()

#__也可让函数私有
