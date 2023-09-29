class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        strings = set()
        ans = 0
        for w in words:
            if w in strings:
                ans += 1
            else:
                strings.add(w[::-1])
        return ans
