class Solution:
    def sortString(self, s: str) -> str:
        cntlist = collections.Counter(s)
        asc = True
        ans = ""
        while cntlist:
            for c in sorted(cntlist) if asc else reversed(sorted(cntlist)):
                ans += c
                cntlist[c]-=1
                if cntlist[c]==0:
                    del cntlist[c]
            asc = not asc

        return ans
