class Solution:
    def toLowerCase(self, s: str) -> str:
        res = ""
        for c in s:
            if c.isupper():
                res += chr(ord(c)+32)
            else:
                res += c
        return res
      
      
 class Solution:
    def toLowerCase(self, s: str) -> str:
        return s.lower()
