class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        n = len(mat)
        mid = n//2
        s = 0
        for i in range(n):
            s+=mat[i][i]
            s+=mat[n-i-1][i]

        if n%2!=0:
            s-=mat[mid][mid]

        return s
