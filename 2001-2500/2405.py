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
