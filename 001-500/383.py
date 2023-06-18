class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d = defaultdict(int)

        i = 0
        while i<len(ransomNote) or i<len(magazine):
            if i<len(ransomNote):
                d[ransomNote[i]]-=1
            if i<len(magazine):
                d[magazine[i]]+=1
            i+=1

        for i in d.values():
            if i<0:
                return False

        return True
