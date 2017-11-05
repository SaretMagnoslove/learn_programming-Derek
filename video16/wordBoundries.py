import re

randStr = 'ape at the apex'

regex = re.compile(r'\bape\b')

matches = re.findall(regex,randStr)

print(len(matches))

for ii in matches:
    print(ii)