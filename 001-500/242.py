class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False

        d = {}

        for i in range(len(s)):
            if s[i] in d:
                d[s[i]] += 1
            else:
                d[s[i]] = 1

        for i in range(len(t)):        
            if t[i] in d:
                d[t[i]] -= 1
            else:
                return False

        for v in d.values():
            if v>0:
                return False
        return True
