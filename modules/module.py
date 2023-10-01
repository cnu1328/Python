#module
'''def add(a,b):
    result = a+b
    return result'''
import example
print(example.add(10,20))

import example
n = 11#int(input('Enter a number : ' ))
print(example.prime(n))

from math import *
print(pi)

from example import summation
x = 10
y = 20
print(summation(x,y))
from example import multiplication
print(multiplication(x,y))

from example import devide
x = 100
y = 10
print(example.devide(x,y))


from example import *
x = 50
y = 5
print(summation(x,y))
print(multiplication(x,y))
print(devide(x,y))

#The dir() built-infunction


import math
print(dir())
x = 25
y = -56
z = 5
print(math.ceil(x))
print(copysign(x,y))
print(fabs(x))

print(factorial(5))

print(floor(x))

print(fmod(13,4))

print(frexp(x))
s = 10,20,30,40,50,60,70,80,90
print(fsum(s))

print(isfinite(x))

print(isinf(x))

print(isnan(x))

print(ldexp(x,z))

print(modf(x))

print(modf(9.98789))

print(trunc(x))

print(exp(x))

print(expm1(x))

print(log(1))

print(log1p(x))

print(log2(x))

print(log10(x))

print(pow(x,z))

print(sqrt(x))

print(acos(0))

print(asin(1))

print(atan(x))


#random module
import random

print('random')
print('randon directory')
print(dir())
print(random.random())

print(random.randint(1000,2000))

print(random.uniform(z,x))

print(random.randrange(100,1000,3))

l = ['Heads','Tails']
print(random.choice(l))

#composition
print(math.exp(math.log(1)))

degree = 270
print(math.sin(math.tan(degree)))


#recursive functions

from example import factorial
num = 5
print('factorial of your number is ',factorial(num))


#fibonacci series in recursive function
'''from example import fab_recurse
n = 10
print('your fabonacci series is ', fab_recurse(n))'''

def fab_recurse(n):
    if n <= 0:
        print('please enter positive number ')
    else:
        print('your fabonacci series is ')
        for i in range(n):
            print(fab_recurse(i),end = ',')
n = 1
fab_recurse(n)
print('')

from example import reverse
str1 = 'srinivas'
print(example.reverse(str1))



from example import string

str = 'srinu'
print(string(str))

















































































































      





































