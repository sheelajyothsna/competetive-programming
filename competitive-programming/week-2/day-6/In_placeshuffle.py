import random

def get_random(floor, ceiling):
    return random.randrange(floor, ceiling + 1)

def shuffle(the_list):
    # For each index in the list
    if len(the_list)<=1:
        return the_list
    for i in xrange(0, len(the_list) - 1):
        print(the_list)
        # Grab a random other index
        j = get_random(i, len(the_list)-1)
        print(j)
        # And swap the values
        if j != i:
            print("swap")
            the_list[i], the_list[j] = \
                the_list[j], the_list[i]

sample_list = ['a', 'b', 'c','d']
print 'Sample list:', sample_list

print 'Shuffling sample list...'
shuffle(sample_list)
print sample_list
