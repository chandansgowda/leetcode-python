class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c1,c2,cd1,cd2=0,0,0,1
        for num in nums:
            if num==cd1:
                c1+=1
            elif num==cd2:
                c2+=1
            elif c1==0:
                c1,cd1=1,num
            elif c2==0:
                c2,cd2=1,num
            else:
                c1-=1
                c2-=1
        if cd1==cd2:
            return [cd1]
        return [n for n in (cd1,cd2) if nums.count(n)>len(nums)//3]


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
