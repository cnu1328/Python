class first():
    def __init__(self):

        print('first')

class second(first):

    def __init__(self):

        super().__init__()

        print('second')

class third(second,first):

    def __init__(self):

        super().__init__()

        print('third')


class main():

     third()

if __name__ == '__main__' :

    main()





#other example

class animal():

    def cat(self):

        print('eating..')
        
class dog(animal):

    def dog1(self):

        print('running...')

class babydog(dog):

    def dog2(self):

        print('following..')

class main():

    d = babydog()

    d.cat()
    d.dog1()
    d.dog2()

if __name__ == '__main__':

    main()











































