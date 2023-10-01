n = int(input("Enter a number to check amstrong or not : " ))
temp = n
am = 0
while n>0 :
    rem = n%10
    am += rem**3
    n = n//10
print(am)
if temp == am:
    print('Enter number is a Amstrong number')
else :
    print('Enter number is not a Amstrong number')
