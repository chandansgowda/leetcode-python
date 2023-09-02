class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        def helper(i, t):
            if i==-1:
                if t==0:
                    return 1
                return 0
            if (i,t) in memo:
                return memo.get((i,t))
            pos = helper(i-1,t-nums[i])
            neg = helper(i-1,t+nums[i])
            memo[(i,t)] = pos+neg
            return memo[(i,t)]

        return helper(len(nums)-1,target)



class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def helper(i, t):
            if i==-1:
                if t==0:
                    return 1
                return 0
            pos = helper(i-1,t-nums[i])
            neg = helper(i-1,t+nums[i])
            return pos+neg
        return helper(len(nums)-1,target)
            
        
