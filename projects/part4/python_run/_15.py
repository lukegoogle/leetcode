class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        
        nums.sort()
        result = []
        n = len(nums)
        
        for i in range(n - 2):
            if nums[i] > 0:
                break
            
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            target = -nums[i]
            L = i + 1
            R = n - 1
            
            while L < R:
                current_sum = nums[L] + nums[R]
                
                if current_sum == target:
                    result.append([nums[i], nums[L], nums[R]])
                    
                    while L < R and nums[L] == nums[L+1]:
                        L += 1
                    while L < R and nums[R] == nums[R-1]:
                        R -= 1
                        
                    L += 1
                    R -= 1
                    
                elif current_sum < target:
                    L += 1
                    
                else:
                    R -= 1
                    
        return result
    
# --- Example Usage Code ---

sol = Solution()
print("--- 3Sum Examples ---")

# Test Case 1: Standard example with duplicates
nums1 = [-1, 0, 1, 2, -1, 4]
result1 = sol.threeSum(nums1)
# Expected output (after sorting): [[-1, -1, 2], [-1, 0, 1]]
print(f"Input: {nums1}")
print(f"Output: {result1} (Expected: [[-1, -1, 2], [-1, 0, 1]])")

# Test Case 2: No solution
nums2 = [0, 1, 1]
result2 = sol.threeSum(nums2)
print(f"Input: {nums2}")
print(f"Output: {result2} (Expected: [])")

# Test Case 3: Only zeros
nums3 = [0, 0, 0]
result3 = sol.threeSum(nums3)
print(f"Input: {nums3}")
print(f"Output: {result3} (Expected: [[0, 0, 0]])")

# Test Case 4: Longer array with various numbers and duplicates
nums4 = [-2, 0, 1, 1, 2]
result4 = sol.threeSum(nums4)
# Expected output: [[-2, 0, 2], [-2, 1, 1]]
print(f"Input: {nums4}")
print(f"Output: {result4} (Expected: [[-2, 0, 2], [-2, 1, 1]])")

# Test Case 5: Array that breaks early (Optimization 1)
nums5 = [1, 2, 3]
result5 = sol.threeSum(nums5)
print(f"Input: {nums5}")
print(f"Output: {result5} (Expected: [])")