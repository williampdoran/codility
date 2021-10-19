class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def visit(self, tree, path, children):
        if tree == None:
            return path
        path.append(tree.val)
        if tree.left:
            children.append(tree.left)
        if tree.right:
            children.append(tree.right)
        if len(children) > 0:
            self.visit(children.pop(), path, children)
        return path
