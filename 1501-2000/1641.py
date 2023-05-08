class Solution:
    def countVowelStrings(self, n: int) -> int:
        dp = [1]*5
        while n>0:
            for i in reversed(range(0,4)):
                dp[i]+=dp[i+1]
            n-=1
        return dp[0]
