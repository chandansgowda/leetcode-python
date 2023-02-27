class Solution:
    def romanToInt(self, s: str) -> int:
        smap = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        res = 0
        i = 0
        while i<len(s):
            if i<len(s)-1 and smap[s[i]] < smap[s[i+1]]:
                res = res + smap[s[i+1]] - smap[s[i]]
                i+=1
            else:
                res += smap[s[i]]
            i+=1
        return res
            
