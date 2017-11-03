cust_list = []
while True:
    ans = input('Do you want another costumer? ')[0].lower()
    if ans == 'n': break
    else:
        fname,lname = input('Enter first and last names: ').split()
        cust_list.append({'fname':fname,'lname':lname})
for name in cust_list:
    print (name['fname'],name['lname'])