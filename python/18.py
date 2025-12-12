def fourSum(nums: list[int], target: int) -> list[list[int]]:
    nums.sort()
    result = []
    n = len(nums)
    
    for i in range(n - 3):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
            
        for j in range(i + 1, n - 2):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
                
            current_target = target - nums[i] - nums[j]
            left = j + 1
            right = n - 1
            
            while left < right:
                current_sum = nums[left] + nums[right]
                
                if current_sum == current_target:
                    result.append([nums[i], nums[j], nums[left], nums[right]])
                    
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                        
                    left += 1
                    right -= 1
                elif current_sum < current_target:
                    left += 1
                else:
                    right -= 1
                    
    return result

# Example Output
print("--- LeetCode 18 ---")
print(f"Output for ([1, 0, -1, 0, -2, 2], 0): {fourSum([1, 0, -1, 0, -2, 2], 0)}")
print(f"Output for ([2, 2, 2, 2, 2], 8): {fourSum([2, 2, 2, 2, 2], 8)}")