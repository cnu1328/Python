p = 0
n = 0
sp = 0
sn = 0
inp = 0
while inp != -1 :
    inp = int(input("Enter your integer values : "  ))
    if inp>= 0 :
        p += 1
        sp += inp
    else :
        n += 1
        sn += inp
pavg = sp/p
navg = sn/n
print("Average of positive numbers is " , pavg)
print("Average of negative numbers is " , navg)
