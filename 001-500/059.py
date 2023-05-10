class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        m = [[0]*n for _ in range(n)]
        top = left = 0
        down = right = n-1
        d = 0 #direction
        ele = 1

        while (top<=down and left<=right):
            if d==0:
                for i in range(left,right+1):
                    m[top][i] = ele
                    ele += 1
                top += 1
            
            if d==1:
                for i in range(top,down+1):
                    m[i][right] = ele
                    ele += 1
                right -= 1

            if d==2:
                for i in reversed(range(left,right+1)):
                    m[down][i] = ele
                    ele += 1
                down -= 1

            if d==3:
                for i in reversed(range(top,down+1)):
                    m[i][left] = ele
                    ele += 1
                left += 1

            d = (d+1)%4
        
        return m


