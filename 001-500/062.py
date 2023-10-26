class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def helper(i,j,dp):
            if i==0 and j==0:
                return 1
            elif i<0 or j<0:
                return 0
            elif dp[i][j]!=-1:
                return dp[i][j]
            l = helper(i-1,j,dp)
            r = helper(i,j-1,dp)
            dp[i][j] = l+r
            return dp[i][j]
        
        dp = [[-1]*m for _ in range(n)]
        return helper(n-1,m-1,dp)

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def helper(i,j):
            if i==0 and j==0:
                return 1
            elif i<0 or j<0:
                return 0
            l = helper(i-1,j)
            r = helper(i,j-1)
            return l+r
        
        return helper(n-1,m-1)
