dic = {'srinu':5,'shashi':5}
dic1 = dict() #{}
dic2 = {}
print(dic2)
print(dic1)
print(dic)
print(type(dic))

#accessing elements in dict
dic = {'name':'srinu',1 : (1,2,3,5)}
print(dic['name'])
print(dic.get(1))


#traversing a dict

dic = {'srinu':5,'shashi':5}
for i in dic:
    print(i,':',dic[i])

    print(i,':',dic.get(i))
    



#dictionary functions

dic = {'srinu':5,'shashi':5}
print(len(dic))


#dictionary methods

dic = {'srinu':5,'shashi':5}
dic.clear()
print(dic)

dic = {'srinu':5,'shashi':5}
print(dic.get('srinu'))

#print(dic.has_key('srinu'))

print(dic.items())

print(dic.keys())

print(dic.values())

dic.pop('srinu')
print(dic)



dic = {'srinu':5,'shashi':5}

dic.popitem()
print(dic)


sub = {'tel','maths'}
m =dict.fromkeys(sub,78)
n = dict.fromkeys(sub,50)
print(n)
print(m)

dic = {'srinu':5,'shashi':5}
dic.update(m)
print(dic)





































































