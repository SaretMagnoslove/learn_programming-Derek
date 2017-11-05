import re

# matching the begining of a string
randStr = 'match everything up to @'

regex = re.compile(r'^.*[^@]')

matches = re.findall(regex, randStr)

for ii in matches:
    print(ii)

# matching the end of the string
randStr = '@ match this string'

regex = re.compile(r'[^@\s].*$')

matches = re.findall(regex, randStr)

for ii in matches:
    print(ii)
