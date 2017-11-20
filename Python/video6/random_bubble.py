import random
length_list = int(input('Enter length of random list: '))
random_list = []
for ii in range(length_list):
    random_list.append(random.randint(1,9))

def bubble_sort(the_list):
    size = len(the_list)
    while size > 0:
        for ii in range(size-1):
            if the_list[ii]>the_list[ii+1]:
                the_list[ii],the_list[ii+1] = the_list[ii+1],the_list[ii]
        size -= 1
    return the_list

def main():
    print ('The sorted list is: ',bubble_sort(random_list))
main()