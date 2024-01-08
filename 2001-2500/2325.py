class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        d = {}
        ans = ""
        n = 0 
        for i in key:
            if i not in d and i != " ":
                d[i]=chr(ord('a')+n)
                n += 1
        for i in message:
            if i in d:
                ans += d[i]
            elif i == " ":
                ans += " "
        
        return ans

