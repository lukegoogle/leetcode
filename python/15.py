def threeSum(nums: list[int]) -> list[list[int]]:
    nums.sort()
    result = []
    n = len(nums)
    
    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
            
        target = -nums[i]
        left = i + 1
        right = n - 1
        
        while left < right:
            current_sum = nums[left] + nums[right]
            
            if current_sum == target:
                result.append([nums[i], nums[left], nums[right]])
                
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                    
                left += 1
                right -= 1
            elif current_sum < target:
                left += 1
            else:
                right -= 1
                
    return result

# Example Output
print("--- LeetCode 15 ---")
print(f"Output for [-1, 0, 1, 2, -1, -4]: {threeSum([-1, 0, 1, 2, -1, -4])}")
print(f"Output for [0, 1, 1]: {threeSum([0, 1, 1])}")