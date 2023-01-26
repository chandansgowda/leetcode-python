class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        m = {}
        numsSorted = sorted(nums)
        for i in range(len(numsSorted)):
            if numsSorted[i] not in m.keys():
                m[numsSorted[i]]=i
        return [m[x] for x in nums]
