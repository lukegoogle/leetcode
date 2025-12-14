class Solution:
    def search(self, nums: list[int], target: int) -> int:
        
        L, R = 0, len(nums) - 1
        
        while L <= R:
            mid = (L + R) // 2
            
            if nums[mid] == target:
                return mid
            
            if nums[L] <= nums[mid]:
                if nums[L] <= target < nums[mid]:
                    R = mid - 1
                else:
                    L = mid + 1
            else:
                if nums[mid] < target <= nums[R]:
                    L = mid + 1
                else:
                    R = mid - 1
                    
        return -1
    
# --- Example Usage Code ---

sol = Solution()
print("--- Search in Rotated Sorted Array Examples ---")

# Test Case 1: Target found in the left half of the original array (right of pivot)
nums1 = [4, 5, 6, 7, 0, 1, 2]
target1 = 0
result1 = sol.search(nums1, target1)
print(f"Input: {nums1}, target={target1}")
print(f"Output: {result1} (Expected: 4)")

# Test Case 2: Target found in the right half of the original array (left of pivot)
nums2 = [4, 5, 6, 7, 0, 1, 2]
target2 = 6
result2 = sol.search(nums2, target2)
print(f"\nInput: {nums2}, target={target2}")
print(f"Output: {result2} (Expected: 2)")

# Test Case 3: Target not found
nums3 = [4, 5, 6, 7, 0, 1, 2]
target3 = 3
result3 = sol.search(nums3, target3)
print(f"\nInput: {nums3}, target={target3}")
print(f"Output: {result3} (Expected: -1)")

# Test Case 4: Array with a single rotation (pivot is nums[0])
nums4 = [1, 3]
target4 = 3
result4 = sol.search(nums4, target4)
print(f"\nInput: {nums4}, target={target4}")
print(f"Output: {result4} (Expected: 1)")

# Test Case 5: Pivot at the end
nums5 = [3, 1]
target5 = 1
result5 = sol.search(nums5, target5)
print(f"\nInput: {nums5}, target={target5}")
print(f"Output: {result5} (Expected: 1)")