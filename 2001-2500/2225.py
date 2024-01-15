class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        d = defaultdict(int)
        players = set()
        for w,l in matches:
            d[l] += 1
            players.add(w)
            players.add(l)
        ans = [[],[]]
        for p in sorted(players):
            if d[p]==0 or d[p]==1:
                ans[d[p]].append(p)
        return ans
