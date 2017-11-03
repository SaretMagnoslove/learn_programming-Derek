age = eval(input('Enter your age here: '))
if age == 5: print('Go to kindergarden')
elif 6<=age<=17:
    print('Go to {} grade'.format(age-5))
elif age > 17: print('Go to college')
else: print('Lucky you!!! You can just stay home :)')