class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [[0]*(n+1) for _ in range(n+1)]

        for i in range(n):
            dp[n-1][i] = triangle[n-1][i]
            
        for i in range(n-1,-1,-1):
            for j in range(i,-1,-1):
                down = triangle[i][j] + dp[i+1][j]
                diagonal = triangle[i][j] + dp[i+1][j+1]
                dp[i][j] = min(down,diagonal)

        return dp[0][0]



class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        def f(i,j,dp):
            if i==n-1:
                return triangle[i][j]
            if dp[i][j]!=-1:
                return dp[i][j]
            down = triangle[i][j] + f(i+1,j,dp)
            diagonal = triangle[i][j] + f(i+1,j+1,dp)
            dp[i][j] = min(down,diagonal)
            return dp[i][j]
            
        dp = [[-1]*n for _ in range(n)]
        return f(0,0,dp)


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        def f(i,j):
            if i==n-1:
                return triangle[i][j]
            down = triangle[i][j] + f(i+1,j)
            diagonal = triangle[i][j] + f(i+1,j+1)
            return min(down,diagonal)
        return f(0,0)
