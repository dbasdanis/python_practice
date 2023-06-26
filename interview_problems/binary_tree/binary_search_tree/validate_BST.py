from typing import Optional
from treeNode import TreeNode

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = []
        prev = None
        while stack or root:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            if prev is not None:
                if prev >= root.val:
                    return False
            prev = root.val
            root = root.right

        return True