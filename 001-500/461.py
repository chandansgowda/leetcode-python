class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        hd = 0
        z = x^y
        while z:
            if z%2==1:
                hd += 1
            z = z>>1
        return hd
        

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x^y).count('1')
