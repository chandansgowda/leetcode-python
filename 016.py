class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = nums[0]+nums[1]+nums[2]
        for i in range(len(nums)):
            s,e=i+1,len(nums)-1
            while s<e:
                sm = nums[s]+nums[e]+nums[i]
                if sm==target:
                    return target
                if abs(sm-target)<abs(res-target):
                    res=sm
                if sm<target:
                    s+=1
                elif sm>target:
                    e-=1
                
        return res
