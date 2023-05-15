class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        res = []
        for i in range(9):
            for j in range(9):
                ele = board[i][j]
                if ele != ".":
                    res += [(i,ele), (ele,j), (i//3,j//3,ele)]
        return len(res)==len(set(res))
        
