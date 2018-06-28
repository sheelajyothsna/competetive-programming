import unittest


class Trie(object):

    # Implement a trie and use it to efficiently store strings
    

    def __init__(self):
        self.path = {}
        self.marked = False

    def add_word(self, key):
        if len(key) == 0:
            if key in self.path:
                return False
            else:
                node = Trie()
                node.marked = True
                self.path[key] = node
                return True
        root = key[0]
        if root in self.path:
            node = self.path[root]
        else:
            node = Trie()
            self.path[root] = node

        if len(key) > 1:
            remains = key[1:]
            return node.add_word(remains)
        else:
            if node.marked:
                return False
            else:
                self.path[root].marked = True
                return True  








# Tests

class Test(unittest.TestCase):

    def test_trie_usage(self):
        trie = Trie()

        result = trie.add_word('catch')
        self.assertTrue(result, msg='new word 1')

        result = trie.add_word('cakes')
        self.assertTrue(result, msg='new word 2')

        result = trie.add_word('cake')
        self.assertTrue(result, msg='prefix of existing word')

        result = trie.add_word('cake')
        self.assertFalse(result, msg='word already present')

        result = trie.add_word('caked')
        self.assertTrue(result, msg='new word 3')

        result = trie.add_word('catch')
        self.assertFalse(result, msg='all words still present')

        result = trie.add_word('')
        self.assertTrue(result, msg='empty word')

        result = trie.add_word('')
        self.assertFalse(result, msg='empty word present')


unittest.main(verbosity=2)
