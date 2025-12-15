class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n = len(nums)
        i = 0
        while i < n:
            val = nums[i]
            correct_idx = val - 1
            if 1 <= val <= n and nums[correct_idx] != val:
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
            else:
                i += 1
        
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        return n + 1