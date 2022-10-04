# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        result = f"{self.val}"
        if self.left != None:
            result = f"{self.left}->{result}"
        if self.right != None:
            result = f"{result}<-{self.right}->"
        return result


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

    def invertTreeRec(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return root
        else:
            root.left, root.right = root.right, root.left
            self.invertTreeRec(root.right)
            self.invertTreeRec(root.left)
        return root

root = TreeNode(4, left=TreeNode(2, left=TreeNode(1), right=TreeNode(3)), right=TreeNode(7, left=TreeNode(6), right=TreeNode(9)))
print(root)
print(Solution().invertTreeRec(root))
print(Solution().invertTree(root=root))