import random
import math
def get_random(floor, ceiling):
    return math.floor(random.randint(0,1)*(ceiling - floor) +floor)
def shuffle(the_list):

    # Shuffle the input in place\
    n = len(the_list)
    i = 0
    for num in the_list:
        
        base = int(get_random(i, n-1))
        print base
        temp = the_list[i]
        the_list[i] = the_list[base]
        the_list[base] = temp
        i+=1

    return the_list


sample_list = [1, 2, 3, 4, 5]
print 'Sample list:', sample_list

print 'Shuffling sample list...'
shuffle(sample_list)
print sample_list