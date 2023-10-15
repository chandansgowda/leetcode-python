class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        res = list(words[0])
        for word in words:
            newRes = []
            for c in word:
                if c in res:
                    newRes.append(c)
                    res.remove(c)
            res = newRes
        return res
        
