class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        maxVal = 0
        charHistory = {}
        
        for i in range(len(s)):
            if s[i] in charHistory and start<=charHistory[s[i]]:
                start = charHistory[s[i]]+1
            else:
                maxVal = max(maxVal,i-start+1)
            charHistory[s[i]]=i
        
        return maxVal
