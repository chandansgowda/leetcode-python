class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        g = {}
        x = defaultdict(list)
        for i in range(1,n+1):
            g[i] = []

        for s,d in trust:
            g[s].append(d)
            x[d].append(s)
        
        for s,d in g.items():
            if len(d)==0:
                if len(x[s])==n-1:
                    return s
        
        return -1
