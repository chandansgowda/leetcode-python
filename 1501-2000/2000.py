class Solution:
    def reversePrefix(self, w: str, ch: str) -> str:
        j = -1
        word = list(w)
        for i in range(len(word)):
            if word[i]==ch:
                j = i
                break
        i = 0
        while i<j:
            word[i],word[j]=word[j],word[i]
            i+=1
            j-=1
        return "".join(word)
