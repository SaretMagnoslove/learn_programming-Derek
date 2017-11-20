import re

randStr = '''ape is big
turtle is slow
cheetah is fast
dragon is just awsome'''

regex = re.compile(r'(?m)^.*?\s')

matches = re.findall(regex,randStr)

print(len(matches))

for ii in matches:
    print(ii)