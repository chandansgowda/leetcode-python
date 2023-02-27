class Solution(object):
    def countKDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count=0
        m = {}

        for num in nums:
            if num in m:
                m[num]+=1
            else:
                m[num]=1

        for num in nums:
            if num+k in nums:
                count+=m[num+k]

        return count
