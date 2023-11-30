class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        n = s.count("1")-1
        ans = "1"*n
        ans += "0"*(len(s)-n-1)
        ans += "1"
        return ans
