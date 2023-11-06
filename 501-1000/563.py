# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        def helper(root):
            if not root:
                return 0
            l,r = helper(root.left),helper(root.right)
            self.ans += abs(l-r)
            return root.val + l + r
        self.ans = 0
        helper(root)
        return self.ans
        
