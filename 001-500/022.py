class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(l,r,s):
            if len(s)==n*2:
                res.append(s)
                return
            
            if l<n:
                dfs(l+1,r,s+'(')
            if r<l:
                dfs(l,r+1,s+')')

        res = []
        dfs(0,0,'')
        return res
        
