class Sum:
    @staticmethod
    def sumAll(*args):
        sum = 0
        for ii in args:
            sum += ii
        return sum
def main():
    print(Sum.sumAll(1,2,3,4,5))
main()