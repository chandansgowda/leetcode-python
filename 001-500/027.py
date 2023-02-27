class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        fast=slow=count=0
        while fast<len(nums):
            if nums[fast]==val:
                fast+=1
            else:
                count+=1
                nums[slow]=nums[fast]
                fast+=1
                slow+=1
        return count
