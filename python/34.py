def searchRange(nums: list[int], target: int) -> list[int]:
    def find_bound(is_first):
        left, right = 0, len(nums) - 1
        result = -1
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                result = mid
                if is_first:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return result

    first = find_bound(True)
    if first == -1:
        return [-1, -1]
        
    last = find_bound(False)
    return [first, last]

# Example Output
print(f"Output for ([5, 7, 7, 8, 8, 10], 8): {searchRange([5, 7, 7, 8, 8, 10], 8)}")
print(f"Output for ([5, 7, 7, 8, 8, 10], 6): {searchRange([5, 7, 7, 8, 8, 10], 6)}")