from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def search(self, root, val) -> Optional[TreeNode]:
        # print(f'r= {root}\n')
        if root is None: return None
        if root.val == val:
            return root
        elif root.val > val:
            return self.search(root.left, val)
        else:
            return self.search(root.right, val)

    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None: return root
        else: return self.search(root, val)