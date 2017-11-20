
def rect_area():
    hight = float(input('Enter hight: '))
    width = float(input('Enter width: '))
    area = hight * width
    return area
def circ_area():
    import math
    radius = float(input('Enter Radius: '))
    area = math.pi * math.pow(radius,2)
    return area
def calculate_area(shape):
    shape = shape.lower()
    if shape == 'rect': return rect_area()
    elif shape == 'circ': return circ_area()
def main():
    shape = (input('Enter a shape(rect or circ):'))
    print('the area of the {} is {:.2f}'.format(shape,calculate_area(shape)))

main()
