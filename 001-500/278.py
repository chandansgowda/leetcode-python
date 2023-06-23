# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l,h=1,n
        ans = 1
        while l<=h:
            m = (l+h)>>1
            if isBadVersion(m)==False:
                l = m+1
            else:
                h = m-1
                ans = m
        return ans
