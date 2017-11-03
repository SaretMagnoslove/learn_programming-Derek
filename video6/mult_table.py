table = [[0]*10 for i in range(10)]

for ii in range(1,11):
    for jj in range(1,11):
        table[ii-1][jj-1] = ii*jj
for line in range(len(table)):
    print (table[line])


