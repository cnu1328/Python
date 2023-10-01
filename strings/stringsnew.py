#traversing a string
a = 'srinivas'
for i in a :
    print(i,end = ',')
print('')

i = 0
while i<len(a):
    print(a[i],end=',')
    i += 1
print('')

#strings are immutable
#a[3]='e'
#print(a)

#concatanation
a = 'Hello!'
c = ','
b = 'Srinu'
print(a+b)
print('H' in a )
print('r' not in a)
print(a[::-1])

#slicing a string stride
d = 'Srinivas'
print(d[:7])

#strings using relation operators
e ='Srinu'
print(b==e)
print(b!=e)
print(a<b)
print(a>d)
print(a<=c)
print(b>=d)

#Escape scequence
print('good\nnice')
print('good\tnice')
print('good\\nice')
print('good\'nice')
print('good\"nice')

#raw string
print('....................................................')
print(r'good\nnice')
print(R'good\'nice')
#string formatting operator

print(f"my name is %s and my age is %d and my weight is %f "%('srinu',20,62.452))
print("my name is {} and my age is {} and my weight is {} ".format('srinu',20,62.452))

print('srinu you are {}person bcoz you have {} and courage in {}'.format('lucky',50,5.5))


#practice
print('my name is %s and my age is %d'%('srinu',40))
print('my name is {} and my age is {}'.format('srinu',40))

#string methods and functions
#len()
a = 'srinivas introduced as srinu'
print(len(a))
print(a.capitalize())
print('...........find...........')
print(a.find('srinu'))
print(a.rfind('v'))
print(a.index('as'))
print(a.rindex('u'))

b = 'srinu123'
c = 'srinu'
print(b.isalnum())
print(c.isalpha())
d = '123456'
print(d.isdigit())
e = 'srinu'
print(e.islower())
print(e.isupper())
print(e.lower())
print(e.upper())

#strip
f = '    srinu    '
print(f.strip())
print(f.lstrip())
print(f.rstrip())
g,h,i = ' ','\t','\n'

print(g.isspace())
print(h.isspace())
print(i.isspace())

print(a.istitle())

print(a.replace('srinivas','srinu'))
print(a.replace('srinu','nani'))

print(c.join(c))

print(a.swapcase())

print(a.split())

print(a.partition('as'))
j = 13.450054
print(round(j))

print(a.count(c,0,len(a)))

print(a.encode())

#string  constants
import string
print(string.ascii_uppercase)
print(string.ascii_lowercase)
print(string.digits)
print(string.ascii_letters)
print(string.hexdigits)
print(string.octdigits)
print(string.printable)
print(string.whitespace)
print(string.punctuation)

















































