# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(root,curSum):
            if not root:
                return False

            curSum+=root.val
            if not root.right and not root.left:
                return curSum==targetSum

            return dfs(root.left,curSum) or dfs(root.right,curSum)

        return dfs(root,0)
