class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        
        L, R = 0, len(nums) - 1
        
        while L <= R:
            mid = (L + R) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                L = mid + 1
            else:
                R = mid - 1
                
        return L
    
# --- Example Usage Code ---

sol = Solution()
print("--- Search Insert Position Examples ---")

# Test Case 1: Target found
nums1 = [1, 3, 5, 6]
target1 = 5
result1 = sol.searchInsert(nums1, target1)
print(f"Input: {nums1}, target={target1}")
print(f"Output: {result1} (Expected: 2)")

# Test Case 2: Target not found, insert in middle
nums2 = [1, 3, 5, 6]
target2 = 2
result2 = sol.searchInsert(nums2, target2)
print(f"\nInput: {nums2}, target={target2}")
print(f"Output: {result2} (Expected: 1)")

# Test Case 3: Target not found, insert at the end
nums3 = [1, 3, 5, 6]
target3 = 7
result3 = sol.searchInsert(nums3, target3)
print(f"\nInput: {nums3}, target={target3}")
print(f"Output: {result3} (Expected: 4)")

# Test Case 4: Target not found, insert at the beginning
nums4 = [1, 3, 5, 6]
target4 = 0
result4 = sol.searchInsert(nums4, target4)
print(f"\nInput: {nums4}, target={target4}")
print(f"Output: {result4} (Expected: 0)")

# Test Case 5: Empty array
nums5 = []
target5 = 5
result5 = sol.searchInsert(nums5, target5)
print(f"\nInput: {nums5}, target={target5}")
print(f"Output: {result5} (Expected: 0)")