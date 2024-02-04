from collections import defaultdict

class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        d = defaultdict(int)
        for num in nums:
            d[num]+=1
        res = []
        while d:
            row = []
            keys = list(d.keys())
            for k in keys:
                row.append(k)
                d[k]-=1
                if d[k]==0:
                    del d[k]
            res.append(row)
        return res
        
