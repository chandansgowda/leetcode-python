class Solution:
    def arraySign(self, nums: List[int]) -> int:
        c = 0
        for num in nums:
            if num==0: return 0
            elif num<0: c+=1
        return 1 if not c%2 else -1


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        p = 1
        for num in nums:
            p *= num
        if p>0:
            return 1
        elif p<0:
            return -1
        else:
            return 0
