class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        ans = 0
        for i in range(1,n+1):
            if i%m==0:
                ans-=i
            else:
                ans+=i
        return ans
        
