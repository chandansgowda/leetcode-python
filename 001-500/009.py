#Without conversion to string
class Solution:
    def isPalindrome(self, x: int) -> bool:
        revx = 0
        temp = x
        while temp>0:
            revx = revx*10 + (temp%10)
            temp = temp//10
        if (x==revx): return True


#Converting to string and then checking
class Solution:
    def isPalindrome(self, x: int) -> bool:
        xstr = str(x)
        return xstr==xstr[::-1]
