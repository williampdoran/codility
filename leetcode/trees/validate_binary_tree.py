# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def visit(self, root, path):
        # print(f"p={path}\n")
        if(root.left):
            self.visit(root.left, path)
        path.append(root.val)
        if (root.right):
            self.visit(root.right, path)
        return path

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None: return False
        elif not root is None and (root.left is None and root.right is None):
            return True
        else:
            path = self.visit(root, [])
            # print(f"p={path}\n")
            for i in range(len(path)-1):
                if path[i] >= path[i +1]:
                    return False
            return True