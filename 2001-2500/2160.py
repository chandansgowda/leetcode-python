class Solution:
    def minimumSum(self, num: int) -> int:
        n = sorted(str(num))
        return int(n[0] + n[2]) + int(n[1] + n[3])

    
class Solution:
    def minimumSum(self, num: int) -> int:
        a,b,c,d = sorted(str(num))
        return int(a+c) + int(b+d)
