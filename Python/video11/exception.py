alist = [1, 2, 3]
try:
    print(alist[3])
except IndexError:
    print('Sorry, index doesn\'t exist...really sorry...like really')
except:
    print('Unknown error occured, congratulations')
