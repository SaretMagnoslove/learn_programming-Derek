def isprime(num):
    for number in range(2,num):
        if num % number == 0: return False
    else:
        return True
def primelist(max_num):
    prime_list = []
    for ii in range(max_num):
        if isprime(ii):prime_list.append(ii)
    return (prime_list)
def main():
    max_num = int(input('Input max num to check: '))
    print (primelist(max_num))

main()
    
