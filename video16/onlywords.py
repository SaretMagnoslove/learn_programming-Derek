import re

series = '<name>super natural</name><name>buffy the vampire slayer</name>'

matches = re.findall('<name>(.*?)</name>',series)

for ii in matches:
    print(ii)