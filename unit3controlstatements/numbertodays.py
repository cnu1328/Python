n = int(input('Enter a number b/t 1-7 to get week day : '))
if n >=1 and n<=7 :
    if n==1 :
        print("SUNDAY")
    elif n==2 :
        print('MONDAY ')
    elif n==3 :
        print('TUESDAY')
    elif n==4 :
        print('WEDNESDAY')
    elif n==5 :
        print('THURSDAY')
    elif n==6 :
        print('FRIDAY')
    else :
        print('SATURDAY')
else :
    print('Number should between 1-7 ')
n = int(input('Enter a number b/t 1-7 to get week day : '))   
dic = {1:'Monday',2:'Tuesday',3:'Wednesday',4:'Thursday',5:'Friday',6:'Saturday',7:'Sunday'}
for i in dic:
    if i==n:
        print(dic[i])
    
