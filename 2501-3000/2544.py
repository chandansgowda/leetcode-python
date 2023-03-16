class Solution:
    def alternateDigitSum(self, n: int) -> int:
        res = 0
        sign = 1
        for sn in str(n):
            res += (int(sn)*sign)
            if sign==1:
                sign = -1
            else:
                sign = 1
        return res

