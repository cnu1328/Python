ch = input('Enter a character : ')
ch = ch[0]
if ch == 'a'or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u'or ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U' :
    print('Entered character is a vowel ')
else :
    print('Entered character is not a vowel ' )

vowel = ['a','e','i','o','u','A','E','I','O','U']
for i in vowel :
    if ch == i:
        print("Entered Cahracter is a vowel")
        break
else:
    print("Entered character is not a vowel")

    
