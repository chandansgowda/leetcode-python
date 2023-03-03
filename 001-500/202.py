class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n!=1:
            n = sum(int(x)**2 for x in str(n))
            if n in seen:
                return False
            seen.add(n)
            
        return True


class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n not in seen:
            seen.add(n)
            n = sum(int(x)**2 for x in str(n))
            
        return n==1
