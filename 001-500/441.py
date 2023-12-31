class Solution:
    def arrangeCoins(self, n: int) -> int:
        l = 0
        r = n
        while l<=r:
            m = (l+r)>>1
            coins_until_m = (m*(m+1))>>1
            if coins_until_m == n:
                return m
            elif n < coins_until_m:
                r = m-1
            else:
                l = m+1
        return r
        
