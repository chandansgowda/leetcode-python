class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        M = 10**9 + 7
        d = [0] + [1] * (k + 1)
        for n in range(2, n+1):
            new = [0]
            for k in range(k+1):
                v = d[k+1]
                v -= d[k-n+1] if k >= n else 0
                new.append( (new[-1] + v) % M )
            d = new
        return (d[k+1] - d[k]) % M
