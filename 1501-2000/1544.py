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
