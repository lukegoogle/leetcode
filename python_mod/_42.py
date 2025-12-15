class Solution:
    def trap(self, height: list[int]) -> int:
        if not height:
            return 0
        
        total_water = 0
        left = 0
        right = len(height) - 1
        maxL = height[left]
        maxR = height[right]
        
        while left < right:
            if maxL < maxR:
                left += 1
                maxL = max(maxL, height[left])
                total_water += maxL - height[left]
            else:
                right -= 1
                maxR = max(maxR, height[right])
                total_water += maxR - height[right]
                
        return total_water