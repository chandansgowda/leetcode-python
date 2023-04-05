class Solution:
    def repeatedCharacter(self, s: str) -> str:
        seen = []
        for c in s:
            if c in seen:
                return c
            else:
                seen.append(c)
