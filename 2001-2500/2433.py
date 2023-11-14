class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        prev = pref[0]
        for i in range(1,len(pref)):
            pref[i]^=prev
            prev^=pref[i]
        return pref
        
