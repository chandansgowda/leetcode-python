class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i, c in enumerate(min(strs)):
            if c != max(strs)[i]:
                return max(strs)[:i]
        return min(strs)
