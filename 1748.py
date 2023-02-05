class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = {}

        for num in nums:
            if num in m:
                m[num]+=1
            else:
                m[num]=1

        count = 0
        for num in nums:
            if m[num]==1:
                count+=num

        return count
