import re
# first example
randStr = 'one two three four'
regex = re.compile(r'\w+(?=\b)')
matches = re.findall(regex,randStr)
for ii in matches:
    print(len(ii),ii)
