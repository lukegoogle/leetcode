class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        
        def find_bound(is_first):
            L, R = 0, len(nums) - 1
            idx = -1
            
            while L <= R:
                mid = (L + R) // 2
                if nums[mid] == target:
                    idx = mid
                    if is_first:
                        R = mid - 1
                    else:
                        L = mid + 1
                elif nums[mid] < target:
                    L = mid + 1
                else:
                    R = mid - 1
            return idx
            
        first = find_bound(True)
        if first == -1:
            return [-1, -1]
            
        last = find_bound(False)
        return [first, last]
    
# --- Example Usage Code ---

sol = Solution()
print("--- Find First and Last Position of Element Examples ---")

# Test Case 1: Standard case with target found multiple times
nums1 = [5, 7, 7, 8, 8, 10]
target1 = 8
result1 = sol.searchRange(nums1, target1)
print(f"Input: {nums1}, target={target1}")
print(f"Output: {result1} (Expected: [3, 4])")

# Test Case 2: Target found once
nums2 = [1, 2, 3, 4, 5]
target2 = 3
result2 = sol.searchRange(nums2, target2)
print(f"\nInput: {nums2}, target={target2}")
print(f"Output: {result2} (Expected: [2, 2])")

# Test Case 3: Target not found
nums3 = [5, 7, 7, 8, 8, 10]
target3 = 6
result3 = sol.searchRange(nums3, target3)
print(f"\nInput: {nums3}, target={target3}")
print(f"Output: {result3} (Expected: [-1, -1])")

# Test Case 4: Empty array
nums4 = []
target4 = 0
result4 = sol.searchRange(nums4, target4)
print(f"\nInput: {nums4}, target={target4}")
print(f"Output: {result4} (Expected: [-1, -1])")

# Test Case 5: Target is the first element
nums5 = [1, 1, 1, 2, 3]
target5 = 1
result5 = sol.searchRange(nums5, target5)
print(f"\nInput: {nums5}, target={target5}")
print(f"Output: {result5} (Expected: [0, 2])")