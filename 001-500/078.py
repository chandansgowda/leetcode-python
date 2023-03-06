class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.backtrack(nums,[], res)
        return res

    def backtrack(self,nums,path,res):
        res.append(path)
        for i in range(len(nums)):
            self.backtrack(nums[i+1:], path+[nums[i]], res)
