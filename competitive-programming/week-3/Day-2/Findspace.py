import unittest

def find_repeat(the_list):
    low = 1
    high = len(the_list) - 1

    while low < high:
        mid = low + ((high - low) // 2)
        lower_rangelow, lower_rangehigh = low, mid
        upper_rangelow, upper_rangehigh = mid+1, high

        items_in_lower_range = 0
        for item in the_list:

            if lower_rangelow <= item <= lower_rangehigh:
                items_in_lower_range += 1

        distinct_possible_integers_in_lower_range = (
            lower_rangehigh
            - lower_rangelow
            + 1
        )
        if items_in_lower_range > distinct_possible_integers_in_lower_range:

            low, high = lower_rangelow, lower_rangehigh
        else:

            low, high = upper_rangelow, upper_rangehigh

    return low



# Tests

class Test(unittest.TestCase):

    def test_just_the_repeated_number(self):
        actual = find_repeat([1, 1])
        expected = 1
        self.assertEqual(actual, expected)

    def test_short_list(self):
        actual = find_repeat([1, 2, 3, 2])
        expected = 2
        self.assertEqual(actual, expected)

    def test_medium_list(self):
        actual = find_repeat([1, 2, 5, 5, 5, 5])
        expected = 5
        self.assertEqual(actual, expected)

    def test_long_list(self):
        actual = find_repeat([4, 1, 4, 8, 3, 2, 7, 6, 5])
        expected = 4
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
