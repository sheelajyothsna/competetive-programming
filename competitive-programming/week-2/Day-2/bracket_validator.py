import unittest


def is_valid(code):

    # Determine if the input code is valid
    stack =[]
    for i in range(len(code)):
        if(code[i] == '{' or code[i] == '(' or code[i] == '['):
            stack.append(code[i])
        else:
            if not stack:
                return False
            x = stack.pop()
                # print(x)
            if(x=='(' and code[i]!=')'):
                return False
            if(x=='{' and code[i]!='}'):
                return False
            if(x=='[' and code[i]!=']'):
                return False
    if not stack:
        return True
    else:
        return False

    





# Tests

class Test(unittest.TestCase):

    def test_valid_short_code(self):
        result = is_valid('()')
        self.assertTrue(result)

    def test_valid_longer_code(self):
        result = is_valid('([]{[]})[]{{}()}')
        self.assertTrue(result)

    def test_mismatched_opener_and_closer(self):
        result = is_valid('([][]}')
        self.assertFalse(result)

    def test_missing_closer(self):
        result = is_valid('[[]()')
        self.assertFalse(result)

    def test_extra_closer(self):
        result = is_valid('[[]]())')
        self.assertFalse(result)

    def test_empty_string(self):
        result = is_valid('')
        self.assertTrue(result)


unittest.main(verbosity=2)