import fibo
fibolist = []
fibo_leng = int(input('Enter the length of the fibo list: '))
for ii in range(1,fibo_leng+1):
    fibolist.append(fibo.fibo(ii))
print ('Fibo list is: ',fibolist)
    