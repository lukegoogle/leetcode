class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        
        if not nums:
            return 0
        
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
                
        return i + 1
    
# --- Example Usage Code ---

sol = Solution()
print("--- Remove Duplicates from Sorted Array Examples ---")

# Test Case 1: Standard case
nums1 = [1, 1, 2]
original_nums1 = list(nums1) # Keep original for printout
k1 = sol.removeDuplicates(nums1)
# The first k elements should be [1, 2]
print(f"Input: {original_nums1}")
print(f"Output Length (k): {k1} (Expected: 2)")
print(f"Modified Array (first k elements): {nums1[:k1]}")

# Test Case 2: Many duplicates
nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
original_nums2 = list(nums2)
k2 = sol.removeDuplicates(nums2)
# The first k elements should be [0, 1, 2, 3, 4]
print(f"\nInput: {original_nums2}")
print(f"Output Length (k): {k2} (Expected: 5)")
print(f"Modified Array (first k elements): {nums2[:k2]}")

# Test Case 3: No duplicates
nums3 = [10, 20, 30]
original_nums3 = list(nums3)
k3 = sol.removeDuplicates(nums3)
# The first k elements should be [10, 20, 30]
print(f"\nInput: {original_nums3}")
print(f"Output Length (k): {k3} (Expected: 3)")
print(f"Modified Array (first k elements): {nums3[:k3]}")

# Test Case 4: Empty array
nums4 = []
original_nums4 = list(nums4)
k4 = sol.removeDuplicates(nums4)
# Expected: 0
print(f"\nInput: {original_nums4}")
print(f"Output Length (k): {k4} (Expected: 0)")
print(f"Modified Array (first k elements): {nums4[:k4]}")