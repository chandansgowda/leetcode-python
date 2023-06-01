from collections import defaultdict

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        g = defaultdict(list)
        for edge in edges:
            g[edge[0]].append(edge[1])
            g[edge[1]].append(edge[0])
        for s,dlist in g.items():
            if len(dlist)==len(g.keys())-1:
                return s
