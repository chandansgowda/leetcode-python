class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)-len(needle)+1):
            flag = True
            for j in range(len(needle)):
                if haystack[i+j]!=needle[j]:
                    flag = False
            if flag: return i
        return -1
      
      
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
