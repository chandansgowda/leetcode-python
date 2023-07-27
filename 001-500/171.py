class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        for i,c in enumerate(reversed(columnTitle)):
            res += (26**i) * (ord(c) - ord('A') + 1)
        return res


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res,count = 0,len(columnTitle)-1
        for c in columnTitle:
            res += (26**count) * (ord(c) - ord('A') + 1)
            count-=1
        return res
