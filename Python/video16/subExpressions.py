import re

randStr = 'my phone number is 412-555-1212'

regex = re.compile(r'412-(.*)')

matches = re.findall(regex,randStr)

print(len(matches))

for ii in matches:
    print(ii)