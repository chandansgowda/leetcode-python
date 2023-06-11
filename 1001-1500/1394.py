class Solution:
    def findLucky(self, arr: List[int]) -> int:
        d = defaultdict(int)
        for num in arr:
            d[num]+=1
        for key,val in sorted(d.items(), reverse=True):
            if key==val:
                return key
        return -1
