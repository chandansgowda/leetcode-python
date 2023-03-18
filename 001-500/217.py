class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                return True
        return False

    
    
    
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return sorted(nums)!=sorted(list(set(nums)))

    
   
    
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for num in nums:
            if num in d:
                return True
            else:
                d[num]=1
        return False
    
    
    
    
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set()
        for num in nums:
            if num in s:
                return True
            else:
                s.add(num)
        return False
