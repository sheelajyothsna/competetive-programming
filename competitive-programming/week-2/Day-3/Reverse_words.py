import unittest


def reverse_words(message):

    lenOfMsg = len(message)
    if lenOfMsg == 0:
        return message

    reverselist(message, 0, lenOfMsg-1)
    # print("message ",message)
    p = 0
    for k in range(lenOfMsg):
        if message[k] == " ":
            reverselist(message, p, k-1)
            p =  k+ 1
    reverselist(message, p, lenOfMsg-1)

    return message


def reverselist(list, i, j):
    if j == 0:
        return list
    while i < j:
        temp = list[i]
        list[i] = list[j]
        list[j] = temp

        i += 1
        j -= 1
    # print(list_of_chars)
    return list

# Tests

class Test(unittest.TestCase):

    def test_one_word(self):
        message = list('vault')
        reverse_words(message)
        expected = list('vault')
        self.assertEqual(message, expected)

    def test_two_words(self):
        message = list('thief cake')
        reverse_words(message)
        expected = list('cake thief')
        self.assertEqual(message, expected)

    def test_three_words(self):
        message = list('one another get')
        reverse_words(message)
        expected = list('get another one')
        self.assertEqual(message, expected)

    def test_multiple_words_same_length(self):
        message = list('rat the ate cat the')
        reverse_words(message)
        expected = list('the cat ate the rat')
        self.assertEqual(message, expected)

    def test_multiple_words_different_lengths(self):
        message = list('yummy is cake bundt chocolate')
        reverse_words(message)
        expected = list('chocolate bundt cake is yummy')
        self.assertEqual(message, expected)

    def test_empty_string(self):
        message = list('')
        reverse_words(message)
        expected = list('')
        self.assertEqual(message, expected)


unittest.main(verbosity=2)