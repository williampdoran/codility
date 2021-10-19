from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def visit(self, tree, path):
        if tree == None:
            return path
        # path.append(tree.val)
        children = []
        if tree.left:
            children.append(tree.left)
        if tree.right:
            children.append(tree.right)
        if children:
            path.append([x.val for x in children])
        for child in children:
            self.visit(child, path)
        return path

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        else:
            return self.visit(root, [[root.val]])