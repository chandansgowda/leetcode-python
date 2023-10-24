class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
                for num in nums:
                    val = abs(num)-1
                    nums[val] = -abs(nums[val])
                return [i+1 for i in range(len(nums)) if nums[i]>0]
        
