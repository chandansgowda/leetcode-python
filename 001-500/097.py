class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l1,l2,l3 = len(s1),len(s2),len(s3)
        if l1+l2!=l3:
            return False

        dp = [[-1]*(l2+1) for _ in range(l1+1)]
        
        def helper(i,j,k):
            if k==l3:
                return True
            
            if dp[i][j]!=-1:
                return dp[i][j]
            
            ans = False
            if i<l1 and s1[i]==s3[k]:
                ans = ans or helper(i+1,j,k+1)
            
            if j<l2 and s2[j]==s3[k]:
                ans = ans or helper(i,j+1,k+1)
            
            dp[i][j] = ans
            return ans

        return helper(0,0,0)
        


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l1,l2,l3 = len(s1),len(s2),len(s3)
        if l1+l2!=l3:
            return False
        
        def helper(i,j,k):
            if k==l3:
                return True
            
            ans = False
            if i<l1 and s1[i]==s3[k]:
                ans = ans or helper(i+1,j,k+1)
            
            if j<l2 and s2[j]==s3[k]:
                ans = ans or helper(i,j+1,k+1)
            
            return ans

        return helper(0,0,0)
