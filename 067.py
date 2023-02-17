class Solution:
    def addBinary(self, a: str, b: str) -> str:
        c = 0
        la = len(a)-1
        lb = len(b)-1
        res = ""

        while la>=0 or lb>=0:
            s = c
            if la>=0 : s += ord(a[la]) - ord('0')
            if lb>=0 : s += ord(b[lb]) - ord('0')
            la,lb = la-1, lb-1
            c = 1 if s>1 else 0
            res += str(s%2)

        if c==1:
            res+="1"

        return res[::-1]
