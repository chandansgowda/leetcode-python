from heapq import * 

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = []
        res = 0
        for num in nums:
            heappush(h,num)
            if len(h)>k:
                heappop(h)
        return heappop(h)


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapify(nums)
        return nlargest(k,nums)[-1]
