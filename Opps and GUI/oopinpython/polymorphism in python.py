#function overriding
class parent():

    def myMethod(self):

        print('Calling parent Method')

class child(parent):

    def myMethod(self):

        print('Calling child Method')

c = child()
c.myMethod()

#other example

class animal():

    def __init__(self,name = ""):

        self.name = name

    def talk(self):

        pass

class cat(animal):
    def talk(self):

        print('cat')

class dog(animal):
    def talk(self):

        print('dog')
a = animal()
a.talk()

c = cat()
c.talk()

d = dog()
d.talk()



#operator overloading

import math

class circle :
    def __init__(self,radius):
        self.__radius = radius

    def getradius(self):
        return self.__radius

    def area(self):
        return math.pi*(self.__radius**2)

    def __add__(self,another_circle):
        return circle(self.__radius + another_circle.__radius)
    


c1 = circle(4)
print(c1.getradius())
        

print(c1.area())

c2 = circle(5)

c = c1 +c2

print(c.getradius())
print(c.area())



#other example

class vector :

    def __init__(self,a,b):

        self.a = a
        self.b = b

    def __str__(self):

        return 'vector (%d ,%d )'%(self.a,self.b)
    def __add__(self,other):
        return vector(self.a + other.a, self.b + other.b)


v1 = vector(19,20)
v2 = vector(10,20)
print(v1+v2)

class mul :

    def __init__(self,a,b):

        self.a = a
        self.b = b

    def __str__(self):

        return 'multiplication of two given numbers is (%d,%d)'%(self.a,self.b)
    def __mul__(self,other):

        return mul(self.a*other.a,self.b*other.b)
class subs:
    def __init__(self,a,b):

        self.a = a
        self.b = b
    def __str__(self):

        return 'substraction of two given numbers is (%d,%d)'%(self.a,self.b)

    def __sub__(self,other):

        return subs(self.a-other.a,self.b-other.b)

class mods :

    def __init__(self,a,b):

        self.a = a
        self.b = b
    def __str__(self):

        return 'Modulus of given values are {} and {} '.format(self.a,self.b)

    def __mod__(self,other):

        return mods(self.a%other.a,self.b%other.b)

class divi :

    def __init__(self,a,b):

        self.a = a
        self.b = b

    def __str__(self):

        return 'Division of given numbers is {} and {} '.format(round(self.a),round(self.b))
    def __truediv__(self,other):

        return divi(self.a/other.a,self.b/other.b)

class less:
    def __init__(self,a,b):

        self.a = a
        self.b = b
    def __str__(self):

        if self.a < self.b:
            return '{} is less than {} '.format(self.a,self.b)
        else:
            return '{} is less than {}'.format(self.b,self.a)

    def __lt__(self,other):

        return less(self.a<other.a,self.b<other.b)
            
class main:
    m1 = mul(10,20)
    m2 = mul(2,1)
    print(m1*m2)
    
    m1 = subs(10,20)
    m2 = subs(2,1)
    
    print(m1-m2)

    m1 = mods(10,20)
    m2 = mods(3,3)
    print(m1%m2)

    m1 = divi(10,20)
    m2 = divi(3,3)
    print(m1/m2)

    m1 = less(10,20)
    m2 = less(3,3)
    print(m1<m2)

if __name__ == '__main__' :

    main()


































































