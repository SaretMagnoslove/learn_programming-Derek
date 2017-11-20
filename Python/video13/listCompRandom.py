# generate 50 random number betweem 1 and 1000 and return multiples of 9
import random
print([x for x in [random.randint(1,1001) for ii in range(50)] if x%9==0])
