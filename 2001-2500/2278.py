class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        d = {}
        for c in s:
            if c in d:
                d[c]+=1
            else:
                d[c]=1
        try:
            count = d[letter]
            return int((count/len(s))*100)
        except:
            return 0
