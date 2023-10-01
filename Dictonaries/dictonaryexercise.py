#1. Write a Python script to add key to a dictionary?
a = {1:'good',2:'ok',3:'average'}
b = {4:'below average'}
a.update(b)
print(a)

#2. Write a Python script to concatenate following dictionaries to create a new one?
dic1={1:10, 2:20} 
dic2={3:30, 4:40} 
dic3={5:50,6:60}

dic4 = dict()

for i in (dic1,dic2,dic3):
    dic4.update(i)
print(dic4)



#3. Write a Python script to check if a given key already exists in a dictionary?

d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
key = 8
if key in d:
    print('it already exist')
else:
    print('it not exist')

#4. Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both 
#included) and the values are square of keys?

dic = dict()
for i in range(1,16):
    d = {i : i*i}
    dic.update(d)
print(dic)


#5. Write a Python program to remove duplicates from Dictionary.
student_data = {'id1':{'name': ['Sara'], 'class': ['V'], 'subject_integration': ['english, math, science']},'id2': {'name': ['David'], 'class': ['V'], 
 'subject_integration': ['english, math, science']},'id3': {'name': ['Sara'], 'class': ['V'], 'subject_integration': ['english, math, science']},'id4': 
 {'name': ['Surya'], 'class': ['V'], 'subject_integration': ['english, math, science']}}


print(set(student_data))



#6. Write a Python program to multiply all the items in a dictionary
d = {'data1':100,'data2':54,'data3':247}
res = 1
for i in d:
    res = res*d[i]
    print(res)

#7. Write a Python program to iterate over dictionaries using for loops

d = {'Red': 1, 'Green': 2, 'Blue': 3}
for i in d:
    print(i,'corresponds to ' ,d[i])
    
#8. Write a Python program to sort a dictionary by key.


d = {'data4':100,'data2':54,'data3':247}
print(sorted(d.items()))


#9. Write a Python program to create a dictionary from a string.
s = 'rguktbasar'
d = dict()
for i in s:
    c = s.count(i)
    di = {i : c}
    d.update(di)
print(d)
    
#10. Write a program that has dictionary of names of students and a list of their marks in 4 subjects. 
#Create another dictionary from this dictionary that has name of the students and their total marks. Find 
#out the topper and his/her scorev

d 


































































