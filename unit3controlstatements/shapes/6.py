r = int(input('row : '))
for i in range(1,r+1):
    for j in range(1,i+1):
        print(j,end='')
    print()

for i in range(1,r+1):
    for j in range(1,i+1):
        print(i,end='')
    print()
