# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.deepest = float('-inf')
        self.res = 0

    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        def dfs(root, level):
            if not root:
                return
            if level>self.deepest:
                self.res = root.val
                self.deepest = level
            elif level ==self.deepest:
                self.res += root.val
            dfs(root.left,level+1)
            dfs(root.right,level+1)
        
        dfs(root,0)
        return self.res
        
