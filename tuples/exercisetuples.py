#1. Write a Python program to create a tuple.
t = tuple()
for i in range(1,11):
    t += (i,)
print(t)

#2. Write a Python program to create a tuple with different data types.
t = tuple()
t1 = 'srinu','dinesh'
t1 = tuple(t1)
t2 = ([2,3,4,5],)
for i in range(1,11):
    t += (i,)

print(t+t1+t2)

#3. Write a Python program to create a tuple with numbers and print tuple.
t = tuple()
for i in range(1,11):
    t += (i,)
print(t)

#4. Write a Python program to add an item in a tuple.
t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
t = list(t)
t.append(11)
t = tuple(t)
print(t)

#5. Write a Python program to convert a tuple to a string.
t = ('s','r','i','n','u')
s = ''.join(t)
print(s)

t1 = ('s','w','a','m','i')
s = ''.join(t1)
print(s)

#6. Write a Python program to get the 4th element and 4th element from last of a tuple.

t = (1, 2, 3, 'srinu', 5, 6, 7, 8, 9, 10)
m = tuple()
for i in range(1,len(t)):
    if i == 4 or i == len(t)-3:
        m += (t[i-1],)
print(m)

print(t[3])
print(t[-4])
#7. Write a Python program to find the repeated items of a tuple. 
#Example: tuplex = 2, 4, 5, 6, 2, 3, 4, 4, 7 
#Output: 4 is 3 times


t = (2, 4, 5, 6, 2, 3, 4,0,0,0,0,0,0,0,0,0,0, 4, 7)
print('you are searching in this tuple : ', t)
item = 0
times = 0
for i in range(len(t)):
    if t.count(t[i])>item:
        item = i
        times = t.count(i)
print(times,'is',item,'times')
        



#8. Write a Python program to check whether an element exists within a tuple


t = ('s','r','i','n','u')
check = 'o'
if check in t:
    print('it exist')
else:
    print('it not exist')




#9. Write a Python program to remove an item from a tuple.

t = ('s','r','i','n','u')
t = list(t)
t.remove('u')
t = tuple(t)
print(t)


#10. Write a Python program to slice a tuple.

t = ('s','r','i','n','u')
print(t[1:3])


#11. Write a Python program to find the index of an item of a tuple.

t = ('s','r','i','n','u')
print(t.index('r'))

#12. Write a Python program to find the length of a tuple.
#13. Write a Python program to reverse a tuple.
#14. Write a program to swap two values using tuple assignment

t = ('s','r','i','n','u')
print(len(t))
print(t[::-1])
t1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

t,t1 = t1,t

print('t is ',t)
print('t1 is ', t1)


#15. Write a program that has a nested tuple to store topper details. Edit the details and reprint the details.

t = (('srinu',98),('shashi',97),('dinesh',95))

u = tuple()
a,b = t[0]
c,d = t[1]
e,f = t[2]
us = 99
ush = 99
ud = 99
for i in t:
    u += ((a,us),(c,ush),(e,ud))
    break
print(u)
    


#16. Write a program that has a list of numbers(both positive as well as negative). Make a new tuple that 
#has only positive values from this list.

        

n = [1,2,3,5,4,6,7,8,9,-1,-3,-4,-6,-7,-7,-8]
m = list()
for i in n :
    if i>0:
        m.append(i)
m = tuple(m)
print(m)

        





















































































    
