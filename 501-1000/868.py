class Solution:
    def binaryGap(self, n: int) -> int:
        count = 0
        temp = -1

        while n:
            if n&1:
                if temp==-1:
                    temp = 1
                else:
                    count = max(count,temp)
                    temp = 1
            else:
                if temp!=-1:
                    temp += 1
            n >>= 1
        return count
