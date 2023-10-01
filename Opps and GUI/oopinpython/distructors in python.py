class point:

    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
        print('constructed')
    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name,' is distructed')
pt1 = point()
pt2 = pt1
pt3 = pt1

print(id(pt1),'\n',id(pt2),'\n',id(pt3))
print(id(pt1),id(pt2),id(pt3),end = '\n')

del pt1,pt2,pt3


        
