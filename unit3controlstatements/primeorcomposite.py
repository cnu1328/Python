'''n = int(input('Enter a number : '))
count = 0
    for i in range(1,n+1):
    if n%i==0 :
        count +=1
if count ==2 :
    print('Entered number is a prime number ')
else: 
    print('Entered number is a composite number ')'''

pc = 0
cc = 0
count = 0 
inp = 0
while inp!=-1 :
    inp = int(input('Enter a number : '))
    for i in range(1,inp+1):
        if inp%i == 0:
            count += 1
    print("THINK ABOUT IT")
            
    
print('prime numbers entered by user ' ,pc)
print('composite numbers entered by user ' ,cc)

'''for i in range(0,7):
    if i == 3 or i==6 :
        continue
    else:
        print(i,end='')
print('')


count = 0
for i in range(2,1000):
    for j in range(2,i):
        if i%j == 0:
            break
    else :
        count += 1
        if count ==101:
            break
        print(i,end=',')
   for i in range(2,inp+1):
        if inp%i ==0 :
            break
    else :
        count += 1
        if count ==2 :
            pc += 1
        else :
            cc += 1         '''
