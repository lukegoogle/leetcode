class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
                
        return i
    
# --- Example Usage Code ---

sol = Solution()
print("--- Remove Element Examples ---")

# Test Case 1: Standard case
nums1 = [3, 2, 2, 3]
val1 = 3
original_nums1 = list(nums1) # Keep original for printout
k1 = sol.removeElement(nums1, val1)
# The first k elements should be [2, 2]
print(f"Input: {original_nums1}, val={val1}")
print(f"Output Length (k): {k1} (Expected: 2)")
print(f"Modified Array (first k elements): {nums1[:k1]}")

# Test Case 2: Target value is not present
nums2 = [4, 5]
val2 = 1
original_nums2 = list(nums2)
k2 = sol.removeElement(nums2, val2)
# The first k elements should be [4, 5]
print(f"\nInput: {original_nums2}, val={val2}")
print(f"Output Length (k): {k2} (Expected: 2)")
print(f"Modified Array (first k elements): {nums2[:k2]}")

# Test Case 3: Target value is all elements
nums3 = [5, 5, 5]
val3 = 5
original_nums3 = list(nums3)
k3 = sol.removeElement(nums3, val3)
# The first k elements should be []
print(f"\nInput: {original_nums3}, val={val3}")
print(f"Output Length (k): {k3} (Expected: 0)")
print(f"Modified Array (first k elements): {nums3[:k3]}")

# Test Case 4: Longer array
nums4 = [0, 1, 2, 2, 3, 0, 4, 2]
val4 = 2
original_nums4 = list(nums4)
k4 = sol.removeElement(nums4, val4)
# The first k elements should be [0, 1, 3, 0, 4] (order may vary, but these 5 unique elements must be present)
print(f"\nInput: {original_nums4}, val={val4}")
print(f"Output Length (k): {k4} (Expected: 5)")
print(f"Modified Array (first k elements): {nums4[:k4]}")