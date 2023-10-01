#say ascii value of given character or number
'''ascii values
numbers - 48 - 57
uppercase - 65-90
lowercase - 97-122'''
ch = input("Enter a character : ")
ch = ch[0]
ascii = ord(ch)
if ascii >= 48 and ascii < 58 :
    print("Entered character is a 'NUMBER'")
elif ascii >=65 and ascii < 91 :
    print("Entered character is a 'UPPERCASE ALPHABET'")
elif ascii >=97 and ascii < 123:
    print("Entered character is a 'LOWERCASE ALPHABET'")
else :
    print("Please Enter a valid character ")
