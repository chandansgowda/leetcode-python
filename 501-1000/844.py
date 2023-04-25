class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stk1 = []
        stk2 = []

        for c in s:
            if c=="#":
                if len(stk1):
                    stk1.pop()
            else:
                stk1.append(c)

        for c in t:
            if c=="#":
                if len(stk2):
                    stk2.pop()
            else:
                stk2.append(c)

        return stk1==stk2
