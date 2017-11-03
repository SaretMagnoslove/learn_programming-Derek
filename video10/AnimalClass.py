class Animal:
    def __init__(self, birthtype='Unknown', appearance='unknown', blooded='unknown'):
        self.birthtype = birthtype
        self.appearance = appearance
        self.blooded = blooded

    @property
    def birthtype(self):
        return self.__birthtype

    @birthtype.setter
    def birthtype(self, birthtype):
        self.__birthtype = birthtype

    @property
    def appearance(self):
        return self.__appearance

    @appearance.setter
    def appearance(self, appearance):
        self.__appearance = appearance

    @property
    def blooded(self):
        return self.__blooded

    @blooded.setter
    def blooded(self, blooded):
        self.__blooded = blooded

    def __str__(self):
        return ('A {} is {} it is {} it is {}'.format(type(self).__name__, self.birthtype,
                                                      self.appearance, self.blooded))


class Mammal(Animal):
    def __init__(self, birthtype='born alive', appearance='hair and fur', blooded='hot',
                 nurseyoung=True):
        Animal.__init__(self, birthtype, appearance, blooded)
        self.__nurseyoung = nurseyoung

    @property
    def nurseyoung(self):
        return self.__nurseyoung

    @nurseyoung.setter
    def nurseyoung(self, nurseyoung):
        self.__nurseyoung = nurseyoung

    def __str__(self):
        return super().__str__() + ' and it is {} it nurse his young'.format(
            self.nurseyoung)


class reptile(Animal):
    def __init__(self, birthtype='an egg', appearance='dry scales', blooded='cold'):
        Animal.__init__(self, birthtype, appearance, blooded)

    def sumAll(self, *args):
        sum = 0
        for ii in args:
            sum += ii
        return sum


def getbirthtype(theobject):
    print('the {} is {}'.format(type(theobject).__name__, theobject.birthtype))


def main():
    animal1 = Animal('Born alive')
    print(animal1.birthtype)
    print(animal1)
    mammal1 = Mammal()
    print()
    print(mammal1.birthtype, mammal1.appearance,
          mammal1.blooded, mammal1.nurseyoung)
    print(mammal1)
    reptile1 = reptile()
    print()
    print(reptile1.birthtype)
    print(reptile1)
    print('Sum: {}'.format(reptile1.sumAll(1, 2, 3, 4, 5)))
    getbirthtype(mammal1)
    getbirthtype(reptile1)


main()
