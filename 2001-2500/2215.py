class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        x = set(nums1) - set(nums2)
        y = set(nums2) - set(nums1)
        return [list(x), list(y)]
