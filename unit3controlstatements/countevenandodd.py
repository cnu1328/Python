e = 0
o = 0
esum = 0
osum = 0
inp = 0
while inp!=-1:
    inp = int(input("Enter your values : "))
    if inp%2==0 :
        e +=1
        esum += inp
    else :
        o += 1
        osum += inp
print('Total count of even numbers : ' , e)
print('Total count of odd numbers : ' , o)
print('Total sum of even numbers : ' , esum)
print('Total sum of odd numbers : ' , osum)
print('Avg of even numbers : ' , esum/e)
print('Avg of odd numbers : ' , osum/o)
