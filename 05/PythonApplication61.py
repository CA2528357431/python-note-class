#  类 属性---str

class stu():

    def __init__(self,a,b):
        self.point=b
        self.name=a
        self.n="free"
    def __str__(self):
        return "%s,FOR HK"%self.n    
    # 使a又代表了 str

   
        
a=stu("xm",100)
print(a)

