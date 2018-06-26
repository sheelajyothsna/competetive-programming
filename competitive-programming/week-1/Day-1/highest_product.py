import sys
import unittest

high = sys.maxsize
low = -sys.maxsize-1
def highest_product_of_3(arr):
    if len(arr) < 3:
         raise ValueError("cannot be defined")

    max1 = low
    max2 = low
    max3 = low
    min1 = high
    min2 = high

    for i in range(0,len(arr)):
        if arr[i] > max1:
            max3 = max2
            max2 = max1
            max1 = arr[i]

        elif arr[i] > max2:
            max3 = max2
            max2 = arr[i]

        elif arr[i] > max3:
            max3 = arr[i]

        if arr[i] < min1:
            min2 = min1
            min1 = arr[i]

        elif arr[i] < min2:
            min2 = arr[i]

    return max((min1*min2*max1),(max1*max2*max3))


# Tests
class Test(unittest.TestCase):

    def test_short_list(self):
        actual = highest_product_of_3([1, 2, 3, 4])
        expected = 24
        self.assertEqual(actual, expected)

    def test_longer_list(self):
        actual = highest_product_of_3([6, 1, 3, 5, 7, 8, 2])
        expected = 336
        self.assertEqual(actual, expected)

    def test_list_has_one_negative(self):
        actual = highest_product_of_3([-5, 4, 8, 2, 3])
        expected = 96
        self.assertEqual(actual, expected)

    def test_list_has_two_negatives(self):
        actual = highest_product_of_3([-10, 1, 3, 2, -10])
        expected = 300
        self.assertEqual(actual, expected)

    def test_list_is_all_negatives(self):
        actual = highest_product_of_3([-5, -1, -3, -2])
        expected = -6
        self.assertEqual(actual, expected)

    def test_error_with_empty_list(self):
        with self.assertRaises(Exception):
            highest_product_of_3([])

    def test_error_with_one_number(self):
        with self.assertRaises(Exception):
            highest_product_of_3([1])

    def test_error_with_two_numbers(self):
        with self.assertRaises(Exception):
            highest_product_of_3([1, 1])


unittest.main(verbosity=2)
