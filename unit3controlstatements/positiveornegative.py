'''#how to check a number is a +ve or negatve
num = float(input("Enter a value : "))
if num < 0 :
    print("Entered number is negative")
elif num > 0:
    print("Enterd number is positive")
else :
    print("Enterd number is Zero")'''


#whileloop
i=0
while i<10 :
    print(i)
    i+=1
#forloop
for i in range(1,10):
    print(i)

#Break
for i in range(1,10):
    #print(i,end='')
    if i==5 :
        break
    print(i,end='')
#continue
print('\n')
for i in range(1,10):
    #print(,i,end='')
    if i==5 :
        continue
    print(i,end='')
print('\n')
for i in "HELLO" :
    #print(,i,end='')
    if i==5 :
        pass
    print("PASS",i)
#nestedloop
for i in range(1,10):
    for j in range(2,7):
        a = i*j
        print(a,end=' ')
        
print('\n')

n = 5
for i in range(1,11):
    print(n,'*',i,'=',n*i)































    
    
