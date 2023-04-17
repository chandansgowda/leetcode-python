class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        ans = -1
        for c in s:
            if c=="(":
                stack.append("(")
                ans = max(ans,len(stack))
            elif c==")":
                stack.pop()
        return ans
