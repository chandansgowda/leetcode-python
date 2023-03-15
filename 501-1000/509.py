class Solution:
    def fib(self, n: int) -> int:
        a,b=0,1
        for _ in range(n-1):
            a,b=b,a+b
        return b if n!=0 else 0
