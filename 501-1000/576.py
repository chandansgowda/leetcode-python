# Recursive - TLE
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        R = m
        C = n
        M = 10**9 + 7

        def dfs(r,c,maxMove):
            if (r<0 or r==R or c<0 or c==C):
                return 1
            if maxMove==0:
                return 0
            return (
                (dfs(r+1,c,maxMove-1) + dfs(r-1,c,maxMove-1)) % M
                +
                (dfs(r,c+1,maxMove-1) + dfs(r,c-1,maxMove-1)) % M
            ) % M
        
        return dfs(startRow, startColumn, maxMove)
