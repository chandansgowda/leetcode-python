# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode], cnt=0) -> int:
        if not root: return 0
        cnt ^= 1<<(root.val-1)
        if root.left is None and root.right is None:
            return 1 if cnt & (cnt-1) == 0 else 0
        return self.pseudoPalindromicPaths(root.left, cnt) + self.pseudoPalindromicPaths(root.right, cnt)
