class Square:
    def __init__(self, hight = '0', width = '0'):
        self.hight = hight
        self.width = width
    @property
    def hight(self):
        print('retrieving the hight...')
        return self.__hight
    @hight.setter
    def hight(self, value):
        if value.isdigit():
            self.__hight = value
        else:
            print('pls provide only numbers for hight')
    @property
    def width(self):
        print('retrieving the width...')
        return self.__width
    @width.setter
    def width(self, value): 
        if value.isdigit():
            self.__width = value
        else:
            print('pls provide only numbers for width')
    def getArea(self):
        return int(self.__hight) * int(self.__width)
def main():
    aSquare = Square()

    hight = input('enter hight: ')
    width = input('enter width: ')

    aSquare.hight = hight
    aSquare.width = width

    print ('the hight is: ',aSquare.hight)
    print ('the width is: ',aSquare.width)

    print ('the area is: ',aSquare.getArea())

main()

