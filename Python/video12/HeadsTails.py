import random
randomlist = []
heads,tails = 0,0
for num in range(100):
    randomlist.append(random.choice(['H', 'T']))    
print('Heads = {},Tails = {}'.format(randomlist.count('H'),randomlist.count('T')))
