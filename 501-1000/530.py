# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        prev,res = None,float('inf')

        def dfs(root):
            if not root:
                return None

            dfs(root.left)

            nonlocal prev,res
            if prev:
                res = min(res,root.val-prev.val)
            prev = root

            dfs(root.right)

        dfs(root)
        return res
