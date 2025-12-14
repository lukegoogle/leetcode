class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        
        nums.sort()
        n = len(nums)
        closest_sum = nums[0] + nums[1] + nums[2]
        
        for i in range(n - 2):
            L = i + 1
            R = n - 1
            
            while L < R:
                current_sum = nums[i] + nums[L] + nums[R]
                
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                
                if current_sum < target:
                    L += 1
                elif current_sum > target:
                    R -= 1
                else:
                    return current_sum
                    
        return closest_sum
    
# --- Example Usage Code ---

sol = Solution()
print("--- 3Sum Closest Examples ---")

# Test Case 1: Standard example
nums1 = [-1, 2, 1, -4]
target1 = 1
result1 = sol.threeSumClosest(nums1, target1)
# Expected: 2 (since -1 + 2 + 1 = 2)
print(f"Input: nums={nums1}, target={target1}")
print(f"Output: {result1} (Expected: 2)")

# Test Case 2: Target is 0
nums2 = [0, 0, 0]
target2 = 1
result2 = sol.threeSumClosest(nums2, target2)
# Expected: 0
print(f"Input: nums={nums2}, target={target2}")
print(f"Output: {result2} (Expected: 0)")

# Test Case 3: Negative numbers and target
nums3 = [1, 1, 1, 0]
target3 = -100
result3 = sol.threeSumClosest(nums3, target3)
# Expected: 2 (1 + 1 + 0 = 2, the closest sum possible)
print(f"Input: nums={nums3}, target={target3}")
print(f"Output: {result3} (Expected: 2)")

# Test Case 4: Target is reached exactly
nums4 = [1, 2, 3, 4, 5]
target4 = 7
result4 = sol.threeSumClosest(nums4, target4)
# Expected: 7 (2 + 1 + 4 = 7, or 3 + 2 + 2 = 7 etc.)
print(f"Input: nums={nums4}, target={target4}")
print(f"Output: {result4} (Expected: 7)")