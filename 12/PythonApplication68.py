#  扩展继承

class animal:
    def __init__(self):
        self.weight=100
        
    def eat(self):
        self.weight+=30
    
class cat(animal):
    def __init__(self):
        super().__init__()
        self.go=10
    
    def eat(self):
        super().eat()
        self.weight+=self.go

a=cat()
a.eat()
print(a.go)
print(a.weight)

#用super调用父类的原函数以对此函数完成扩充