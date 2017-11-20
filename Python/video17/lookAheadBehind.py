import re

randStr = "<h1>I'm Important</h1> <h1>So am I</h1>"

regex = re.compile(r'(?<=<h1>).+?(?=</h1>)')

matches = re.findall(regex,randStr)
for ii in matches:
    print(ii)