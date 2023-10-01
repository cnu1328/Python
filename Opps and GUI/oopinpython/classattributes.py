# class attributes
class employee :
    '''it gives employees information'''
    empcount = 0

    def __init__(self,name,salary):

        self.name = name
        self.salary = salary
        employee.empcount +=1
    def displayemployee(self):
        print('name ',self.name, ',salary ', self.salary)
    def displayempcount(self):
        print('no. of employees : ', self.empcount)

class main():
	emp1 = employee('srinu',250000)
	emp2 = employee('shashi',520000)

	emp1.displayemployee()
	emp2.displayemployee()

	print('Total employee no. ' , employee.empcount)

	emp1.age = 7
	print('age = ',emp1.age)

	emp1.age = 8

	print('age = ',emp1.age)

	del emp1.age

	op = hasattr(emp1,'age')

	if op == False :
		setattr(emp1,'age',80)
	print('new age ',getattr(emp1,'age'))

	delattr(emp1,'age')
	#print('new age ',getattr(emp1,'age'))


	print(employee.__doc__)
	print(employee.__name__)
	print(employee.__dict__)
	print(employee.__module__)
	print(employee.__bases__)
	

    
