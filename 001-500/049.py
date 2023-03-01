from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return list(ans.values())

    
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}

        for s in strs:
            if tuple(sorted(s)) in ans:
                ans[tuple(sorted(s))].append(s)
            else:
                ans[tuple(sorted(s))] = [s]
        return list(ans.values())
