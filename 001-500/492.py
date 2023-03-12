class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        import math
        mid = int(math.sqrt(area))
        while mid>0:
            if area%mid==0:
                return [int(area/mid),mid]
            mid-=1
        
