import re

randStr = 'my phone number is 412-555-1212'

regex = re.compile(r'412-(.*)-(.*)')

matches = re.findall(regex,randStr)

print(matches[0][0])
print(matches[0][1])
