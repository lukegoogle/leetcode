class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []
        used = [False] * len(nums)
        
        def backtrack(current_permutation):
            if len(current_permutation) == len(nums):
                result.append(list(current_permutation))
                return

            for i in range(len(nums)):
                if used[i]:
                    continue
                
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue
                
                used[i] = True
                current_permutation.append(nums[i])
                backtrack(current_permutation)
                current_permutation.pop()
                used[i] = False

        backtrack([])
        return result