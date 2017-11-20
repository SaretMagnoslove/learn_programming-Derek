word_list = []
avlist = []
with open('MyData.txt',mode='w') as MyData:
    MyData.write('some random text\nsome more random test\nand finally...')
with open('MyData.txt') as MyData:
    while True:
        line = MyData.readline()
        if not line:
            break
        num_word = len(line.split())
        word_list.append(num_word)
        lenword = 0
        for word in line:
            lenword += len(word)
        avword = lenword/num_word
        avlist.append(avword)
        
    for word in range(len(word_list)):
        print ('Number of words in line', word+1,'is',word_list[word])
    for word in range(len(avlist)):
        print('Average length of words in line {}, is {}'.format(word+1,avlist[word]))
        

