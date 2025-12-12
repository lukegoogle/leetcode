def twoSum(nums: list[int], target: int) -> list[int]:
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i

# Example Output
print("--- LeetCode 1 ---")
print(f"Output for ([2, 7, 11, 15], 9): {twoSum([2, 7, 11, 15], 9)}")
print(f"Output for ([3, 2, 4], 6): {twoSum([3, 2, 4], 6)}")