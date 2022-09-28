class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            r = target - nums[i]
            if r in d: return [d[r],i]
            d[nums[i]]=i
            
        
