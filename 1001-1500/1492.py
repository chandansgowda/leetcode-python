class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        i = 1
        while k>0:
            if i>n:
                return -1
            if n%i==0:
                k-=1
            i+=1
        return i-1
