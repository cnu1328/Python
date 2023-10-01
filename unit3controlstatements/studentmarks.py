maths = float(input("Please enter your marks obtained in maths subject : "))
physics = float(input("Please enter your marks obtained in physics subject : "))
chemistry = float(input("Please enter your marks obtained in chemistry subject : "))
social = float(input("Please enter your marks obtained in social subject : "))
total = maths + physics + chemistry + social
avg = total/4
if maths >=0 and maths <101 and physics >=0 and physics <101  and chemistry >=0 and chemistry <101 and social >=0 and social < 101 :
    if maths >= 35 and physics >= 35 and chemistry >= 35 and social >= 35 :
        if avg >= 75 :
            print("Your total marks scored is ",total, " and Your average is " , "\nYour Grade is 'DISTINCTION' ")
        elif avg >= 60 and avg <75:
            print("Your total marks scored is ",total, " and Your average is " ,avg, "\nYour Grade is 'FIRST DIVISION' ")
        elif avg >=50 and avg < 60 :
            print("Your total marks scored is ",total, " and Your average is " ,avg, "\nYour Grade is 'SECOND DIVISION' ")
        elif avg >=40 and avg < 50 :
            print("Your total marks scored is ",total, " and Your average is " ,avg, "\nYour Grade is 'THIRD DIVISION' ")
        elif avg >=35 and avg < 40 :
            print("Your total marks scored is ",total, " and Your average is " ,avg, "\nYour Grade is 'PASS' ")
        else :
            print("FAIL")
    else :
        print("FAIL")
else :
    print("Please enter the marks between 1-100 ")
    
              
