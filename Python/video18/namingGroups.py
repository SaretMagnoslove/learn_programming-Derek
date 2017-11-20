import re

randStr = "December 21 1974"

regex = r'^(?P<month>\w+)\s(?P<days>\d+)\s(?P<year>\d+)'

matches = re.search(regex,randStr)

print ('month: ',matches.group('month'))
print ('day: ',matches.group('days'))
print ('year: ',matches.group('year'))