class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxval = max(nums)
        nums.remove(maxval)
        return (maxval-1)*(max(nums)-1)


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                ans = max(ans, (nums[i]-1)*(nums[j]-1))
        return ans
