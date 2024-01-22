class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        return [sum(nums)-sum(set(nums)), int(len(nums)*(len(nums)+1)/2-sum(set(nums)))]

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        x = (len(nums)*(len(nums)+1))//2
        s = sum(set(nums))
        return [sum(nums)-s, x-s]
        
