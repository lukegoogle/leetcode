def permuteUnique(nums: list[int]) -> list[list[int]]:
    nums.sort()
    result = []
    
    def backtrack(current_permutation, used):
        if len(current_permutation) == len(nums):
            result.append(list(current_permutation))
            return
            
        for i in range(len(nums)):
            if used[i]:
                continue
            if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                continue
                
            current_permutation.append(nums[i])
            used[i] = True
            backtrack(current_permutation, used)
            used[i] = False
            current_permutation.pop()

    backtrack([], [False] * len(nums))
    return result

# Example Output
print(f"Output for [1, 1, 2]: {permuteUnique([1, 1, 2])}")
print(f"Output for [2, 2, 1, 1]: {permuteUnique([2, 2, 1, 1])}")