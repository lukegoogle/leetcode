def combinationSum(candidates: list[int], target: int) -> list[list[int]]:
    result = []
    
    def backtrack(current_combination, remaining, start_index):
        if remaining == 0:
            result.append(list(current_combination))
            return
            
        if remaining < 0:
            return
            
        for i in range(start_index, len(candidates)):
            candidate = candidates[i]
            current_combination.append(candidate)
            backtrack(current_combination, remaining - candidate, i)
            current_combination.pop()
            
    backtrack([], target, 0)
    return result

# Example Output
print(f"Output for ([2, 3, 6, 7], 7): {combinationSum([2, 3, 6, 7], 7)}")
print(f"Output for ([2, 3, 5], 8): {combinationSum([2, 3, 5], 8)}")