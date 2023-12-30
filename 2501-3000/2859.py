class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        res = 0
        for i in range(len(nums)):
            if str(bin(i)).count("1")==k:
                res+=nums[i]
        return res


class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        return sum([nums[i] for i in range(len(nums)) if bin(i)[2:].count('1')==k])
