class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        top = left = 0
        down = m-1
        right = n-1
        d = 0 #direction
        ans = []

        while (top<=down and left<=right):
            if (d==0):
                for i in range(top,right+1):
                    ans.append(matrix[top][i])
                top += 1
            elif (d==1):
                for i in range(top,down+1):
                    ans.append(matrix[i][right])
                right -= 1
            elif (d==2):
                for i in reversed(range(left, right+1)):
                    ans.append(matrix[down][i])
                down -= 1
            elif (d==3):
                for i in reversed(range(top, down+1)):
                    ans.append(matrix[i][left])
                left += 1
                
            d = (d+1)%4

        return ans
