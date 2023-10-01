''''num = int(input('Enter a number : '))
num1 = int( input('Enter other number : ' ))
if num>num1 :
    print(num ,' is greater number than ', num1)
else :
    print(num1 ,' is greater number than ' , num )


num2 = int( input('Enter other number : ' ))
if num>num2 :
    print(num ,' is greater number than ', num1,',',num2)
elif num1>num2 :
    print(num1 ,' is greater number than ' , num,',', num2 )
else :
    print(num2 ,' is greater number than ' , num,',', num1)

'''
a = int(input('Enter a value : '))
b = int(input('Enter a value : '))
c = int(input('Enter a value : '))

if a>b:
    if b>c:
        print(b," is middle number than ",a,"and",c)
    else:
        if a>c:
            print(c," is middle number than ",a,"and",b)
        else:
            print(a," is middle number than ",b,"and",c)
else:
    if b<c:
        print(b," is middle number than ",a,"and",c)
    else:
        if a<c:
            print(c," is middle number than ",a,"and",b)
        else:
            print(a," is middle number than ",b,"and",c)
