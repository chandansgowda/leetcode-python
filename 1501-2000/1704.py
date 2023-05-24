class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        v = "aeiouAEIOU"
        count = 0
        for i in range(len(s)):
            if s[i] in v:
                if i<=len(s)//2-1:
                    count += 1
                else:
                    count -= 1

        return count==0
