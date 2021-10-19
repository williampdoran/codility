# Definition for a binary tree node.
from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def visit(self, tree: Optional[TreeNode], accumulator: List[int]) -> List[int]:
        if tree == None:
            return accumulator
        if tree.left:
            self.visit(tree.left, accumulator)
        accumulator.append(tree.val)
        if tree.right:
            self.visit(tree.right, accumulator)
        return accumulator

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.visit(root, [])