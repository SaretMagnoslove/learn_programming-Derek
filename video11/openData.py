try:
    MyFile = open('MyData2.txt')
except FileNotFoundError as ex:
    print('Your file name sucked!')
    print (ex.args)
else:
    print(MyFile.read())
    MyFile.close()
finally:
    print('doesn\'t really matters...')

