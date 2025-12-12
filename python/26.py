def removeDuplicates(nums: list[int]) -> int:
    if not nums:
        return 0

    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
            
    return i + 1

# Example Output
nums1 = [1, 1, 2]
k1 = removeDuplicates(nums1)
print(f"Output for [1, 1, 2]: k={k1}, nums={nums1[:k1]}")

nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
k2 = removeDuplicates(nums2)
print(f"Output for [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]: k={k2}, nums={nums2[:k2]}")