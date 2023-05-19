class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxVol = 0
        i,j=0,len(height)-1
        while i<j:
            h = min(height[i],height[j])
            w = j-i
            vol = h*w
            maxVol = max(maxVol,vol)
            if height[i]>height[j]:
                j-=1
            else:
                i+=1
        return maxVol
