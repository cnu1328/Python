class animal :
    def eat(self):
        print('eating...')
class Dog(animal):
    def bow(self):
        print('bowing..')
class cat(animal):
    def meow(self):
        print('meowing')

def main():

    d = Dog()
    c = cat()

    d.eat()
    d.bow()

    c.eat()
    c.meow()

if __name__ == '__main__' :
    main()
