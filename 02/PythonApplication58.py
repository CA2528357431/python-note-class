#  类 属性---安全添加

class stu():

    count=0



    def __init__(self):
        print("create stu")
        self.point=95
        cls.count=cls.count+1
        #创造class时调用
        
        
    def study(self,a):
        self.point=self.point+0.1*a
    def play(self,a):
        self.point=self.point-0.1*a
   
        
a=stu()
b=stu()
a.play(50)
a.study(100)
print(a.point)
print(stu.count)

# 类属性 ，对一个类整体其作用，相当于全局变量。本例中 count 即为类属性，每创建一次就+1。用类名调用
# 实例属性 ，对单个对象作用，在对象内作用。本例中 point 即为类属性,用对象名调用
 