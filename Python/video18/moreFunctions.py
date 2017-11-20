import re

match = re.search(r'\d{2}','The chicken weight 13 lbs.')

print ('match: ',match.group())
print ('span: ',match.span())
print ('start: ',match.start())
print ('end: ', match.end())