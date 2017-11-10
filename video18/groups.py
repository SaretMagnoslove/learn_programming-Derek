import re

bd = input('Enter your bd (mm-dd-yyyy): ')

bdregex = re.search(r'(\d{1,2})-(\d{1,2})-(\d{4})', bd)

print('your birth date is: ',bdregex.group())
print('which means: ')
print('the day date is: ',bdregex.group(1))
print('on month: ',bdregex.group(2))
print('and year: ',bdregex.group(3))



