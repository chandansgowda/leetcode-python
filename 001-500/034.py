class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binSearch(leftBias):
            l,h=0,len(nums)-1
            index = -1
            while l<=h:
                m = (l+h)>>1
                if nums[m]<target:
                    l = m+1
                elif nums[m]>target:
                    h = m-1
                else:
                    index = m
                    if leftBias:
                        h = m-1
                    else:
                        l = m+1
            return index
        return [binSearch(True), binSearch(False)]
