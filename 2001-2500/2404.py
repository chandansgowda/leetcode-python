from collections import defaultdict
class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        d = defaultdict(lambda: 0)
        val,freq=-1,-float('inf')
        for num in nums:
            if num%2==0:
                d[num]+=1
                if d[num]>freq or (d[num]==freq and num<val):
                    val = num
                    freq = d[num]
        return val
