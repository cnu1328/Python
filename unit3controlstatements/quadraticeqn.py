a = int(input('Enter a value : '))
b = int(input('Enter b value : '))
c = int( input(  'Enter c valur : '))
if a==0 :
    print(" please check your details again\n You entered linear equation values ")
else:
    import cmath

    d = (b**2)- (4*a*c)

    sol1 = (-b - (cmath.sqrt(d)))/(2*a)
    sol2 = (-b + (cmath.sqrt(d)))/(2*a)
    print('Your solutions are ', sol1 ,',',sol2)
