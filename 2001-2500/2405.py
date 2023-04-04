class Solution:
    def partitionString(self, s: str) -> int:
        seen = ""
        res = 1
        for c in s:
            if c in seen:
                res += 1
                seen = ""
            seen += c

        return res



class Solution:
    def partitionString(self, s: str) -> int:
        i = 0
        seen = ""
        c = 0
        while i<len(s):
            if s[i] in seen:
                seen = ""
                c += 1
            else:
                seen += s[i]
                i+=1
        return c + 1
