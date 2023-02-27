class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []

        for i in range(0,len(nums),2):
            f = nums[i]
            v = nums[i+1]
            for i in range(f): res.append(v)

        return res
