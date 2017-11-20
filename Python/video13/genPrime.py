def isprime(num):
    for ii in range(2, num):
        if num % ii == 0:
            return False
    return True


def genPrime(maxnum):
    for num in range(2, maxnum):
        if isprime(num):
            yield num


def main():
    prime = genPrime(50)

    for ii in range(10):
        print(next(prime))


main()
