class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        ans = 0
        s = set(nums)
        for num in nums:
            if num+diff in s and num+2*diff in s:
                ans += 1
        return ans
        
