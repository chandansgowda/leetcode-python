class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def helper(i,amt):
            if i==0:
                if amt%coins[0]==0:
                    return amt//coins[0]
                else:
                    return float('inf')
            not_pick = helper(i-1,amt)
            if coins[i]<=amt:
                pick = 1 + helper(i,amt-coins[i])
            else:
                pick = float('inf')
            return min(pick,not_pick)

        res = helper(len(coins)-1, amount)
        return res if res!=float('inf') else -1
