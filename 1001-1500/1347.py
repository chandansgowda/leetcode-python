class Solution:
    def minSteps(self, s: str, t: str) -> int:
        ds, dt = defaultdict(int), defaultdict(int)
        for c in s:
            ds[c]+=1
        for c in t:
            dt[c]+=1
        ans = 0
        for k in ds.keys():
            ans += (ds[k]-dt[k]) if ds[k]>dt[k] else 0
        return ans
        
