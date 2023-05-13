class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        x = n&1
        n >>= 1
        while n!=0:
            if x^(n&1):
                x = n&1
                n >>= 1
            else:
                return False
        return True
