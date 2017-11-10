import re

randStr = "12345 12345-1234 1234 12346-333"

regex = re.compile(r'(\d{5}\s|\d{5}-\d{4})') 

matches = re.findall(regex,randStr)

for ii in matches:
    print(ii)

