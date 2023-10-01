''' ascii values
 numbers 48 - 57
 lower   97 - 122
 upper   65 - 90
'''
u = 0
l = 0
n = 0
inp = 0
while inp != '*' :
    inp = input("Enter the characters : ")
    inp = inp[0]
    asci = ord(inp)
    if asci >= 48 and asci <=57 :
        n += 1
    elif asci >= 97 and asci <= 122 :
        l += 1
    elif asci >= 65 and asci <= 91 :
        u += 1
    else :
        print('invalid character ')
print("Total number of numbers entered by user is ", n)
print("Total number of lowercase entered by user is ", l)    
print("Total number of uppercase entered by user is ", u)
