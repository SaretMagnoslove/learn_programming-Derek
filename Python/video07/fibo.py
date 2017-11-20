def fibo(num):
    if num <=2:
        return 1
    else:
        next_num = fibo(num-2)+fibo(num-1)
    return next_num
def main():
    fibo_number = int(input('Enter place in fibo: '))
    print (fibo(fibo_number))
if __name__ == "__main__":
    main()

