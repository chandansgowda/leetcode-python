class Solution:
    def countElements(self, nums: List[int]) -> int:
        if len(nums)<3:
            return 0
        nums.sort()
        ans = len(nums) - nums.count(nums[0])
        if nums[0]!=nums[-1]:
            ans -= nums.count(nums[-1])
        return ans
        
