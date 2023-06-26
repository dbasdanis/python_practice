import unittest

class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class TestNode(unittest.TestCase):
    def test_node_creation(self):
        node = Node(1)
        self.assertEqual(node.val, 1)
        self.assertIsNone(node.left)
        self.assertIsNone(node.right)

    def test_node_with_left_child(self):
        left_child = Node(2)
        node = Node(1, left_child)
        self.assertEqual(node.val, 1)
        self.assertEqual(node.left.val, 2)
        self.assertIsNone(node.right)

    def test_node_with_right_child(self):
        right_child = Node(3)
        node = Node(1, right=right_child)
        self.assertEqual(node.val, 1)
        self.assertIsNone(node.left)
        self.assertEqual(node.right.val, 3)

    def test_node_with_both_children(self):
        left_child = Node(2)
        right_child = Node(3)
        node = Node(1, left_child, right_child)
        self.assertEqual(node.val, 1)
        self.assertEqual(node.left.val, 2)
        self.assertEqual(node.right.val, 3)

if __name__ == '__main__':
    unittest.main()