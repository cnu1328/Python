class JustCounter :

    __secretCount = 0

    def count(self):
        self.__secretCount += 1
        print(self.__secretCount)

class main:

    c = JustCounter()

    c.count()
    c.count()

    #print(c.__secretCount)

if __name__ == '__main__':

    main()


import random

class ATM :

    __pin =  random.randint(1000,9999)

    def atmpin(self):
        print(self.__pin)

class main:

    a = ATM()

    a.atmpin()
    #print(a.__pin)

if __name__ == '__main__':

    main()


import random

class SIM:

    __num=random.randint(9000000000,9999999999)
    def PhoneNum(self):
        print(self.__num)

class main:

    p=SIM()
    p.PhoneNum()
    
























    
        
    
