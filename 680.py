class Solution:
    def validPalindrome(self, s: str) -> bool:
        l,r = 0,len(s)-1
        flag = 0
        while l<r:
            if s[l]!=s[r]:
                x,y = s[l:r], s[l+1:r+1]
                return x==x[::-1] or y==y[::-1]
            l,r=l+1,r-1
        return True
