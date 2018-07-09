import unittest


def is_single_riffle(half1, half2, shuffled_deck):

    # Check if the shuffled deck is a single riffle of the halves
    i=j=k=0
    n1 = len(half1)
    n2 = len(half2)
    n3 = len(shuffled_deck)
    if((n1+n2)!=n3): return False
    while(i<n1 and j <n2 and k< n3):
        if(shuffled_deck[k]==half1[i]): i=i+1
        elif(shuffled_deck[k]==half2[j]): j=j+1
        else: return False
        k=k+1
    if(i<n1):
        if(shuffled_deck[k]==half1[i]): i=i+1
        else: return False
        k=k+1
    elif(j<n2):
        if(shuffled_deck[k]==half2[j]): j=j+1
        else: return False
        k=k+1

    return True





# Tests

class Test(unittest.TestCase):

    def test_both_halves_are_the_same_length(self):
        result = is_single_riffle([1, 4, 5], [2, 3, 6], [1, 2, 3, 4, 5, 6])
        self.assertTrue(result)

    def test_halves_are_different_lengths(self):
        result = is_single_riffle([1, 5], [2, 3], [1, 2, 6, 3, 5])
        self.assertFalse(result)

    def test_one_half_is_empty(self):
        result = is_single_riffle([], [2, 3, 6], [2, 3, 6])
        self.assertTrue(result)

    def test_shuffled_deck_is_missing_cards(self):
        result = is_single_riffle([1, 5], [2, 3, 6], [1, 6, 3, 5])
        self.assertFalse(result)

    def test_shuffled_deck_has_extra_cards(self):
        result = is_single_riffle([1, 5], [2, 3, 6], [1, 2, 3, 5, 6, 8])
        self.assertFalse(result)


unittest.main(verbosity=2)
