class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s = 0
        p = 1
        while n>0:
            i = n%10
            n //= 10
            s += i
            p *= i
        return p-s
