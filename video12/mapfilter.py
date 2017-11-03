alist = range(1,11)
print(list(map(lambda x:x*2,alist )))

alist = list(map((lambda x,y:x+y),[1,2,3],[1,2,3]))
print (alist)

print(list(filter((lambda x:x%2==0),range(1,11))))