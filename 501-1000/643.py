class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l,r=0,k-1
        curSum = sum(nums[:k])
        maxSum = curSum
        while r<len(nums)-1:
            curSum-=nums[l]
            l+=1
            r+=1
            curSum+=nums[r]
            maxSum = max(maxSum, curSum)
        return maxSum/k
        
