def trap(height: list[int]) -> int:
    if not height:
        return 0
        
    left, right = 0, len(height) - 1
    max_left = height[left]
    max_right = height[right]
    total_water = 0
    
    while left < right:
        if max_left < max_right:
            left += 1
            max_left = max(max_left, height[left])
            total_water += max_left - height[left]
        else:
            right -= 1
            max_right = max(max_right, height[right])
            total_water += max_right - height[right]
            
    return total_water

# Example Output
print(f"Output for [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]: {trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])}")
print(f"Output for [4, 2, 0, 3, 2, 5]: {trap([4, 2, 0, 3, 2, 5])}")