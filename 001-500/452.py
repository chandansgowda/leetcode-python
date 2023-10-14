class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[1])
        arrows=0
        end = float('-inf')
        for balloon in points:
            if balloon[0]>end:
                end = balloon[1]
                arrows += 1

        return arrows
