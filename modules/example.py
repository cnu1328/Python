#module
def add(a,b):
    result = a+b
    return result

def prime(n):
    count = 0
    for i in range(1,n+1):
        if n%i ==0:
            count +=1
    if count ==2:
        com = 'Your entered number is prime'
        return com
    else:
        com = 'Your entered number is not a prime'
        return com

def summation(x,y):
    result = x+y
    return result
def multiplication(x,y):
    result = x*y
    return result
def devide(x,y):
    result = x/y
    return result

def factorial(num):
    if num == 1:
        return 1
    else:
        return (num*factorial(num-1))



def fab_recurse(n):
    if n <=1 :
        return n
    else:
        return fab_recurse(n-1)+fab_recurse(n-2)

#16.Write a Python function to reverse a string if it's length is a multiple of 4.


def reverse(str1):
    if len(str1)%4 == 0 :
        return str1[::-1]
    else:
        return str1


def string(str):
    b = ''
    for i in str:
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U':
            b += ''
        else:
            b += i
    return b









































        
        


