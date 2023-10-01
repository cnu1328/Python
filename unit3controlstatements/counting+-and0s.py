pc = 0
nc = 0
zc = 0
num = 0
while num != -1 :
    num = int(input("Enter numbers +ve, -ve and zero : "))
    if num >= 1 :
        pc += 1
    elif num < 0 :
        nc += 1
    else :
        zc += 1
print("Entered positive numbers ", pc )
print("Entered negative numbers ", nc )
print("Entered zero's ", zc )
    
