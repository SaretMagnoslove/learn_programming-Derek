import re

randStr = '1. bread 2. milk 3. lettuce'

regex = re.compile(r'(?<=\d.\s)\w+')

matches = re.findall(regex,randStr)
for ii in matches:
    print(ii)
