class Dog:
    def __init__(self, name='',hight=0,weight=0):
        self.name = name
        self.hight = hight
        self.weight = weight
    def run(self):
        print('{}, the dog, is now running...'.format(self.name))
    def eat(self):
        print('{}, the dog, is now eating...'.format(self.name))
    def bark(self):
        print('{}, the dog, is now barking...'.format(self.name))
def main():
    spot = Dog('spot',66,26)
    spot.bark()
    Bowser = Dog()
    Bowser.name = 'Bowser'
    Bowser.eat()

main()
         
