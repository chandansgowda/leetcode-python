# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def recf(nums,start,end):
            while start<=end:
                mid = (start+end)>>1
                node = TreeNode(nums[mid])
                node.left = recf(nums, start, mid-1)
                node.right = recf(nums, mid+1, end)
                return node
        return recf(nums,0,len(nums)-1)
