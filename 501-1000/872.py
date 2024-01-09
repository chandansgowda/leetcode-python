# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def findLeaf(root):
            if not root:
                return []
            if not (root.left or root.right):
                return [root.val]
            return findLeaf(root.left) + findLeaf(root.right)
        return findLeaf(root1)==findLeaf(root2)



class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return []
            if not root.left and not root.right:
                return [root.val]
            return dfs(root.left) + dfs(root.right)
        return dfs(root2)==dfs(root1)
        
