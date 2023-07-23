class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l,r,total=0,0,0
        ans = float('inf')

        while r<len(nums):
            total += nums[r]
            while total>=target:
                ans = min(ans,r-l+1)
                total-=nums[l]
                l+=1
            r+=1

        return 0 if ans==float('inf') else ans
