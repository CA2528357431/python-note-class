#  类 属性---赋值与缺省

class stu():

    def __init__(self,a,b=0):
        print("create stu")
        self.point=b
        self.name=a

   
        
a=stu("xm",100)
print(a.name," ",a.point)

b=stu("xm")
print(b.name," ",b.point)
