class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        ans = 0
        for word in words:
            if s.find(word)==0:
                ans += 1
        return ans
        
class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        ans = 0
        for word in words:
            if s[:len(word)]==word:
                ans += 1
        return ans
        
