class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s)-1
        while s[i]==" ":
            i -= 1
        count = 0
        while i!=-1 and s[i]!=" ":
            i -= 1
            count += 1
        return count
