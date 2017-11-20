import re
# a simple example
randStr = 'the cat cat fell off the window'
regex = re.compile(r'(\b\w+)\s+\1')
matches = re.findall(regex, randStr)
for ii in matches:
    print(ii)
# a real world example
randStr = "<a href='#'><b>The Link</b></a>"
regex = re.compile(r'<b>(.*?)</b>')
randStr = re.sub(regex,r'\1',randStr)
print (randStr)
# another example: phone number
randStr = '412-555-1212'
regex = re.compile(r'([\d]{3})-([\d]{3}-[\d]{4})')
randStr = re.sub(regex,r'(\1)\2',randStr)
print (randStr)
