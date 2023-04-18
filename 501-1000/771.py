class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        c = 0
        for stone in stones:
            c += stone in jewels
        return c
