import random
a = random.randint(1,10)
while True:
    guess = int(input('Guess a number:'))
    if guess == a:
         print ('You are right')
         break
    else: print('Try again')
