import re

longStr = '''Just some words
and some more\r
and more
'''

print('number of matches: ',len(re.findall('[\w\s]+[\r]?[\n]',longStr)))

matches = re.findall('[\w\s]+[\r]?[\n]',longStr)
for ii in matches:
    print(ii)