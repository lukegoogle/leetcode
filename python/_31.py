class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        
        n = len(nums)
        i = n - 2
        
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
            
        if i >= 0:
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
            
        left, right = i + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

# --- Example Usage Code ---

sol = Solution()
print("--- Next Permutation Examples ---")

# Helper function to test and print the result
def test_permutation(nums_list):
    original = list(nums_list)
    sol.nextPermutation(nums_list)
    print(f"Input: {original}")
    print(f"Output: {nums_list}")

# Test Case 1: Standard case
test_permutation([1, 2, 3]) # Expected: [1, 3, 2]

# Test Case 2: Array needs partial reversal and swap
test_permutation([3, 2, 1]) # Expected: [1, 2, 3] (Sorted descending, so becomes the lowest)

# Test Case 3: Finding the pivot and swap candidate
test_permutation([1, 1, 5]) # Expected: [1, 5, 1]

# Test Case 4: Complex swap and reverse
test_permutation([1, 5, 8, 4, 7, 6, 5, 3, 1]) # Expected: [1, 5, 8, 5, 1, 3, 4, 6, 7]

# Test Case 5: Single element
test_permutation([4]) # Expected: [4]