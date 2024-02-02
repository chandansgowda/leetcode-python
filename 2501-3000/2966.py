class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        n = len(nums)
        if n % 3 != 0:
            return []

        nums.sort()

        result = []
        group_index = 0
        for i in range(0, n, 3):
            if i + 2 < n and nums[i + 2] - nums[i] <= k:
                result.append([nums[i], nums[i + 1], nums[i + 2]])
                group_index += 1
            else:
                return []
        return result


class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        ans=[]
        n=len(nums)//3
        for i in range(n):
            if nums[3*i+2]-nums[3*i]> k: 
                return []
            ans.append(nums[3*i:3*i+3])
        return ans
        
