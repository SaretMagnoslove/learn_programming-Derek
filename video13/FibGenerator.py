class FibGenerator:
    def __init__(self):
        self.first = 0
        self.second = 1

    def __inter__(self):
        return self

    def __next__(self):
        fibnum = self.first + self.second
        self.first = self.second
        self.second = fibnum
        return fibnum


def main():
    fibsuq = FibGenerator()
    num = int(input('Number of fib to generate: '))
    for ii in range(num):
        print('Fib: ', next(fibsuq))


main()
