import re

# example 1
if re.search('ape', 'the ape is at the apex'):
    print('there is an ape here')
# example 2
allapes = re.findall('ape','the ape is at the apex')
for ii in allapes:
    print(ii)
allapes = re.findall('ape.','the ape is at the apex')
for ii in allapes:
    print(ii)
# example 3
theStr = 'the ape is at at the apex'
for ii in re.finditer('ape.',theStr):
    LocTuple = ii.span()
    print(LocTuple)
    print(theStr[LocTuple[0]:LocTuple[1]])
#example 4
animalStr = 'cat mat pat and rat in a hut'
allAnimals = re.findall('[cmpr]at',animalStr)
for ii in allAnimals:
    print(ii)
someAnimals = re.findall('[a-m]at',animalStr)
print('in someAnimals')
for ii in someAnimals:
    print(ii)
moreAnimals = re.findall('[^cr]at',animalStr)
print('in moreAnimals')
for ii in moreAnimals:
    print(ii)


