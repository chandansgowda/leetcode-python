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

        
