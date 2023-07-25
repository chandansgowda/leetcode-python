class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        maxLeftArr = [0]*len(height)
        maxRightArr = [0]*len(height)

        maxLeft = height[0]
        for i in range(1,len(height)):
            maxLeftArr[i] = maxLeft
            if height[i]>maxLeft:
                maxLeft=height[i]

        maxRight = height[-1]
        for i in reversed(range(len(height)-1)):
            maxRightArr[i] = maxRight
            if height[i]>maxRight:
                maxRight=height[i]

        for i in range(1,len(height)-1):
            bar_height = min(maxLeftArr[i], maxRightArr[i])
            if bar_height>height[i]:
                water += bar_height-height[i]
        return water
        


# Exceeds Time Limit
class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        for i in range(1,len(height)-1):
            bar_height = min(max(height[:i]), max(height[i+1:]))
            if bar_height>height[i]:
                water += bar_height-height[i]
        return water
