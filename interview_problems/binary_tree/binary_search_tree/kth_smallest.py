from typing import Optional
from treeNode import TreeNode
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        result = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            result.append(root.val)
            root = root.right

        if k > len(result) or k < 0:
            return 0
        return result[k-1]