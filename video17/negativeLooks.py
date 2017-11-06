import re

randStr = "8 Apples $3, 1 Bread $1, 1 Cereal $4"

regex = re.compile(r'(?<!\$)\d')

matches = re.findall(regex,randStr)

matches = [int(ii) for ii in matches]

from functools import reduce

print('sum of items is: {}'.format(reduce(lambda x,y:x+y,matches)))

