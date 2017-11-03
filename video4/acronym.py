somestring = input('Enter some string: ')
acronym = ''
liststring = somestring.split()
for ii in range(len(liststring)):
    acronym += liststring[ii][0].upper()
print ('Acronym is: ',acronym)
