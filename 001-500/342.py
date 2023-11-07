class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n==1: return True
        if n<=0: return False
        logb4 = math.log(n)/math.log(4)
        return logb4==int(logb4)
        
