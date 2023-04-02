class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        def reverseInteger(n):
            r = 0
            while n>0:
                r = 10*r + n%10
                n //= 10
            return r
        s = set(nums)
        for n in nums:
            s.add(reverseInteger(n))
        return len(s)
            
