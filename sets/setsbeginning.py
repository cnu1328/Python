#set
s = {1,2,3,4,5,6,7,8,9,0}
print(type(s))
s = set()
print(type(s))
s = [1,3,5,8,0]
print(set(s))
s = {1,2,3,4,5,5,6,7,8,9,0}
print(s)
#s[3]= 10
print(s)
s.add(10)
print(s)
s.update((10,20,30))
print(s)


#traversing a set
s = set('Hello everyone! Good morning')
print(s)
for i in s:
    print(set(i),end = ' ')

print('')

#set operations
s = {1,2,3,4,5,5,6,7,8,9}
s1=s
if 1 in s:
    print('present')
else:
    print('not present')

print(1 in s)
print(2 not in s)

print(s == s1)
print(s !=s1)


print(len(s))

print(max(s))
print(min(s))
print(sum(s))
print(all(s))

s = {1,2,10,4,5,5,6,7,8,9,0}

print(any(s))


print(set(sorted(s)))

s.add('good')
print(s)
s.remove('good')
print(s)

print("set methods")
s.discard('good')
print(s)

s.pop()
print(s)

s.clear()
print(s)

s = {1,2,10,4,5,5,6,7,8,9,0}
s1 = {'good','food','stood'}
s.update(s1)
print(s)

s.copy()
print(s)

s = set()
for i in range(1,10):
    s.add(i)
print('s',s)
m = set()
for i in range(5,15):
    m.add(i)
print('m',m)
    
print(s.issubset(m))


print(s.issuperset(m))


print(s.union(m))
print(s|m)

print(s.intersection(m))
print(s&m)

s.intersection_update(m)

print(s)



s = set()
for i in range(1,10):
    s.add(i)

print('s',s)
m = set()
for i in range(5,15):
    m.add(i)
print('m',m)

print(s.difference(m))
print(s-m)

s.difference_update(m)
print(s)
s = set()
for i in range(1,10):
    s.add(i)
m = set()
for i in range(5,15):
    m.add(i)

print(s.symmetric_difference(m))
print(s^m)



#1. Write a program to perform union, intersection, difference and symmetric difference operation on two 
#sets. Take one set as prime numbers and second set as odd numbers. 

s = {2,3,5,7,11,13,17}
m = {1,3,5,7,9,11,13,15}

print(s|m)
print(s&m)


print(s-m)

print(s^m)



#2. Write a program that has a list of countries. Create a set of the countries and print the names of the 
#countries in sorted order.

c = {'india','china','newzeeland','britan','srilanka'}

print(set(sorted(c)))

#3. Write a program that perform update(), pop(), remove(), add() and clear() operations on two sets.

s = {2,3,5,7,11,13,17}
m = {1,3,5,7,9,11,13,15}

s.update(m)
print(s)
print(m)

s = {2,3,5,7,11,13,17}

s.pop()
print(s)

s.remove(13)

print(s)


s,m.clear()
print(s,'\n', m)













