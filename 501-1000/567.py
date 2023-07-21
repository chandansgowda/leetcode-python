from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d1 = defaultdict(int)
        d2 = defaultdict(int)
        for c in s1:
            d1[c]+=1

        for c in s2[:len(s1)]:
            d2[c]+=1
        
        left = 0
        for right in range(len(s1),len(s2)):
            if d1.items()==d2.items():
                return True
            if d2[s2[left]]==1:
                del d2[s2[left]]
            else:
                d2[s2[left]]-=1
            d2[s2[right]]+=1
            left += 1

        if d1.items()==d2.items():
                return True
        
        return False
            
