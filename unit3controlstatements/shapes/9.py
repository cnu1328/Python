r = 5
for i in range(1,r+1):
    num = 1
    for j in range(r,0,-1):
        if j>i :
            print(' ',end='')
        else:
            print(num,end='')
            num+=1
    print()
    
    
