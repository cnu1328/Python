l = [1,2,3,4,5]
print(l)
print(l[0])
my_list = [2,'srinu',4]
print(my_list)
print(my_list[1])
print(my_list[1][1])
nested_list = [3,5,3,2,[5,3],4]
print(nested_list)



l = ['srinu','shashi','dinesh','swami']
l[0] = 'srinivas' #lists are mutable
for i in l:
    print(i)
for i in range(len(l)):
    print(l[i])
    
i = 0 
while i<len(l):
    print(l[i])
    i += 1

    
#list operations
l = [1,2,3,4,5]
m = [1,2,3,5,6]
print(l+m)

print(l*3)
print(5 in l)
print(6 not in l)

print(l[::-1])

print(len(l))
print(max(l))
print(min(l))

print(sum(l))
print("aaaaaaaaaaaallllllllllllllllllaaaaaaaaaaa")
l = [1,2,0,4,5]
l1 = [0,0,0,0,0]

print(all(l)) #false

print(any(l1)) #false

a = ['srinu  you do your best']
print(list(a))

a = l[::-1]
print(sorted(a))

#list methods
#append
l.append(3)
print(l)

a = ['srinu  you do your best']

a.append('for satisfaction')
print(a)

print(l1.count(0))

l = [0,1,2,3,4,5,6]
print(l.index(0))
print(len(l))
l.insert(4,(7,8,9,10))
print(l)

l = [0,1,2,3,4,5,3,6]
l.pop()
print(l)
l.remove(3)
print(l)



l = [0,1,2,3,4,5,3,6]
l.sort()
l.reverse()

print(l)

l1 = [7,8,9,10]

l.reverse()

l.extend(l1)
print(l)
print(l1)
l.remove(3)
print(l)


'''#How to create a matrix
r = 3
c = 2
m = []
for i in range(0,r):
    m.append([])
    for j in range(0,c):
        v = int(input('Enter your matrix vlaues : '))
        m[i].append(v)
print('values of first matrix : ' )
for k in m:
    print(k)
'''






#matrix addition
'''r1 = 2
c1 = 3
r2 = 2
c2 = 3
m1 = []
m2 = []
res = []
if r1 != r2 or c1 != c2 :
    print('For matrix addition rows and colums should be equal')

else:
    for i in range(0,r1):
        m1.append([])
        for j in range(0,c1):
            v = int(input('Enter first matrix vlaues : '))
            m1[i].append(v)
    print('Your first matrix is : ' )
    for k in m1 :
        print(k)

    for i in range(0,r2):
        m2.append([])
        for j in range(0,c2):
            v = int(input('Enter second matrix values : '))
            m2[i].append(v)
        print('Your second matrix is  : ')
    for k in m2 :
        print(k)

    for i in range(0,r2):
        res.append([])
        for j in range(0,c2):
            res[i].append(0)
    #logic
    for i in range(0,r2):
        for j in range(0,c2):
            res[i][j] =m1[i][j] + m2[i][j]
    print('Your result matrix is : ')
    for k in res :
        print(k)'''
#matrix multiplication
r1 = 2
c1 = 3
r2 = 3
c2 = 2
m1 = []
m2 = []
res = []
if r2 != c1 :
    print('for matrix multiplication coloum one should equal to row two')
else:
    for i in range(0,r1):
        m1.append([])
        for j in range(0,c1):
            v = int(input('Enter first matrix values : '))
            m1[i].append(v)
    print('Your first matrix is : ')
    for k in m1:
        print(k)

    for i in range(0,r2):
        m2.append([])
        for j in range(0,c2):
            v = int(input('Enter second matrix values : '))
            m2[i].append(v)
    print('Your second matrix values are : ')
    for k in m2:
        print(k)

    for i in range(0,r1):
        res.append([])
        for j in range(0,c2):
            res[i].append(0)

    print(len(m1))    #2
    print(len(m2[0])) #2 
    print(len(m2))    #3
    for i in range(len(m1)):
        for j in range(len(m2[0])):
            for k in range(len(m2)):
                res[i][j] += m1[i][k] + m2[k][j]
    for k in res:
        print(k)
    
                    
    

    












    














































