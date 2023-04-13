class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        d = {}
        for c in s:
            if c in d:
                d[c]+=1
            else:
                d[c]=1
        x = d[s[0]]
        for k,v in d.items():
            if v!=x:
                return False
        return True
