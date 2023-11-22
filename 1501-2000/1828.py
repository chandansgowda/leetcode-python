class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        res = []
        count = 0
        for i in queries:
            x1,y1,r=i[0],i[1],i[2]
            for j in points:
                x2=j[0]
                y2=j[1]
                if (((x2 - x1)**2 + (y2 - y1)**2)**0.5) <= r :
                    count+=1
            res.append(count)
            count = 0
        return res
