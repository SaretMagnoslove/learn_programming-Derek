investment = eval(input('enter initial amount: '))
interest = eval(input('enter you intrest: '))
for year in range(10):
    investment = investment + investment * interest/100
    print('investment afer {} years is {:.3f}'.format(year,investment))
print('finat value after 10 years of investment is:', investment)