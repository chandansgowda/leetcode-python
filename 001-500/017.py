class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = { "2": "abc", "3": "def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        res = []
        if len(digits)==0:
            return res
        self.dfs(digits,0,dic,'', res)
        return res

    def dfs(self,digits,index,dic,path,res):
        if index>=len(digits):
            res.append(path)
            return
        s = dic[digits[index]]
        for c in s:
            self.dfs(digits,index+1,dic,path+c,res)
