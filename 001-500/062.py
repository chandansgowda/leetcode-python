class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*m for _ in range(n)]
        for i in range(m):
            dp[0][i]=1
        for j in range(n):
            dp[j][0]=1

        for i in range(1,n):
            for j in range(1,m):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
                
        return dp[n-1][m-1]

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
