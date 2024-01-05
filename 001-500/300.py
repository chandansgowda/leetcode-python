class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        packs = []

        for num in nums:
            if not packs or num > packs[-1]:
                packs.append(num)
            else:
                i = bisect.bisect_left(packs, num)
                packs[i] = num
        
        return len(packs)
        
