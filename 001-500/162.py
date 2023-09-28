class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l,h=0,len(nums)-1
        while l<=h:
            m = (l+h)>>1
            if m>0 and nums[m]<nums[m-1]:
                h = m-1
            elif m<len(nums)-1 and nums[m]<nums[m+1]:
                l = m+1
            else:
                return m
