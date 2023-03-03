class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n not in seen:
            seen.add(n)
            n = sum(int(x)**2 for x in str(n))
            
        return n==1
