class Solution:
    def convertToTitle(self, c: int) -> str:
        a = [chr(x) for x in range(ord("A"), ord("Z")+2)]
        res = ""
        while c>0:
          c -= 1
          res += a[c%26]
          c //= 26

        return res[::-1]
    


class Solution:
    def convertToTitle(self, c: int) -> str:
        a = ['0','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        res = ""
        while c>0:
          c -= 1
          res += a[c%26+1]
          c //= 26

        return res[::-1]
