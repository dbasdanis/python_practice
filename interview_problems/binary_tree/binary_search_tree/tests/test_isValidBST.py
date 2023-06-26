from unittest import TestCase
from treeNode import TreeNode
from validate_BST import Solution

class TestIsValidBST(TestCase):
    solution = Solution()
    def test_empty_tree(self):
        self.assertTrue(self.solution.isValidBST(None))

    def test_single_node(self):
        root = TreeNode(5)
        self.assertTrue(self.solution.isValidBST(root))

    def test_valid_tree(self):
        root = TreeNode(5)
        root.left = TreeNode(3)
        root.right = TreeNode(7)
        self.assertTrue(self.solution.isValidBST(root))


    def test_right_heavy_tree(self):
        root = TreeNode(5)
        root.left = TreeNode(3)
        root.right = TreeNode(7)
        root.right.left = TreeNode(6)
        self.assertTrue(self.solution.isValidBST(root))

    def test_left_heavy_tree(self):
        root = TreeNode(5)
        root.left = TreeNode(3)
        root.left.right = TreeNode(4)
        root.right = TreeNode(7)
        self.assertTrue(self.solution.isValidBST(root))