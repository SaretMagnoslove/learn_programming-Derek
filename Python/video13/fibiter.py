class FibIter:
    def __init__(self):
        self.fibo = [1, 1, 2, 3, 5, 8, 13, 21]
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.fibo)-1:
            raise StopIteration
        self.index += 1
        return self.fibo[self.index]


def main():
    fibo = FibIter()
    for num in fibo:
        print(num)


main()
