class Solution:
    def frequencySort(self, s: str) -> str:
        m = Counter(s)
        l = sorted(m.items(), key = lambda x: x[1], reverse=True)
        ans = ""
        for c,count in l:
            ans += c*count
        return ans
        
            
