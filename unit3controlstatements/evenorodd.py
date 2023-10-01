print('*'*20)
for i in range (0,20):
    print('*')
'''write a program using for loop to print all
the numbers from m-n thereby classifying them as even or odd.'''
m = int(input('Enter a number : ' ))
n = int(input('Enter other number : ' ))
if m<n :
    for i in range (m,n+1) :
        print(i)
        #print('\n')
        if i%2 == 0 :
            
            print("Even numbers are : ", i )
        else :
            print("Odd numbers are : ", i )
else :
    print('first number should be less than second number')
