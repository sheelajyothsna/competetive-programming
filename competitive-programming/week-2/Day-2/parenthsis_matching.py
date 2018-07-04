import unittest


def get_closing_paren(sentence, opening_paren_index):

    # Find the position of the matching closing parenthesis
    
    l=len(sentence)
    count=0
    while opening_paren_index<l:
        p=sentence[opening_paren_index]
        if p=="(":
            count+= 1
        elif p== ")":
            count-= 1
            if count == 0:
                return opening_paren_index
        opening_paren_index+= 1
    if count!=0:
        raise Exception

    return -1






# Tests

class Test(unittest.TestCase):

    def test_all_openers_then_closers(self):
        actual = get_closing_paren('((((()))))', 2)
        expected = 7
        self.assertEqual(actual, expected)


    def test_mixed_openers_and_closers(self):
        actual = get_closing_paren('()()((()()))', 5)
        expected = 10
        self.assertEqual(actual, expected)

    def test_no_matching_closer(self):
        with self.assertRaises(Exception):
            get_closing_paren('()(()', 2)


unittest.main(verbosity=2)