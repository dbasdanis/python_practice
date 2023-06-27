import unittest
from trie import TrieNode

class TestTrieNode(unittest.TestCase):
    def setUp(self):
        self.node = TrieNode()

    def test_init(self):
        self.assertEqual(self.node.children, {})
        self.assertFalse(self.node.is_end_of_word)


if __name__ == '__main__':
    unittest.main()