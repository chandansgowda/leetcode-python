class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if set(word1)!=set(word2):
            return False
        d1, d2 = defaultdict(int), defaultdict(int)
        for c in word1:
            d1[c]+=1
        for c in word2:
            d2[c]+=1
        return sorted(d1.values())==sorted(d2.values())
        
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        return set(word1) == set(word2) and Counter(Counter(word1).values()) == Counter(Counter(word2).values())
        
