class Dog:
    numofdogs = 0

    def __init__(self, name='unknown'):
        self.name = name
        Dog.numofdogs += 1

    @staticmethod
    def getdognumber():
        print('Current number of dogs is {}'.format(Dog.numofdogs))


def main():
    spot = Dog('Spot')
    Dog.getdognumber()
    doug = Dog('Doug')
    Dog.getdognumber()

main()