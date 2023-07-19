class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    m.add((i,j))
        for r,c in m:
            for i in range(len(matrix[0])):
                matrix[r][i]=0
            for j in range(len(matrix)):
                matrix[j][c]=0
        
