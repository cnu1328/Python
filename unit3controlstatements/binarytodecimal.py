a = 20
print(bin(a))
b  = 60
print(bin(b))


n = int(input('Enter a decimal number : ' ))
print(bin(n))
print(oct(n))
print(hex(n))


'''binary = int(input('Enter binary values :'))
print(dec(binary))'''

bi = list(input('Enter binary number : ' ))
dec = 0
for i in range(len(bi)):
    digit = bi.pop()
    if digit == '1' :
        dec += 2**i
print(dec)

bi = list(input('Enter a binary number : '))
dec = 0
size = len(bi)
i = 0
while i < size :
    digit = bi.pop()
    if digit == '1' :
        dec += 2**i
    i += 1
print(dec)
