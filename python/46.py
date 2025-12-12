def permute(nums: list[int]) -> list[list[int]]:
    result = []
    
    def backtrack(current_permutation):
        if len(current_permutation) == len(nums):
            result.append(list(current_permutation))
            return
            
        for num in nums:
            if num not in current_permutation:
                current_permutation.append(num)
                backtrack(current_permutation)
                current_permutation.pop()

    backtrack([])
    return result

# Example Output
print(f"Output for [1, 2, 3]: {permute([1, 2, 3])}")
print(f"Output for [0, 1]: {permute([0, 1])}")