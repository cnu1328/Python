#palindrome
num = int(input('Enter a number to check palindrome or not : '))
temp = num
rev =0
while num>0 :
    rem = num%10
    rev = rev*10 + rem
    num = num//10
if temp == rev :
    print('its a palindrome ')
else :
    print('not a palindrome ')



'''t = ['Heads','Tails']
import random
print(Random.random(t))'''

import random
choice = ['Heads','Tails']
user_input = input('To toss your cion press toss or 1 : ')
if user_input == 'toss' or user_input == '1' :
	print(random.choice(choice))
else:
	print('Invalid input')


