#12.Write a Python program to get a string from a given string where all occurrences of its first
#char have been changed to '$', except the first char itself.
#Sample String : 'restart' Expected Result : 'resta$t
a = 'madammadammadam'
b = a[0]
c = b
for i in range(1,len(a)):
    if b == a[i] :
        c += '$'
    else:
        c += a[i]
print(c)
        
#13.Write a Python program to add 'ing' at the end of a given string (length should be at least 3).
#If the given string already ends with 'ing' then add 'ly' instead. If the string length of the
#given string is less than 3, leave it unchanged.
a = 'intrest'
b = a
if len(a)>= 3 :
    if a[-3:] == 'ing' :
        b += 'ly'
    else :
        b += 'ing'
    print(b)
    
else:
    print(b)

#14.Write a Python program to remove the characters which have odd index values of a given string.
a = 'Being ignored is better than alone'
b = ''
for i in range(len(a)):
    if i%2 != 0 :
        b += ''
    else :
        b += a[i]
print(b)


#15.Write a Python script that takes input from the user and displays that input back in upper and lower cases.
#Sample Output: What's your favourite language? 
#english My favourite language is ENGLISH
#My favourite language is english

a = 'Mathamatics'
print('My favourite languague is ' , a.upper())
print('My favourite languague is ',a.lower())


#16.Write a Python function to reverse a string if it's length is a multiple of 4.


def reverse(str1):
    if len(str1)%4 == 0 :
        print(str1[::-1])
    else:
        print(str1)
str1 = 'srinivas'
reverse(str1)



#17.Write a Python program to count and display the vowels of a given text.
a = 'good people come from good areas'
count =  0
for i in a :
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U' :
        count += 1
        print(i,end = ',')

print('')
print(count)
    
#18.Write a Python program to lowercase first n characters in a string.
a = 'Good People Come From Good Areas'
n = 15
b = ''
for i in range(len(a)):
    if n>=i:
        b += a[i].lower()
    else:
        b += a[i]
print(b)

#19.Write a Python program to reverse words in a string.
#20.Write a Python program to count occurrences of a substring in a string.
        

        
    
























    
        
