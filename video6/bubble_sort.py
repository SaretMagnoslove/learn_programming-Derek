def bubble_sort(the_list):
    decrease = 1
    while (len(the_list)-decrease) >0:  
        for ii in range(len(the_list)-decrease):
            if the_list[ii]>the_list[ii+1]:
                the_list[ii],the_list[ii+1] = the_list[ii+1],the_list[ii]
                print(the_list)
        decrease += 1
    return the_list
def main():
    the_list = list((input('Enter a list: ')))
    print ('The sorted list is: ',bubble_sort(the_list))
main()
