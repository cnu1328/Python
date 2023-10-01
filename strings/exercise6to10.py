#6. Write a program that accepts a string from user and redisplays the same string after
#removing vowels from it.
a = 'srinuaeiddousrinivas'
b = ''
for i in a:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U':
        b += ''
    else:
        b += i
print(b)

#7. Write a program that finds whether a given character is present in a string or not. In case it is 
#present it prints the index at which it is present. Do not use built-in find functions to search the
#character.
a = 'unique_soul'
print(a.index('q'))
b = 'qood'
b = b[0]
for i in range(1,len(a)) :
    if b == a[i]:
        print('Entered character is present')
        print('present character index value is ' , i)
        break
        
else:
    print('Entered character is not present')

#8. Write a program that finds a character in a string from ending of string to beginning that
#like rfind function
a = 'light is better than drak'
b = a[::-1]
print(b.find('g'))
c = 'g'
for i in range(0,len(b)):
    if c == b[i] :
        print('your character location is ' , i)


#9. Write a python program that count the occurrences of a character in a string and also
#counting from the specified location . Do not use string count function.
a = 'light is better than drak'
b = 'toch'
print(a.count('t'))
count = 0
b = b[0]
for i in a :
    if b == i :
        count  += 1
print('the entered character occurences in a string are ',count)
#for specified condition
B = 13
E = len(a)
counts = 0
for i in range(len(a)):
    if i>= B and i<= E :
        if b == a[i]:
            counts += 1
print(counts)


#10.Write a program to reverse of string.

a = 'light is better than drak'
print(a[::-1])

rev = ''
for i in range(len(a)) :
    rev += a[-(i-(len(a)-1))]

print(rev)

#11.
c = 'madam'
b = c[::-1]
if c == b:
    print('It\'s palindrome')
else:
    print('It\'s not a palindrome')






















    
































