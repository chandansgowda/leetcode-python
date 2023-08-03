class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        maxSum,minSum = nums[0],nums[0]
        curMax,curMin = 0,0
        totalSum = 0
        for num in nums:
            curMax = max(curMax+num,num)
            curMin = min(curMin+num,num)
            totalSum += num
            maxSum = max(maxSum,curMax)
            minSum = min(minSum,curMin)
        return max(totalSum-minSum,maxSum) if maxSum>0 else maxSum
