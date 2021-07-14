# 继承

class animal:
    def __init__(self):
        self.__go=10
    def eat(self):
        print("eat")
    def drink(self):
        print("drink")
    def show1(self):
        print(self.__go)
class cat(animal):
    def miao(self):
        print("miao")
class tom(cat):
    def joke(self):
        print("joke")
    def show2(self):
        print(self.__go)


a=tom()
a.eat()
a.miao()
a.joke()

a.show1()
a.show2()

#继承可传递
#子类无法通过自己的方法访问上级的私有,但用上级自带的方法访问可以