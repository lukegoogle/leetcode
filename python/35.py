def searchInsert(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return left

# Example Output
print(f"Output for ([1, 3, 5, 6], 5): {searchInsert([1, 3, 5, 6], 5)}")
print(f"Output for ([1, 3, 5, 6], 2): {searchInsert([1, 3, 5, 6], 2)}")
print(f"Output for ([1, 3, 5, 6], 7): {searchInsert([1, 3, 5, 6], 7)}")