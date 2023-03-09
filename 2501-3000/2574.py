class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        res = [nums[0]]
        total = nums[-1]
        for i in range(1,len(nums)):
            res.append(res[i-1]+nums[i])

        i = len(nums)-1
        while i>=0:
            if i!=len(nums)-1:
                total+=nums[i]
            res[i] = abs(res[i]-total)
            i-=1
        

        return res

            
