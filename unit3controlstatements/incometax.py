#incometax
income = float(input("please enter your income : "))
if income <= 150000 :
    tax = 0
    print("Your entered income is ", income," and tax applies is ", tax)
elif income > 150000 and income <= 300000 :
    tax = income*(10/100)
    print("Your entered income is ", income," and tax applies is ", tax)
elif income > 300000 and income <= 500000 :
    tax = income*(20/100)
    print("Your entered income is ", income," and tax applies is ", tax)
else :
    tax = income*(30/100)
    print("Your entered income is ", income," and tax applies is ", tax)
