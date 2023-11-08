class Solution:
    def pivotInteger(self, n: int) -> int:
        tsum = n*(n+1) // 2
        l,r = 1,n+1
        while l<r:
            m = (l+r)//2
            lsum = m*(m+1)//2
            rsum = tsum-lsum-m
            if lsum<rsum:
                l=m+1
            else:
                r=m
        return l if l*(l-1)//2==tsum-(l+1)*l//2 else -1        
