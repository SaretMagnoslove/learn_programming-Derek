def factorial(num):
    if num <=1:
        return 1
    else:
        result = num * factorial(num-1)
    return result

def main():
    num = int(input('Number for factorial: '))
    print(factorial(num))

main()