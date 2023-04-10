class Solution:
    def countAsterisks(self, s: str) -> int:
        l = s.split("|")
        res = 0
        for a in l[0::2]:
            res += a.count("*")
        return res
