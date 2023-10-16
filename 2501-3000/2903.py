class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        ans = [-1,-1]
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if abs(i-j)>=indexDifference and abs(nums[i]-nums[j]) >= valueDifference:
                    ans[0], ans[1] = i,j
                    break
        return ans
        
