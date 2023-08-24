class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        dp = [[0]*(m+1) for _ in range(n+1)]
        for i in range(n):
            for j in range(m):
                if i==0 and j==0:
                    dp[i][j]=grid[0][0]
                else:
                    up = grid[i][j] + dp[i-1][j] if i>0 else 99999
                    left = grid[i][j] + dp[i][j-1] if j>0 else 99999
                    dp[i][j] = min(up,left)
        return dp[n-1][m-1]


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        def f(i,j, dp):
            if i==0 and j==0:
                return grid[0][0]
            elif i<0 or j<0:
                return 9999999
            elif dp[i][j]!=-1:
                return dp[i][j]
            up = grid[i][j] + f(i-1,j,dp)
            left = grid[i][j] + f(i,j-1,dp)
            dp[i][j] = min(up,left)
            return dp[i][j]
        
        dp = [[-1]*m for _ in range(n)]
        return f(n-1,m-1,dp)

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        def f(i,j):
            if i==0 and j==0:
                return grid[0][0]
            elif i<0 or j<0:
                return 9999999
            up = grid[i][j] + f(i-1,j)
            left = grid[i][j] + f(i,j-1)
            return min(up,left)
        
        return f(n-1,m-1)
