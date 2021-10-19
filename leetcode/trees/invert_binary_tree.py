# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def helper(self, root):
        if root is None:
            pass
        else:
            temp = root.left
            root.left = root.right
            root.right = temp
            self.helper(root.right)
            self.helper(root.left)
        return root

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None: return root
        else: return self.helper(root)