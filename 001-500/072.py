class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        def helper(i,j,dp):
            if i==0:
                return j
            if j==0:
                return i
            if dp[i][j]!=-1:
                return dp[i][j]
            if word1[i-1]==word2[j-1]:
                dp[i][j] = helper(i-1,j-1,dp)
            else:
                insertOp = helper(i-1,j,dp)
                deleteOp = helper(i,j-1,dp)
                swapOp = helper(i-1,j-1,dp)
                dp[i][j] = min(insertOp,deleteOp,swapOp) + 1
            return dp[i][j]
        
        dp = [[-1]*(len(word2)+1) for _ in range(len(word1)+1)]
        return helper(len(word1),len(word2),dp)



class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        def helper(i,j):
            if i==0:
                return j
            if j==0:
                return i
            if word1[i-1]==word2[j-1]:
                return helper(i-1,j-1)
            else:
                insertOp = helper(i-1,j)
                deleteOp = helper(i,j-1)
                swapOp = helper(i-1,j-1)
                return min(insertOp,deleteOp,swapOp) + 1
        
        return helper(len(word1),len(word2))

        
