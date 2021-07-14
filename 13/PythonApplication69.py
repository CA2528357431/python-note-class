# 多继承

class A:
    def a(self):
        print("a")
    def c(self):
        print("use A")
class B:
    def b(self):
        print("b")
    def c(self):
        print("use B")

        
class C(B,A):
    pass


rtx=C()
rtx.a()
rtx.b()
rtx.c()

#多继承中多个上级有相同函数，则调用前面的上级函数，如（B,A)中调用了B.c
#如有重名，应避免用多继承
