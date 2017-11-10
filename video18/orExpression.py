import re

randStr = '1. Dog 2. Cat 3. Turtle'

regex = re.compile(r'\d.\s(Dog|Cat)')

matches = re.findall(regex,randStr)

for ii in matches:
    print(ii)