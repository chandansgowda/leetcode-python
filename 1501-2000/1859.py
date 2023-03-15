class Solution:
    def sortSentence(self, s: str) -> str:
        l = s.split()
        l.sort(key=lambda x: x[-1])
        for i in range(len(l)):
            l[i] = l[i][:-1]
        return " ".join(l)
