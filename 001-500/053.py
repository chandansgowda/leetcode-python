class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0]*len(nums)
        for idx,num in enumerate(nums):
            dp[idx] = max(dp[idx-1]+num, num)
        return max(dp)


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum = 0
        maxSum = nums[0]
        for num in nums:
            if curSum<0:
                curSum = 0
            curSum+=num
            maxSum = max(curSum,maxSum)
        return maxSum
