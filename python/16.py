def threeSumClosest(nums: list[int], target: int) -> int:
    nums.sort()
    n = len(nums)
    closest_sum = float('inf')

    for i in range(n - 2):
        left = i + 1
        right = n - 1
        
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            
            if abs(current_sum - target) < abs(closest_sum - target):
                closest_sum = current_sum
                
            if current_sum < target:
                left += 1
            elif current_sum > target:
                right -= 1
            else:
                return target
                
    return closest_sum

# Example Output
print("--- LeetCode 16 ---")
print(f"Output for ([-1, 2, 1, -4], 1): {threeSumClosest([-1, 2, 1, -4], 1)}")
print(f"Output for ([0, 0, 0], 1): {threeSumClosest([0, 0, 0], 1)}")