class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d = {'(':')', '[':']', '{':'}'}
        stk = []

        for c in s:
            if c in d:
                stk.append(c)
            elif len(stk)>0 and c==d[stk[-1]]:
                stk.pop()
            else:
                return False

        return not bool(len(stk))
