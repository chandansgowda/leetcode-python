from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d = defaultdict(int)
        n = len(nums)//3
        res = []
        for num in nums:
            d[num]+=1
        for i,j in d.items():
            if j>n:
                res.append(i)

        return res
    
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d = {}
        n = len(nums)//3
        res = []
        for num in nums:
            if num not in d:
                d[num]=1
            else:
                d[num]+=1
        for i,j in d.items():
            if j>n:
                res.append(i)

        return res
