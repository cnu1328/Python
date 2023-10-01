t = (2,3,4,5,6,7,8,9,)
print(t)
print(type(t))
t1 = ('srinu',2,3,5,('shashi','dinesh'),2,3,4,5)
print(t1)
print(t1[4][0])

#t[0] = 'srinivas'

t1,t = t,t1
print(t)
print(t1)


#traversing tuple
for i in t:
    print(i)



#tuple operations

print(t+t1)
print(t1*4)
print('srinu' in t1)
print('srinu' not in t)

print(t[:2])

#tuple functions

t = (2,3,4,5,6,7,8,9)
print(len(t))
print(max(t))
print(min(t))
print(sum(t))

to = (1,1,1,1)
print(any(to))
print(all(to))

t = list(t)
print(t)
t = tuple(t)
print(t)

print(tuple('srinu is a good boy'))



t1 = ('srinu','shashi','dinesh')
print(sorted(t1))

reversed(t1)
print(t1)

#tuple methods

t1 = ('srinu',2,3,5,('shashi','dinesh'),2,3,4,5)
print(t1.count(3))
print(t1.index(5))


t = (9,)
print(t)
print(type(t))


t = [2,3,4,5]
del(t[2])
print(t)

t = tuple(t)
#del(t[1])

#del(t)
print(t)




T1=(10,20,30)
T2=(100,200,300) 
T3=(10,20,30)
#print(cmp(T1,T2))



























































































