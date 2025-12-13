class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_to_index = {} 
        
        for i, num in enumerate(nums):
            complement = target - num
            
            if complement in num_to_index:
                return [num_to_index[complement], i]
            
            num_to_index[num] = i
            
        return []
    
solver = Solution()

# Test Case 1
nums1 = [2, 7, 11, 15]
target1 = 9
result1 = solver.twoSum(nums1, target1)
print(f"Input: {nums1}, Target: {target1}")
print(f"Output: {result1}")

# Test Case 2
nums2 = [3, 2, 4]
target2 = 6
result2 = solver.twoSum(nums2, target2)
print(f"Input: {nums2}, Target: {target2}")
print(f"Output: {result2}")