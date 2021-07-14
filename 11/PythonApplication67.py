#  rewrite

class animal:
    def eat(self):
        print("eat")
    
    def drink(self):
        print("drink")
class cat(animal):
    def miao(self):
        print("miao")
    def eat(self):
        print("no")
class tom(cat):
    def joke(self):
        print("joke")


a=tom()
a.eat()
a.miao()

b=cat()
b.eat()

#rewrite会覆盖父类中的函数并传给后代
