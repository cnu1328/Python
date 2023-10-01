#1. Write a Python program to copy the string using for loop(using range and without
#using range function).


a = 'srinu'
b = ''
c =''
for i in range(len(a)):
    b += a[i]

print(b)

for i in a:
    c += i
print(c)

#2. Write a program to print the followingpattern.
'''A
   AB 
   ABC 
   ABCDE
   ABCDEF
'''
k = 65
row = 5
for i in range(0,row):
    for j in range(0,i+1):
        print(chr(k),end = '')
        k += 1
        if k>90:
            k = 65
        
    print('')
    k = 65

#3. Write a python that takes user’s name and PAN cardnumber as input.Validate the information using is X function 
#and print the details

def validate(name,pan):
    if name.isalpha() :
        print('Your name is valid')
    else:
        print('please check your name and re-enter')
        
    if pan[0:4].upper() and pan[5:9].isdigit() and pan[-1].isupper() :
        print('Your pan number is valid')
    else:
        print('Please check your pan No. again')
name ='sr' #input('Enter your valid name : ')
pan = 'a'#input('Enter your pan card No. : ')
validate(name,pan)

#4. Write a program that encrypts a message by adding a key value to every
#character. Hint: say, if key=3, then add 3 to every character

a = 'srinu'
key = 3
b = ''
for i in a:
    asci = ord(i)
    n = asci + key
    i = chr(n)
    b += i
print(b)

#5. Write a program to that uses split() to split multiline string.
a = 'I would like to introduce myself as DHARPALLY SRINIVAS'
print(a.split())



































    
