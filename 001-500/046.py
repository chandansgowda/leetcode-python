class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        self.backtrack(nums,[],res)
        return res

    def backtrack(self, nums, path, res):
        if len(nums)==0:
            res.append(path)
            return
        for i in range(len(nums)):
            self.backtrack(nums[:i]+nums[i+1:], path+[nums[i]], res)
