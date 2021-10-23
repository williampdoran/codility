# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def insert(self, root, val):
        if val < root.val:
            # look left
            if root.left is None:
                root.left = TreeNode(val)
            else:
                self.insert(root.left, val)
        else: #look right
            if root.right is None:
                root.right = TreeNode(val)
            else:
                return self.insert(root.right, val)
        return root

    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None: return TreeNode(val)
        else: self.insert(root, val)
        return root