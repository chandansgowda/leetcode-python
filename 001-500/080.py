class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        fast=slow=0
        while fast<len(nums):
            if slow<2 or nums[fast]!=nums[slow-2] :
                nums[slow]=nums[fast]
                slow +=1
            fast+=1
        return slow
