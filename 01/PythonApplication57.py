# 类--方法


# 利用self调用/cls属性
#记得self!!!记得self!!!记得self!!!记得self!!!
#记得cls!!!记得cls!!!记得cls!!!记得cls!!!
class stu:
    time=0

    def study(self,a):
        self.point=self.point+0.1*a
    def play(self,a):
        self.point=self.point-0.1*a
    
        
    @classmethod #别忘了这个，不然报错
    def mission(cls):
        print("xue %d"%stu.time)
a=stu()
a.point=95
a.play(50)
a.study(100)
print(a.point)
stu.mission()


# 类方法用类名调用,实例方法用对象名调用
