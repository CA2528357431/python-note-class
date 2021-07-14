# new方法

class player1:
    def  __init__(self):
        print("here we go")
    
    def __new__(self):
        print("space")

QQ=player1()
print(QQ)
#new用于分配空间.重写new使得class的对象无法创建
#new应当return地址

class player2:
    def  __init__(self):
        print("here we go")
    
    def __new__(self):
        print("space")
        x=super().__new__(self)#获得应有的地址
        return x

PP=player2()
print(PP)
#先分配空间，后创建