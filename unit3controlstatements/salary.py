#salary
'''salary = float(input("Enter your basic salary : "))
HRA = salary*0.1
TA = salary*0.05
salaryt = salary + HRA +TA
print("your HRA is ",HRA, "\nYour TA is ",TA,"\nYour Total salary is ",salaryt)'''
salary = float(input("Enter your salary : "))
gender = input("please enter your Gender : ")
gender = gender[0]
bonus =0
if gender == 'M' or gender=='m' :
    if salary >= 10000 :
        bonus += salary*0.05
        print("Your bonus is ", bonus, "Your salary is ", bonus+salary)
    else :
        bonus +=salary*0.07
        print("Your bonus is ", bonus, "Your salary is ", bonus+salary)
elif gender == 'f' or gender=='F' :
    if salary >= 10000 :
        bonus += salary*0.1
        print("Your bonus is ", bonus, "Your salary is ", bonus+salary)
    else :
        bonus +=salary*0.12
        print("Your bonus is ", bonus, "Your salary is ", bonus+salary)
else :
    print("invalid input")
