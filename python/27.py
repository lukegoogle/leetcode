def removeElement(nums: list[int], val: int) -> int:
    i = 0
    n = len(nums)
    
    while i < n:
        if nums[i] == val:
            nums[i] = nums[n - 1]
            n -= 1
        else:
            i += 1
            
    return n

# Example Output
nums1 = [3, 2, 2, 3]
val1 = 3
k1 = removeElement(nums1, val1)
print(f"Output for [3, 2, 2, 3], val=3: k={k1}, nums={nums1[:k1]}")

nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
val2 = 2
k2 = removeElement(nums2, val2)
print(f"Output for [0, 1, 2, 2, 3, 0, 4, 2], val=2: k={k2}, nums={nums2[:k2]}")