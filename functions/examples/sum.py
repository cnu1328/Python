def sum(x,y):
    s = x+y
    print('sum is ' ,s )
sum(10,20)
sum(50,60)


#write first and last name of a person using function
def my_function(fname,lname):
    print(fname+' ' +lname)
my_function('srinu','darpally')
my_function('shashi','bandi')


#buildinfunctions
print(max(10,20,30,40,50,60,40,0,90))
print(min(10,20,30,40,50,60,40,0,90))
a=10,20,30,40,50,60,40,0,90
print(len(a))


def message():
    print('Iam working on it')
    print('shall let you know once finish if off')
message()


#docstring
def srinu(name):
    '''hello! Srinu'''
    print(name)
srinu('srinu')
print(srinu.__doc__)


def greet(name):
        print('hello '+name+' good morning')
greet('ram')

def greet(name):
    '''This is your attitude'''
    print('you are beautiful',name)
greet('Ram')
print(greet.__doc__)


#return
def changeme(x):
    return x
x= 5
print(changeme(x))

#void
def check(num):
    if num%2==0:
        print("true")
    else:
        print('False')
r=check(5)
print(r)

#types of argumests
#required arguments
'''def message():
    print('hello')
message('hi')'''

def message(s):
    print(s)
message('hello')

#keyboard arguments

def display(name,x,y):
    print('name is ',name,'\nage is ',x,'\nweight is ',y)
display('srinu',65,5)
display(x=18,name='srinu',y=75)

def display(name,course ='B.TECH'):
    print('your name',name,' and your course ',course)
display('Ram')
display('Srinu','B.COM')


#variable length arguments
def display(*name):
    for i in name:
        print('HELLO',i)
display('srinu','shashi', 'swami','dinesh')


#scope of variables
#Global variables
def test():
    global x
    x = 10
    print('inside ' , x)
test()
print('outside : ', x)

def test () :
    print('inside : ' , x)
print('outside : ',x )
test()

#example
def srinu(*name):
    ''' This is to do some names to say hello'''
    for i in name:
        print('HELLO', i)
print(srinu.__doc__)
srinu('srinu','shashi','dinesh')

# This program has two functions. First we define the main function.
# Next we define the message function.
def main():
    print('I have message for you ')
    message()
    print('Goodbye ')
def message():
    print('im on work ')
    print('meet you next time thank you and ')
main()

#return
def change(x):
    return x
change(7)
print(change(7))

#1. Write a Python function to find the Min of three numbers.
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>")
def mina(x,y,z):
    if x<y:
        print(x,'is smaller')
    elif y<z :
        print(y,'is smaller ')
    else:
        print(z,'is smaller ')

mina(40,20,30)


def compare(x,y,z):
    print(min(x,y,z),'is smaller ')
compare(40,20,30)

#2. Write a Python function to find the Max of three numbers
def mina(x,y,z):
    if x>y:
        print(x,'is greater')
    elif y>z :
        print(y,'is greater ')
    else:
        print(z,'is greater ')

mina(10,20,30)


def compare(x,y,z):
    print(max(x,y,z),'is greater ')
compare(10,20,30)


#3. Write a Python function to calculate the factorial of a number (a non-negative integer). The function 
#accepts the number as an argument.

def fact(f):
    factorial = 1
    for i in range(1,f+1):
        factorial = factorial*i
    print(factorial)
f = int(input('Enter a number : ' ))
fact(f)
print("<<<<<<<<<<<<<<<<<<<")

#4. Write a Python function that accepts a string and calculate the number of upper case letters and lower
#case letters.

def lowercase(str):
    count = 0
    for i in str:
        if ord(i)>=97 and ord(i)<=122 :
            count += 1
    print('lower case letters are ' , count)

def uppercase(str):
    count = 0
    for i in str:
        
        if ord(i)>=65 and ord(i)<=91 :
            count += 1
    print('uppercase letters are ' , count)

str = input(' Enter a string ' )
lowercase(str)
uppercase(str)

str1 = "Good morning"
for i in str1:
    print('Hello : ',i)


#5. Write a Python function that takes a number as a parameter and check the number is prime or not.
def prime(p):
    count =0
    for i in range(1,p+1):
        if p%i==0:
            count += 1
    if count == 2 :
        print('prime ')
    else:
        print('not prime')

p = int(input('Enter a number to check prime or not : ' ))
prime(p)

#6. Write a Python function to check whether a number is perfect or not.

def perfect(n):
    for i in range(1,n):
        if n%i == 0:
            if i*i == n :
                print('Enterd number is a perfect')
                break
    else :
        print('Not a perfect')
n = int(input('Enter a number : ' ))
perfect(n)





















































































































    
