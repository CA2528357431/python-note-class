# None空白

class solider:
    def __init__(self,a=None):
        self.gun=a


a=solider()
print(a.gun)
if(a.gun==None):
    print("no gun")