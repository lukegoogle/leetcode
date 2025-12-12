def firstMissingPositive(nums: list[int]) -> int:
    n = len(nums)
    i = 0
    
    while i < n:
        correct_index = nums[i] - 1
        
        if 1 <= nums[i] <= n and nums[i] != nums[correct_index]:
            nums[i], nums[correct_index] = nums[correct_index], nums[i]
        else:
            i += 1
            
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1
            
    return n + 1

# Example Output
print(f"Output for [1, 2, 0]: {firstMissingPositive([1, 2, 0])}")
print(f"Output for [3, 4, -1, 1]: {firstMissingPositive([3, 4, -1, 1])}")
print(f"Output for [7, 8, 9, 11, 12]: {firstMissingPositive([7, 8, 9, 11, 12])}")