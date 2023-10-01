'''#given year leap or not
year = int(input("Enter a year to check leap or not : "))
if year%100 == 0 :
    if year%400 == 0:
        print("Entered year(",year,") is a leap year")
    else :
        print("Entered year(",year,") is not a leap year")
else :
    if year%4 == 0 :
        print("Entered year(",year,") is a leap year")
    else :
        print("Entered year(",year,") is not a leap year")'''



y = int(input("Enter a year to check leap or not : "))
if y%100 == 0 and y%400 == 0 or y%4==0:
    print("Entered year(",y,") is a leap year")
else :
    print("Entered year(",y,") is not a leap year")



for i in range(1800,1901):
    if i%400==0 and i%100==0 or i%4==0 :
        print(i,end=',')
    
    
