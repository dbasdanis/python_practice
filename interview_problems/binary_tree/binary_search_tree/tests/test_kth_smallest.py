import unittest
from kth_smallest import TreeNode,Solution

class TestKthSmallest(unittest.TestCase):
    def test_kth_smallest(self):
        # Test case 1: root node is None
        solution = Solution()
        root = None
        k = 1
        self.assertEqual(solution.kthSmallest(root, k), 0)

        # Test case 2: k is less than 0
        root = TreeNode(5)
        root.left = TreeNode(3)
        root.right = TreeNode(7)
        k = -1
        self.assertEqual(solution.kthSmallest(root, k), 0)

        # Test case 3: k is greater than number of nodes in the tree
        root = TreeNode(5)
        root.left = TreeNode(3)
        root.right = TreeNode(7)
        k = 4
        self.assertEqual(solution.kthSmallest(root, k), 0)

        # Test case 4: k is equal to number of nodes in the tree
        root = TreeNode(5)
        root.left = TreeNode(3)
        root.right = TreeNode(7)
        k = 3
        self.assertEqual(solution.kthSmallest(root, k), 7)

        # Test case 5: k is equal to 1
        root = TreeNode(5)
        root.left = TreeNode(3)
        root.right = TreeNode(7)
        k = 1
        self.assertEqual(solution.kthSmallest(root, k), 3)

        # Test case 6: k is equal to 2
        root = TreeNode(5)
        root.left = TreeNode(3)
        root.right = TreeNode(7)
        k = 2
        self.assertEqual(solution.kthSmallest(root, k), 5)

        # Test case 7: k is equal to 3
        root = TreeNode(5)
        root.left = TreeNode(3)
        root.right = TreeNode(7)
        k = 3
        self.assertEqual(solution.kthSmallest(root, k), 7)

        # Test case 8: k is equal to 4
        root = TreeNode(5)
        root.left = TreeNode(3)
        root.right = TreeNode(7)
        k = 4
        self.assertEqual(solution.kthSmallest(root, k), 0)

        # Test case 9: k is equal to 5
        root = TreeNode(5)
        root.left = TreeNode(3)
        root.right = TreeNode(7)
        k = 5
        self.assertEqual(solution.kthSmallest(root, k), 0)

        # Test case 10: k is equal to 6
        root = TreeNode(5)
        root.left = TreeNode(3)
        root.right = TreeNode(7)
        k = 6
        self.assertEqual(solution.kthSmallest(root, k), 0)

if __name__ == '__main__':
    unittest.main()