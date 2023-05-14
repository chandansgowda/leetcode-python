class Solution:
    def findComplement(self, num: int) -> int:
        return ((1 << num.bit_length())-1) ^ num
