class Solution:
    def makeGood(self, s: str) -> str:
        stk = []
        for c in s:
            if stk:
                if abs(ord(stk[-1])-ord(c))==32:
                    stk.pop()
                else:
                    stk.append(c)
            else:
                stk.append(c)

        return "".join(stk)


class Solution:
    def makeGood(self, s: str) -> str:
        stk = []
        for c in s:
            if c.isupper() and stk and stk[-1]==c.lower():
                stk.pop()
            elif c.islower() and stk and stk[-1]==c.upper():
                stk.pop()
            else:
                stk.append(c)

        return "".join(stk)
