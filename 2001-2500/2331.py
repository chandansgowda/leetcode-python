# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if root.val==0 or root.val==1:
            return root.val
        elif root.val==2:
            return self.evaluateTree(root.left) or self.evaluateTree(root.right)
        elif root.val==3:
            return self.evaluateTree(root.left) and self.evaluateTree(root.right)
        
