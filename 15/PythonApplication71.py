# 单例

#单例 指 解决特定问题的固定方法
#形式为 某类下定义唯一对象
class x:
    instance=None
    start=False
    def __new__(self,r):
        if x.instance==None:
            x.instance=super().__new__(self)
        return x.instance
    def __init__(self,r):
        if x.start==True:
            x.start=False
        else:
            pass

a=x(1)
b=x(1)
c=x(1)
print(a is b)
print(a is c)

#永远只留一个地址————该类只有一个对象
#初始化也只一次
#new和init的参数必须保持一致