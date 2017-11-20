import re

randStr = "doctor doctors doctor's"

regex = re.compile("[doctor]+['s]*")

matches = re.findall(regex,randStr)

for ii in matches:
    print(ii)
