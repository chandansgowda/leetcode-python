class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        i,res,curMax=0,0,0
        while True:
            if len(grid[i])==0:
                break
            grid[i].sort()
            curMax = max(curMax,grid[i][-1])
            grid[i].pop()
            i+=1
            if i==len(grid):
                res+=curMax
                curMax,i=0,0
        return res


class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            grid[i].sort()
        
        grid = list(zip(*grid))

        return sum(max(row) for row in grid)
        
