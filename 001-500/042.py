# Exceeds Time Limit
class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        for i in range(1,len(height)-1):
            bar_height = min(max(height[:i]), max(height[i+1:]))
            if bar_height>height[i]:
                water += bar_height-height[i]
        return water
