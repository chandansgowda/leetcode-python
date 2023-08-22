class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0]*(len(text2)+1) for _ in range(len(text1)+1)]
        for i in range(len(text1)):
            for j in range(len(text2)):
                if text1[i]==text2[j]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])

        return dp[len(text1)-1][len(text2)-1]


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def helper(i,j, dp):
            if i<0 or j<0:
                return 0
            
            if dp[i][j]!=-1:
                return dp[i][j]

            if text1[i]==text2[j]:
                return 1 + helper(i-1,j-1,dp)

            dp[i][j] = max(helper(i-1,j,dp),helper(i,j-1,dp))
            return dp[i][j]

        dp = [[-1]*len(text2) for _ in range(len(text1))]
        return helper(len(text1)-1,len(text2)-1,dp)


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def helper(i,j):
            if i<0 or j<0:
                return 0

            if text1[i]==text2[j]:
                return 1 + helper(i-1,j-1)

            return max(helper(i-1,j),helper(i,j-1))

        return helper(len(text1)-1,len(text2)-1)
