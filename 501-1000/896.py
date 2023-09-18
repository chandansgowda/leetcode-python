class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums)<=2:
            return True

        isGreat = False
        isLess = False
        for i in range(1,len(nums)):
            if nums[i]<nums[i-1]:
                isGreat = True
            if nums[i]>nums[i-1]:
                isLess = True
            if isGreat and isLess:
                return False
        
        return True
        
