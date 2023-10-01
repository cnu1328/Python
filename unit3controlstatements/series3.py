'''n= int(input('Enter a number : '))
sum = 0
for i in range(1,n+1):
    sum += n/(n+1)
print(sum)


n = int(input('Enter a number : ' ))
sum = 0
for i in range(1,n+1) :
    sum += i**3
print(sum)'''

n = int(input('Enter a number : ' ))
sum = 0
for i in range(1,n+1) :
    sum += 1/n
print(sum)


sum = 0
for i in range(1,n+1) :
    sum += 1/(i**2)
print(sum)

sum = 0
for i in range(1,n+1) :
    sum += i**2/i
print(sum)



sum = 0
for i in range(1,n+1) :
    if i%2 ==0 :
        sum += i**2
print(sum)
