class Solution:
    def addDigits(self, num: int) -> int:
        s = str(num)
        while len(s)!=1:
            res = 0
            for n in s:
                res+=int(n)
            s = str(res)
        return int(s)
