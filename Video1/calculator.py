num1,operation,num2 = input('Enter your calculation :').split()
num1 = int(num1)
num2 = int(num2)

if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    result = num1 / num2
else:
    print ('unrecornized operator')

print ('the result of {}{}{} is {}'.format(num1,operation,num2,result))