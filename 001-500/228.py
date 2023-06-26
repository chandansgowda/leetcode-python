class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        i = 0
        while i<len(nums):
            beg = nums[i]

            while i+1<len(nums) and nums[i]==nums[i+1]-1:
                i+=1

            end = nums[i]

            if beg==end:
                res.append(str(beg))
            else:
                res.append(str(beg) + "->" + str(end))
            i+=1

        return res
