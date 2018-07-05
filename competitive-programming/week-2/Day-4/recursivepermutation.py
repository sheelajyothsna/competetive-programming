import unittest

def get_permutations(string):
    # Base case
    if len(string) <= 1:
        return set([string])

    all_chars_except_last = string[:-1]
    
    last_char = string[-1]

    permutations_of_all_except_last = get_permutations(all_chars_except_last)
    S = set()
    for permutation_of_all_except_last in permutations_of_all_except_last:
        for position in range(len(all_chars_except_last) + 1):
            permutation = (permutation_of_all_except_last[:position]+ last_char+ permutation_of_all_except_last[position:])
            S.add(permutation)
    # print(permutations)

    return S



# Tests

class Test(unittest.TestCase):

    def test_empty_string(self):
        actual = get_permutations('')
        expected = set([''])
        self.assertEqual(actual, expected)

    def test_one_character_string(self):
        actual = get_permutations('a')
        expected = set(['a'])
        self.assertEqual(actual, expected)

    def test_two_character_string(self):
        actual = get_permutations('ab')
        expected = set(['ab', 'ba'])
        self.assertEqual(actual, expected)

    def test_three_character_string(self):
        actual = get_permutations('abc')
        expected = set(['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)