x = int(input("Enter a number : " ))
n = int(input("Enter other number : " ))
power = x
for i in range(1,n):
    power *= x
print(power)
