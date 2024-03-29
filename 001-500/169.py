class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        maj = None
        for num in nums:
            if count==0:
                maj = num
            count += 1 if num==maj else -1
        return maj



class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n2 = len(nums)//2
        d = {}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for i,j in d.items():
            if j>n2:
                return i



from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n2 = len(nums)//2
        d = defaultdict(int)
        for i in nums:
            d[i]+=1
        for i,j in d.items():
            if j>n2:
                return i
            
            
            
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return sorted(nums)[len(nums)//2]

            
