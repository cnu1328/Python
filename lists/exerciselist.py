#1. Create a list named wordList that contains the following words: "washington", "lee", "generals", 
#"arlington", "RGUKT" and perform the following operations.
# i) Print out the first element in wordList 
#ii) Print out the length of the list? 
#iii) Print out the last element in wordList?
#iv) Print out the index of the word "generals" in the list?
wordList = ['washington','lee','generals','arlington','RGUKT']
print(wordList[0])
print(len(wordList))
print(wordList[-1])
print(wordList.index('generals'))

#2. Write a program to that creates a list of numbers from 1-20 that are either divisible by 2 or 4.
l = list()
for i in range(1,21):
    if i%2==0 or i%4==0 :
        l.append(i)
print(l)


#3. Write a program to generate a list of squares from 1-10.
l = list()
for i in range(1,11):
    l.append(i**2)
print(l)

#4. Write a python program the defines a list of countries that are a member of BRICS. Check whether a 
#country is a member of BRICS or not.
brics = ['BANGLADESH','RUSSIA','INDIA','CHINA','SRILANKA']
check = 'INDIa'
a = check.upper()
if a in brics:
    print(a,' is a member of BRICS')
else:
    print(a,' is not a member of BRICS')


#5. Write a python program to create a list of numbers in the range 1 to 10.Then delete all the even 
#numbers from the list and print the final list.

l = list()
for i in range(1,11):
    l.append(i)
print(l)
for i in l :
    if i%2 == 0 :
        l.remove(i)

print(l)


print("############6#######")
#6. Write a program to print index at which a particular value exists. If the value exists at multiple locations 
#in the list, then print all the indices. Also, count the number of times that the value is repeated in the list.
l = [1,5,2,3,3,4,4,4,4,4,4,5,5,5,5]
value = 4
count = 0
print(l.index(value))
for i in range(len(l)):
    if value == l[i]:
        count += 1
        print('index value of ', value, ' is ', i)

print('The given value ',value, ' repeated ' ,count, 'times.')

#7. Write a program that creates a list of words by combining the words in two individual lists.
l = ['srinu',2,3,'shashi',4,5]
m = ['dinesh',6,7,'prasu',8,9]
l.extend(m)
print(l)



#8. Write a program that forms a list of first character of every word in the another list.
l = ['Srinu','Shashi','Dinesh','Swami','Prasu']
m = list()
for i in range(len(l)):
    m.append(l[i][0])
print(m)
    

#9. Write a python program to remove all duplicates from the a list.

l = [1,2,3,3,4,4,4,5,5,5,5]
print(set(l))
print(list(set(l)))



#10. Write a program that creates a list of 10 random integers. Then create two lists-odd list even list that 
#has all odd and even values in the list.
l = list()
el = list()
ol = list()
for i in range(1,11):
    l += [i]
for i in l:
    if i%2 == 0 :
        el += [i]
    else :
        ol += [i]
print('Your random list is : ' ,l)
print('Your even list is : ' , el)
print('Your odd list is : ' ,ol)































































    
    
