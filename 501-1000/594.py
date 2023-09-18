class Solution:
    def findLHS(self, nums: List[int]) -> int:
      c = collections.Counter(nums)
      res = 0
      for x in c:
        if x+1 in c:
          res = max(res, c[x]+c[x+1])
      return res
