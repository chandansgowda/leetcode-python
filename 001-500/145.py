# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = []

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        self.postorderTraversal(root.left)
        self.postorderTraversal(root.right)
        self.ans.append(root.val)
        return self.ans
        
