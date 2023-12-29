class Solution:
    def toHex(self, num: int) -> str:
        if num==0: return '0'
        mp = '0123456789abcdef' 
        ans = ''
        for i in range(8):
            n = num & 15   
            c = mp[n]         
            ans = c + ans
            num = num >> 4
        return ans.lstrip('0')


class Solution:
    def toHex(self, num: int) -> str:
        s, res, num = '0123456789abcdef', '', num & 0xFFFFFFFF        
        while num:
            res += s[num % 16]
            num >>= 4
        return res[::-1] or '0'
        
        
