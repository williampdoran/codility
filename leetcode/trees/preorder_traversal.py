# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def visit(self, tree, accumulator):
        print(f'{tree} \n {accumulator}')
        if tree == None:
            return accumulator
        accumulator.append(tree.val)
        if tree.left:
            self.visit(tree.left, accumulator)
        if tree.right:
            self.visit(tree.right, accumulator)
        return accumulator

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.visit(root, [])