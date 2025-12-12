def combinationSum2(candidates: list[int], target: int) -> list[list[int]]:
    candidates.sort()
    result = []
    
    def backtrack(current_combination, remaining, start_index):
        if remaining == 0:
            result.append(list(current_combination))
            return
            
        if remaining < 0:
            return
            
        i = start_index
        while i < len(candidates):
            candidate = candidates[i]
            current_combination.append(candidate)
            backtrack(current_combination, remaining - candidate, i + 1)
            current_combination.pop()
            
            next_i = i + 1
            while next_i < len(candidates) and candidates[next_i] == candidate:
                next_i += 1
            i = next_i
            
    backtrack([], target, 0)
    return result

# Example Output
print(f"Output for ([10, 1, 2, 7, 6, 1, 5], 8): {combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)}")
print(f"Output for ([2, 5, 2, 1, 2], 5): {combinationSum2([2, 5, 2, 1, 2], 5)}")