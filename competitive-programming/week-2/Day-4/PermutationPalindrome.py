import unittest

def has_palindrome_permutation(the_string):

    # Check if any permutation of the input is a palindrome
    dict = {}
    list=[]

    for x in the_string:
        if x in dict:
            dict[x] += 1
        else:
            list.append(x)
            dict[x] = 1


    for x in list:
        if dict[x] % 2 == 0:
            del dict[x]

    if len(dict) == 1 or len(dict) == 0:
        return True

    return False














# Tests

class Test(unittest.TestCase):

    def test_permutation_with_odd_number_of_chars(self):
        result = has_palindrome_permutation('aabcbcd')
        self.assertTrue(result)

    def test_permutation_with_even_number_of_chars(self):
        result = has_palindrome_permutation('aabccbdd')
        self.assertTrue(result)

    def test_no_permutation_with_odd_number_of_chars(self):
        result = has_palindrome_permutation('aabcd')
        self.assertFalse(result)

    def test_no_permutation_with_even_number_of_chars(self):
        result = has_palindrome_permutation('aabbcd')
        self.assertFalse(result)

    def test_empty_string(self):
        result = has_palindrome_permutation('')
        self.assertTrue(result)

    def test_one_character_string(self):
        result = has_palindrome_permutation('a')
        self.assertTrue(result)


unittest.main(verbosity=2)
