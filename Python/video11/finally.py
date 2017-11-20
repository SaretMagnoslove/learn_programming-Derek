num1, num2 = input('Enter two nums to divide: ').split()
try:
    quotient = int(num1) / int(num2)
    print('{}/{}={}'.format(num1, num2, quotient))
except ZeroDivisionError:
    print('Zero is a big No NO')
else:
    print('You did well')
finally:
    print('I love you no matter what')
