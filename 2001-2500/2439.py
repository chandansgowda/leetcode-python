class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        s = 0
        maxv = float('-inf')
        for i in range(len(nums)):
            s += nums[i]
            maxv = max(maxv, math.ceil(s/(i+1)))
        return maxv
        
