class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        v = "aeiouAEIOU"
        count = 0
        for i in range(len(s)):
            if s[i] in v:
                if i<=len(s)//2-1:
                    count += 1
                else:
                    count -= 1

        return count==0


class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        def is_vowel(x):
            v = "aeiouAEIOU"
            return x in v

        c = 0
        for i in range(len(s)//2):
            if is_vowel(s[i]):
                c+=1
            if is_vowel(s[len(s)-i-1]):
                c-=1
            
        return c==0


        
