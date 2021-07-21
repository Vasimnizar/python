class myfirst:
    def __init__(self,x,y):
        self.x=x
        self.y=y
obj1 =myfirst(10,20)
class mysecond(myfirst):
    pass
obj2=mysecond(40,50)
print(obj2.x)
print(obj2.y)
print(obj1.x)
print(obj1.y)
