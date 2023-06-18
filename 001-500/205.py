class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        l1 = []
        l2 = []
        for c in s:
            l1.append(s.index(c))
        for c in t:
            l2.append(t.index(c))
        return l1==l2
