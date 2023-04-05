class Solution:
    def rotate(self, m: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m.reverse()
        #transposing
        for i in range(len(m)):
            for j in range(i):
                m[i][j], m[j][i] = m[j][i], m[i][j]
