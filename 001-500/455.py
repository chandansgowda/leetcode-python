class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort()
        g.sort()
        i,j=0,0
        while i<len(g) and j<len(g):
            if s[j]>=g[i]:
                i+=1
            j+=1
        return i
        
