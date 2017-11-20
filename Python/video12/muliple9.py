import random
alist = list(random.randint(1,1001) for ii in range(100))
print(list(filter((lambda x:x%9==0),alist)))

