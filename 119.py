class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [[1]]
        for _ in range(rowIndex):
            x = res.pop()
            res.append(list(map(add, x+[0], [0]+x)))

        return res[0]
