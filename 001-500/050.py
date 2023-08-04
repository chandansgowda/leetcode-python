class Solution:
    def myPow(self, x: float, n: int) -> float:
        def solve(x,n):
            if x==0:
                return 0
            if n==0:
                return 1
            res = solve(x,n//2)
            res *= res
            return res*x if n%2!=0 else res

        res = solve(x,abs(n))
        return res if n>0 else 1/res
