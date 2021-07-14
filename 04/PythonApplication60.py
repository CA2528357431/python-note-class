#  类 删除、析构

class stu():

    def __init__(self,a=0):
        self.point=a
    def __del__(self):
        print ("die")

a=stu()
print(a.point)
del a
