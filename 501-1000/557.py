class Solution:
    def reverseWords(self, s: str) -> str:
        l = s.split(" ")
        l = [word[::-1] for word in l]
        return " ".join(l)
