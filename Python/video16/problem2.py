import re

randStr = 'my phone numbers are 412-555-1212 412-555-1213 412-555-1214'

regex = re.compile(r'412-(.{8})')

matches = re.findall(regex,randStr)
print(matches)

print(len(matches))

for ii in matches:
    print(ii)