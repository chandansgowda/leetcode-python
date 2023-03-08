class Solution:
    def addDigits(self, num: int) -> int:
        while len(str(num))!=1:
            res = 0
            while num!=0:
                num,c=divmod(num,10)
                res+=c
            num = res
        return num

    
    
class Solution:
    def addDigits(self, num: int) -> int:
        s = str(num)
        while len(s)!=1:
            res = 0
            for n in s:
                res+=int(n)
            s = str(res)
        return int(s)
