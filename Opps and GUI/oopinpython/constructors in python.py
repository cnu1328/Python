class sample:
    x = 0

    def __init__(self,y):

        sample.x=y
        print('consturctor is activated x =',sample.x)

    def dist(self):
        print('this is ordianary x = ',sample.x)
        

ob = sample(100)
ob1 = sample(300)
ob.dist()

sample.x = 300
print('the value of x is  ',sample.x)



class Employname :

    empcount = 0

    def __init__(self,name,salary):

        self.name = name
        self.salary = salary
        Employname.empcount += 1

    def displaycount(self):
        print('count of employees : ',Employname.empcount)

    def displayemployee(self):

        print('employ name : ',self.name,' employ salary : ',self.salary)

ob = Employname('srinu', 150000)
ob1 = Employname('pranav', 500000)

ob.displayemployee()
ob1.displayemployee()

ob.displaycount()







































