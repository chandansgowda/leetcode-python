class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        while n>=5:
            count += (n//5)
            n = n//5
        return count
