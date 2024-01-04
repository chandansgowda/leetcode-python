class Solution:
    def minOperations(self, nums: List[int]) -> int:
        d = defaultdict(int)
        for num in nums:
            d[num] += 1

        if min(d.values()) == 1:
            return -1
        
        return sum(c // 3 + (c % 3 > 0) for c in d.values())

        
