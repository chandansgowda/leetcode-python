class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return int(len(nums)*(len(nums)+1)/2 - sum(nums))


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s = sum(nums)
        n = len(nums)
        return int(n*(n+1)/2 - s)
