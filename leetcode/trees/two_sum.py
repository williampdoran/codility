from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inOrder(self, root, path):
        if root.left:
            self.inOrder(root.left, path)
        path.append(root.val)
        if root.right:
            self.inOrder(root.right, path)
        return path
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if root is None: return False
        else:
            path = self.inOrder(root,[])
            # print(f'p = {path}\n')
            hashes = set()
            for i in path:
                diff = k - i
                if diff in hashes:
                    return True
                else:
                    hashes.add(i)
            return False