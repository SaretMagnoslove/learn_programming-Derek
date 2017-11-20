def isodd(num):
    if num % 2 == 0:
        return False
    else:
        return True

def oddlist(func, alist):
    newlist = []
    for num in alist:
        if func(num):
            newlist.append(num)
    return newlist

print(oddlist(isodd,[1,2,3,4,5]))
