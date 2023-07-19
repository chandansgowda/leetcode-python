class Solution:
    def reverseWords(self, s: str) -> str:
        res = []
        temp = ""
        for c in s:
            if c!=" ":
                temp += c
            else:
                if temp!="":
                    res.append(temp)
                    temp = ""
        if temp!="":
            res.append(temp)
        return " ".join(res[::-1])
