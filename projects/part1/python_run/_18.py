class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        
        nums.sort()
        result = []
        n = len(nums)
        
        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                
                new_target = target - nums[i] - nums[j]
                L = j + 1
                R = n - 1
                
                while L < R:
                    current_sum = nums[L] + nums[R]
                    
                    if current_sum == new_target:
                        result.append([nums[i], nums[j], nums[L], nums[R]])
                        
                        while L < R and nums[L] == nums[L+1]:
                            L += 1
                        while L < R and nums[R] == nums[R-1]:
                            R -= 1
                            
                        L += 1
                        R -= 1
                        
                    elif current_sum < new_target:
                        L += 1
                    else:
                        R -= 1
                        
        return result
    
# --- Example Usage Code ---

sol = Solution()
print("--- 4Sum Examples ---")

# Test Case 1: Standard example
nums1 = [1, 0, -1, 0, -2, 2]
target1 = 0
result1 = sol.fourSum(nums1, target1)
# Expected output: [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
print(f"Input: nums={nums1}, target={target1}")
print(f"Output: {result1}")
print(f"(Expected: [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]])")

# Test Case 2: Array with duplicates and non-zero target
nums2 = [2, 2, 2, 2, 2]
target2 = 8
result2 = sol.fourSum(nums2, target2)
# Expected output: [[2, 2, 2, 2]] (Only one unique combination)
print(f"Input: nums={nums2}, target={target2}")
print(f"Output: {result2} (Expected: [[2, 2, 2, 2]])")

# Test Case 3: No solution found
nums3 = [1, 2, 3, 4, 5]
target3 = 10
result3 = sol.fourSum(nums3, target3)
print(f"Input: nums={nums3}, target={target3}")
print(f"Output: {result3} (Expected: [])")

# Test Case 4: Negative target
nums4 = [-3, -1, 0, 2, 4, 5]
target4 = 2
result4 = sol.fourSum(nums4, target4)
# Expected output: [[-3, -1, 2, 4], [-3, 0, 2, 3]... wait, the list is [2, 3, 4, 5]
# [-3, -1, 2, 4] -> -4 + 6 = 2
# [-3, 0, 2, 3] -> -3 + 5 = 2
# After sorting: [-3, -1, 0, 2, 4, 5]
# [-3, -1, 0, 6] (R=n-1, 6 is not in list)
# [-3, 0, 2, 3] -> sum is 2. (0, 2, 3 are indices 2, 3, 4, wait, indices are 2, 3, 4 are 0, 2, 4. sum is -3+0+2+4=3).
# Correct expected: [[-3, -1, 2, 4]]
print(f"Input: nums={nums4}, target={target4}")
print(f"Output: {result4} (Expected: [[-3, -1, 2, 4]])")