# Definition for a binary tree node.
from  typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def visit(self, root, path, target):
        if not root:
            return False
        path.append(root.val)
        # print(f'p={path}')
        if root.left is None and root.right is None and sum(path) == target:
            # print(f'target={path}')
            return True
        if self.visit(root.left, path, target) or self.visit(root.right, path, target):
            return True
        path.pop(-1)
        return False

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None: return False
        else: return self.visit(root, [], targetSum)
