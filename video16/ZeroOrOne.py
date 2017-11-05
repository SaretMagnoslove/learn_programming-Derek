import re
randStr = 'cat cats catcat catatonia catancdefghijklmnopqrst'

regex = re.compile('[cat]+s?')

matches = re.findall(regex, randStr)

for ii in matches:
    print(ii)
