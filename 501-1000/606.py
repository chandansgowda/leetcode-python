# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return ''
        s = str(root.val)
        if root.left is None and root.right is None:
            s += ''
        if root.left:
            s += '({})'.format(self.tree2str(root.left))
        if root.left is None and root.right:
            s += '()'
        if root.right:
            s+= '({})'.format(self.tree2str(root.right))
        return s
        
