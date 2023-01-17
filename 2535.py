class Solution(object):
    def differenceOfSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        es = sum(nums)
        ds = 0
        for num in nums:
            while num>0:
                ds+=num%10
                num//=10
        return abs(es-ds)
