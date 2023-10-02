class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        d = [x for x in arr if arr.count(x)==1]
        return "" if k>len(d) else d[k-1]
