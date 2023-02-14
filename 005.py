class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        start = 0
        end = 0
        m = 0

        for i in range(len(s)):

            #odd palindromes
            l,r=i,i
            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l+1)>m:
                    start = l
                    end = r
                    m = r-l+1
                l-=1
                r+=1

            #even palindromes
            l,r=i,i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l+1)>m:
                    start = l
                    end = r
                    m = r-l+1
                l-=1
                r+=1

        return s[start:end+1]
