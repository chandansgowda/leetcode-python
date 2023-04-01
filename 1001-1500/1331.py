class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        arrSorted = sorted(set(arr))
        d = {}
        for i in range(len(arrSorted)):
            d[arrSorted[i]] = i+1
        res = []
        for num in arr:
            res.append(d[num])
        return res
