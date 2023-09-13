class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        dp = [[0]*m for _ in range(n)]

        for i in range(m):
            if obstacleGrid[0][i]==1:
                break
            dp[0][i]=1
        for j in range(n):
            if obstacleGrid[j][0]==1:
                break
            dp[j][0]=1

        for i in range(1,n):
            for j in range(1,m):
                if obstacleGrid[i][j]==1:
                    dp[i][j] = 0
                elif i==0 and j==0:
                    dp[i][j] = 1
                else:
                    left,up = 0,0
                    if i>0:
                        up = dp[i-1][j]
                    if j>0:
                        left = dp[i][j-1]
                    dp[i][j] = up + left
                
        return dp[n-1][m-1]


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        def helper(i,j,dp):
            if obstacleGrid[i][j]==1:
                return 0
            elif i==0 and j==0:
                return 1
            elif i<0 or j<0:
                return 0
            l = helper(i-1,j,dp)
            r = helper(i,j-1,dp)
            dp[i][j] = l+r
            return dp[i][j]

        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        dp = [[-1]*m for _ in range(n)]
        return helper(n-1,m-1,dp)
