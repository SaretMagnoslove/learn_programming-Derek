name_list = []
ans = ''
while ans != 'N':
    name = input('Enter a name: ')
    name_list.append(name)
    ans = input('Do you want to enter a costumer? ')
else:
    for name in name_list:
        print(name)