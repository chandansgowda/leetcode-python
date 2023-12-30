class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        res = 0
        for i in range(len(nums)):
            if str(bin(i)).count("1")==k:
                res+=nums[i]
        return res
