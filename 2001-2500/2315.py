class Solution:
    def countAsterisks(self, s: str) -> int:
        res = 0
        nt = 0
        for c in s:
            if c=="|":
                nt+=1
            elif nt%2==0:
                res += c=="*"
        return res



class Solution:
    def countAsterisks(self, s: str) -> int:
        l = s.split("|")
        res = 0
        for a in l[0::2]:
            res += a.count("*")
        return res
