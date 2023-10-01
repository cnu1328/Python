sum = 0
for i in range(1,11):
    sum += i
avg = sum/10
print('Total sum is ' , sum , 'and average is ' , avg)

for i in range(1,21):
    print('*',end = '')
print('\n')
m = int(input('Enter a number : ' ))
n = int(input('Enter other number : '))
sum = 0
if m<n:
    for i in range(m,n+1):
        sum += i
    print('sum of total numbers from m-n is ',sum)
else :
    print('m should be less than n ')

