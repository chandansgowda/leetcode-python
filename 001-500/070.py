class Solution:
    def climbStairs(self, n: int) -> int:
        fib = [0,1]
        for i in range(2,n+2):
            fib.append(fib[i-1]+fib[i-2])
        return fib[n+1]

class Solution:
    def climbStairs(self, n: int) -> int:
        a,b=1,1
        while n>0:
            a,b = b,a+b
            n-=1
        return a
